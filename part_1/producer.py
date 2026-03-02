from confluent_kafka import Producer ,error
import json

class KafkaPublisher():
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

    def publish(self,event):

        def delivery_report(err, msg):
            if err:
                self.logger.error(f"KafkaPublisher -  Delivery failed: {err}")
            else:
                self.logger.debug("KafkaPublisher - "
                    f"Delivered {msg.value().decode('utf-8')} \n"
                    f"to {msg.topic()} : partition {msg.partition()} : offset {msg.offset()}"
            )

        value = json.dumps(event).encode("utf-8")

        self.producer.produce(topic=self.topic, value=value, callback=delivery_report)

        self.producer.poll(0)


    def flush(self):
        self.producer.flush()