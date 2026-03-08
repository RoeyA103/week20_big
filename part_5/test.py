from elasticsearch import Elasticsearch

query = {
            "query":{
                "match_all":{
                    
                }
            }
        }

es = Elasticsearch("http://localhost:9200")

# print(es.search(index="podcasts",body=query))
print(es.indices.get_mapping(index="podcasts"))