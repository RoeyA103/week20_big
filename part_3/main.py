from elastic_service import ElasticService
from mongo_service import MongoService
from voice_extrac_service import VoiceExtractor
from manager import Manager
from logger import Logger
from config import Config


def main():
    config = Config()

    logger = Logger.get_logger(
        name="part 3",
        es_host=config.ELASTIC_URI,
        index="loggs"
    )

 
    elastic = ElasticService(
        es_uri=config.ELASTIC_URI,
        index_name=config.ELASTIC_INDEX,
        logger=logger
    )

    mongo = MongoService(
        mongo_uri=config.MONGO_URI,
        mongo_db=config.MONGO_DB_NAME,
        logger=logger
    )

    voice_ex = VoiceExtractor(logger=logger)


    manager = Manager(
        elastice_service=elastic,
        mongo_service=mongo,
        voice_extractor=voice_ex,
        logger=logger
    )


    manager.run()


if __name__ == "__main__":
    main()