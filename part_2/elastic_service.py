from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk



class ElasticsearchClient:
    def __init__(self, es_uri, index_name, logger):
        self.es_uri = es_uri
        self.index_name = index_name
        self.logger = logger
        self.es = Elasticsearch(self.es_uri)

        self.logger.info("ElasticsearchClient created successfully")

        self._create_index()

    def _create_index(self):

        if self.es.indices.exists(index=self.index_name):
            self.logger.info(f"ElasticsearchClient - Index {self.index_name} already exists")
            return

        mapping = {
            "mappings": {
                "properties": {
                    "id": {"type": "keyword"},
                    "name": {"type": "keyword"},
                    "ctime": {"type": "float"},
                    "size_b": {"type": "integer"},
                    "full_path": {"type": "keyword"}
                }
            }
        }

        self.es.indices.create(index=self.index_name, body=mapping)
        self.logger.info(f"ElasticsearchClient - Index {self.index_name} created")

    def insert(self, doc: dict, id: str):
        try:
            response = self.es.index(
                index=self.index_name,
                id=id,
                document=doc,
                refresh=True
            )
            self.logger.debug(
                f"ElasticsearchClient - Document {id} inserted successfully. "
                f"Result: {response.get('result')}\n"
                f"total in index:{self.index_name} - {self.es.count(index=self.index_name)['count']}"
            )

        except Exception as e:
            self.logger.error(
                f"ElasticsearchClient - Failed to insert document {id}: {str(e)}"
            )

