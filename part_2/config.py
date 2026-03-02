import os

class Config():
    def __init__(self):
        self.KAFKA_TOPIC = None
        self.KAFKA_BOOTSTRAP_SERVERS = None
        self.KAFKA_GROUP_ID = None
        self.MONGO_URI = None
        self.MONGO_DB_NAME = None
        self.ELASTIC_URI = None
        self.ELASTIC_INDEX = None

        self.load()
        self.validate()

        print(f"""Config created - KAFKA_TOPIC:{self.KAFKA_TOPIC},
                          KAFKA_BOOTSTRAP_SERVERS:{self.KAFKA_BOOTSTRAP_SERVERS},
                          KAFKA_GROUP_ID:{self.KAFKA_GROUP_ID}
                          MONGO_URI:{self.MONGO_URI}
                          MONGO_DB_NAME:{self.MONGO_DB_NAME}
                          ELASTIC_URI:{self.ELASTIC_URI}
                          ELASTIC_INDEX:{self.ELASTIC_INDEX}""")

    def load(self):
        self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","metadata")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")
        self.KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID" , "metadata-tracker")
        self.MONGO_URI = os.getenv("MONGO_URI","mongodb://localhost:27017")
        self.MONGO_DB_NAME = os.getenv("MONGO_DB_NAME","test")
        self.ELASTIC_URI = os.getenv("ELASTIC_URI",'http://localhost:9200')
        self.ELASTIC_INDEX = os.getenv("ELASTIC_INDEX","podcasts")

    def validate(self):
        missing = []

        if not self.KAFKA_TOPIC:
            missing.append("KAFKA_TOPIC")
        if not self.KAFKA_BOOTSTRAP_SERVERS:
            missing.append("KAFKA_BOOTSTRAP_SERVERS")
        if not self.KAFKA_GROUP_ID:
            missing.append("KAFKA_GROUP_ID")

        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        print("Config - all environments lodaed successfuly")

