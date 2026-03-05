from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan

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
                    "extracted_txt":{"type":"text"}
                }
            }

            self.es.indices.put_mapping(index=self.index_name,body=mapping)
            self.logger.debug(f"ElasticService - Index {self.index_name} updated")
        except Exception as e:
            self.logger.error(f"ElasticService - could not update index: {e}")

    def get_all_doc(self):
        docs = scan(client=self.es,query={"query": {"match_all": {}}})
        return docs
    
    def update_doc(self,id:str,doc):
        try:
            res = self.es.update(index=self.index_name,id=id,doc=doc,refresh=True)

            self.logger.debug(f"ElasticService - doc:{doc} updeted, res:{res.get('result')}")
        except Exception as e:
            self.logger.error(f"ElasticService - could not update field: {e}")