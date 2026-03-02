import os

class Config():
    def __init__(self):
        self.KAFKA_TOPIC = None
        self.KAFKA_BOOTSTRAP_SERVERS = None
        self.DATA_PATH = None

        self.load()
        self.validate()

        print(f"""Config created - KAFKA_TOPIC:{self.KAFKA_TOPIC},\n
                          KAFKA_BOOTSTRAP_SERVERS:{self.KAFKA_BOOTSTRAP_SERVERS},\n
                          DATA_PATH:{self.DATA_PATH}
                          ELASTIC_URI:{self.ELASTIC_URI}""")

    def load(self):
        self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","metadata")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")
        self.DATA_PATH = os.getenv("DATA_PATH","podcast")
        self.ELASTIC_URI = os.getenv("ELASTIC_URI",'http://localhost:9200')

    def validate(self):
        missing = []

        if not self.KAFKA_TOPIC:
            missing.append("KAFKA_TOPIC")
        if not self.KAFKA_BOOTSTRAP_SERVERS:
            missing.append("KAFKA_BOOTSTRAP_SERVERS")
        if not self.DATA_PATH:
            missing.append("DATA_PATH")

        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
        
        print("Config - all environments lodaed successfuly")

