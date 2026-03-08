import os

class Config():
    def __init__(self):
        self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","uploaded")
        self.KAFKA_TOPIC_PRODUCER = os.getenv("KAFKA_TOPIC_PRODUCER","text")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")
        self.KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID" , "metadata-tracker")
        self.MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017")
        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME","test")
        self.ELASTIC_URI = os.getenv("ELASTIC_URI",'http://localhost:9200')
        self.ELASTIC_INDEX = os.getenv("ELASTIC_INDEX","podcasts")

        print(f"""Config created - 
                            MONGO_URI:{self.MONGO_URI}
                            MONGO_DB_NAME:{self.MONGO_DB_NAME}
                            ELASTIC_URI:{self.ELASTIC_URI}
                            ELASTIC_INDEX:{self.ELASTIC_INDEX}""")
