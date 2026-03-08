from confluent_kafka import Consumer
import json

class KafkaConsumer():
    def __init__(self,logger,topic,group,bootstrap_servers):
        self.logger = logger
        self.topic = topic
        self.group = group
        self.bootstrap_servers = bootstrap_servers
        self.consumer = None

        self._get_consumer()
        self.logger.info("KafkaConsumer - created")

    def _get_consumer(self):
        try:
            config = {"bootstrap.servers":self.bootstrap_servers,"group.id":self.group,"auto.offset.reset": "earliest"}
            consumer = Consumer(config)
            consumer.subscribe([self.topic])

            self.consumer = consumer
            self.logger.info("KafkaConsumer - connected")
        except Exception as e:
            raise e
    
    def run(self,callback):
        counter = 0
        while True:
            msg = self.consumer.poll(1.0)

            if not msg:
                if counter % 5 ==0:
                    self.logger.debug("KafkaConsumer - no data")
                counter +=1
                continue
            if msg.error():
                self.logger.error(f"KafkaConsumer - {msg.error()}")
                continue

            val = msg.value().decode("utf-8")
            
            data = json.loads(val)

            self.logger.debug(f"KafkaConsumer - data loaded soccessfuly")

            callback(data)


