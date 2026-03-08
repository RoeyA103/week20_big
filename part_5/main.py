from fastapi import FastAPI
from elastic_service import ElasticService
import uvicorn

es = ElasticService(es_uri="http://localhost:9200",index_name="podcasts")
app = FastAPI()


@app.get("/")
def root():
    return {"message":"healty"}

@app.get("/5 top threat")
def five_top_threat():
    return es.five_top_threat()


@app.post("/find_word/{word}")
def find_word(word:str):
    return es.find_word(word)

@app.get("/count_higt_bds_percent")
def count_higt_bds_percent():
    return es.count_higt_bds_percent()


if __name__=="__main__":
    uvicorn.run("main:app",port=8080,reload=True)


