import speech_recognition as sr

r = sr.Recognizer()

with open("download.wav","rb") as f:
    harvard = sr.AudioFile(f)
    with harvard as source:
        audio = r.record(source)

res = r.recognize_google(audio_data=audio)

print(res)

# import elasticsearch
# from elasticsearch.helpers import scan

# es = elasticsearch.Elasticsearch('http://localhost:9200')


# docs = scan(
#     es,
#     index="podcasts",
#     query={"query": {"match_all": {}}}
# )

# for doc in docs:
#     print(doc["_source"])