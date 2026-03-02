import os

class Config():
    def __init__(self,logger):
        self.logger = logger
        self.KAFKA_TOPIC = None
        self.KAFKA_BOOTSTRAP_SERVERS = None
        self.DATA_PATH = None

        self.load()
        self.validate()

        self.logger.info(f"""Config created - KAFKA_TOPIC:{self.KAFKA_TOPIC},\n
                          KAFKA_BOOTSTRAP_SERVERS:{self.KAFKA_BOOTSTRAP_SERVERS},\n
                          DATA_PATH:{self.DATA_PATH}""")

    def load(self):
        self.KAFKA_TOPIC = os.getenv("KAFKA_TOPIC","metadata")
        self.KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS","localhost:9092")
        self.DATA_PATH = os.getenv("DATA_PATH","podcast")

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
        
        self.logger.info("Config - all environments lodaed successfuly")

