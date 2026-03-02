from metadata_extractor import MetadataExtractor
from config import Config
from logger import Logger
from producer import KafkaPublisher



def main():
    config = Config()
    logger = Logger.get_logger(name="part 1",
                    es_host=config.ELASTIC_URI,
                    index="loggs")
    metadata_extractor = MetadataExtractor(logger)
    producer = KafkaPublisher(logger=logger,
                              bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
                              topic=config.KAFKA_TOPIC)

    count = 0

    try:
        for obj in metadata_extractor.handle_dir(config.DATA_PATH):
            producer.publish(obj.model_dump())
            count += 1
    finally:
        producer.flush()

    logger.logger.info(f"main - sent {count} messages successfully to kafka")

if __name__ == "__main__":
    main()

