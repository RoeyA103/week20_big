from elasticsearch import Elasticsearch 


class ElasticService():
    def __init__(self, es_uri, index_name):
        self.es_uri = es_uri
        self.index_name = index_name
        # self.logger = logger
        self.es = Elasticsearch(self.es_uri)

        # self.logger.info("ElasticService created successfully")

       
    def run_query(self,query:dict):
        try:
            res = self.es.search(index=self.index_name,body=query)
            return [s["_source"] for s in res["hits"]["hits"]]
        except Exception as e:
            pass

    def run_agg_query(self,query):
        res = self.es.search(index=self.index_name,body=query)
        return res["aggregations"]
    def five_top_threat(self):
        query = {
            'query': {
            'term': {
            'bds_threat_level': 'high'}}}
        return self.run_query(query)
    
    def find_word(self,word:str):
        query = {
            "query":{
                "match":{
                    "extracted_txt":word
                }
            }
        }
        res = self.run_query(query)
        print(res)
        return res
    
    def count_higt_bds_percent(self):
        query = {
                "query":{"match":{'bds_threat_level':'high'}},
                'size':0,
                'aggs':{
                    'total_hight':{
                        'value_count':{
                            'field':'bds_threat_level.keyword'
                        }
                    }
                }
            }
        
        return self.run_agg_query(query)
