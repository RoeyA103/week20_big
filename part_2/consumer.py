import json
from confluent_kafka import Consumer 

class KafkaConsumer():
    def __init__(self,bootstrap_servers, topic_name, group_id, logger):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic_name
        self.gruop_id = group_id
        self.logger = logger

        logger.info("KafkaConsumer - created successfully")



    def get_consumer(self):
        consumer_config = {
            "bootstrap.servers": self.bootstrap_servers,
            "group.id": self.gruop_id,
            "auto.offset.reset": "earliest"
        }

        consumer = Consumer(consumer_config)

        consumer.subscribe([self.topic])

        self.logger.debug(f"KafkaConsumer - 🟢 Consumer is running and subscribed to {self.topic} topic")  
        
        return consumer

    def run(self,callback):
        consumer = self.get_consumer()
        try:
            counter = 0
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    if counter % 5 == 0:
                        self.logger.debug("KafkaConsumer - no data")
                    counter +=1
                    continue
                if msg.error():
                    self.logger.error("KafkaConsumer - ❌ Error:", msg.error())
                    continue

                value = msg.value().decode("utf-8")

                data = json.loads(value)

                callback(data)

                self.logger.debug(f"KafkaConsumer - data loded from kafka 'name':{data['name']}")

                
        except KeyboardInterrupt:
            self.logger.info("KafkaConsumer - 🔴 Stopping consumer")

        finally:
            consumer.close()
