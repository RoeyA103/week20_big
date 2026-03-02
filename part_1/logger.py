import logging
from datetime import datetime
from elasticsearch import Elasticsearch


class Logger:
    _logger = None

    @classmethod
    def get_logger(
        cls,
        name="your_logger_name",
        es_host="your_es_host_name",
        index="your_index_logs_name",
        level=logging.DEBUG
    ):
        if cls._logger:
            return cls._logger

        logger = logging.getLogger(name)
        logger.setLevel(level)

        if not logger.handlers:
            es = Elasticsearch(es_host)

            class ESHandler(logging.Handler):
                def emit(self, record):
                    try:
                        es.index(
                            index=index,
                            document={
                                "timestamp": datetime.utcnow().isoformat(),
                                "level": record.levelname,
                                "logger": record.name,
                                "message": record.getMessage(),
                            },
                        )
                    except Exception as e:
                        print(f"ES log failed: {e}")

            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            ch.setFormatter(formatter)

            logger.addHandler(ESHandler())
            logger.addHandler(ch)

        cls._logger = logger
        return logger


