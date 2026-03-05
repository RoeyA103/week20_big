import speech_recognition as sr

# r = sr.Recognizer()


# harvard = sr.AudioFile("download.wav")
# with harvard as source:
#         audio = r.record(source)

# res = r.recognize_google(audio_data=audio)

# print(res)

import elasticsearch
from elasticsearch.helpers import scan

es = elasticsearch.Elasticsearch('http://localhost:9200')


docs = scan(
    es,
    index="podcasts",
    query={"query": {"match_all": {}}}
)

for doc in docs:
    doc= doc["_source"]
    print(doc)