from elasticsearch import Elasticsearch , NotFoundError


class ElasticService():
    def __init__(self, es_uri, index_name, logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger
        self.es = Elasticsearch(self.es_uri)

        self.logger.info("ElasticService created successfully")

        self._update_index()

    def _update_index(self):
        try:
            mapping = {
                "properties":{
                    "bds_percent":{"type":"float"},
                    "is_bds":{"type":"bool"},
                    "bds_threat_level":{"type":"keyword"}
                }
            }

            self.es.indices.put_mapping(index=self.index_name,body=mapping)
            self.logger.debug(f"ElasticService - Index {self.index_name} updated")
        except Exception as e:
            self.logger.error(f"ElasticService - could not update index: {e}")

    def get_doc(self,doc_id:str):
        try:
            doc = self.es.get(index=self.index_name,id=doc_id)
            self.logger.debug(f"ElasticService - doc: {doc_id} found")
            return doc["_source"]
        
        except NotFoundError as e:
            self.logger.error(f"ElasticService - doc:{doc_id} not found")

        except Exception as e:
            self.logger.error(f"ElasticService - error in returning doc:{doc_id}")

    def update_doc(self,doc,doc_id):
        try:
            self.es.update(index=self.index_name,doc=doc,id=doc_id)

            self.logger.debug(f"Statistic - doc:{doc_id} updeted")

        except Exception as e:
            self.logger.errot(f"Statistic - error in updeted doc: {e}")
