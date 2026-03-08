import os

class Config():
    def __init__(self):
        self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","text")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")
        self.KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID" , "text-tracker")
        self.ELASTIC_URI = os.getenv("ELASTIC_URI",'http://localhost:9200')
        self.ELASTIC_INDEX = os.getenv("ELASTIC_INDEX","podcasts")

        print(f"""Config created - 
                            ELASTIC_URI:{self.ELASTIC_URI}
                            ELASTIC_INDEX:{self.ELASTIC_INDEX}
                            KAFKA_TOPIC:{self.KAFKA_TOPIC}""")
