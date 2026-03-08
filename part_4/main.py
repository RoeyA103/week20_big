from elastic_service import ElasticService
from word_list import Decoder
from manager import Manager
from logger import Logger
from config import Config
from consumer import KafkaConsumer
from statistic import Statistic


def main():
    config = Config()

    logger = Logger.get_logger(
        name="part 4",
        es_host=config.ELASTIC_URI,
        index="loggs"
    )

 
    elastic = ElasticService(
        es_uri=config.ELASTIC_URI,
        index_name=config.ELASTIC_INDEX,
        logger=logger
    )

    decoder = Decoder()

    consumer = KafkaConsumer(logger=logger,
                             topic=config.KAFKA_TOPIC,
                             group=config.KAFKA_GROUP_ID
                             ,bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS)
    
    statistic = Statistic(logger=logger,
                          hostile_list=decoder.hotile_list
                          ,semi_hostile_list=decoder.semi_hostile_list)

    manager = Manager(
        elastice_service=elastic,
        statistic=statistic,
        logger=logger,
        consumer=consumer
    )


    manager.run()


if __name__ == "__main__":
    main()