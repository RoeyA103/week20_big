from event_handler import EventHandler
from config import Config
from logger import Logger
from consumer import KafkaConsumer
from mongo_service import GFSSERVICE
from models import MetaData
from elastic_service import ElasticsearchClient


def main():

    config = Config()
    logger = Logger.get_logger(name="part 2",
                    es_host=config.ELASTIC_URI,
                    index="loggs")

    mongo_fs = GFSSERVICE(logger=logger,
                          mongo_uri=config.MONGO_URI
                          ,database_name=config.MONGO_DB_NAME)
    
    consumer = KafkaConsumer(logger=logger,
                              bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVERS,
                              topic_name=config.KAFKA_TOPIC,
                              group_id =config.KAFKA_GROUP_ID)
    
    es_client = ElasticsearchClient(es_uri=config.ELASTIC_URI,
                                    index_name=config.ELASTIC_INDEX,
                                    logger=logger)
    
    event_handler = EventHandler(logger=logger,k_consumer=consumer,
                                 es_client=es_client,
                                 bs_model=MetaData,
                                 mongo_fs=mongo_fs)
    
    event_handler.run()


if __name__ == "__main__":
    main()

