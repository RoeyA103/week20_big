import json
from confluent_kafka import Producer ,error

class KafkaProducer():
    def __init__(self,logger,bootstrap_servers:str,topic:str):
        self.logger = logger
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        try:
            producer_config = {
                "bootstrap.servers": self.bootstrap_servers
            }

            self.producer = Producer(producer_config)
            self.logger.info("KafkaPublisher - connection to kafka succsses")
        
        except error.ProduceError as e:
            self.logger.error(f"KafkaPublisher - {e}")

    def produce(self,data:dict):
        def callback(err,msg):
            if err:
                self.logger.error(f"KafkaProducer - deleviry faild: {err}")
            else:
                self.logger.debug(f"KafkaProducer - delivered:{msg.value().decode('utf-8')}")

        val = json.dumps(data).encode("utf-8")

        self.producer.produce(topic=self.topic,value=val,callback=callback)  

        self.producer.poll(0)

        self.producer.flush()      