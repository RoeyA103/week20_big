from pymongo import MongoClient
from gridfs import GridFS

class MongoService():
    def __init__(self,mongo_uri,mongo_db,logger):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.logger = logger
        self.fs = self._get_gfs()

        self.logger.info("MongoService - created")

    def _get_gfs(self):
        try :
            client = MongoClient(self.mongo_uri)
            db = client[self.mongo_db]
            fs = GridFS(database=db)

            self.logger.info("MongoService - fs connected")
            return fs
        except Exception as e:
            self.logger.error(f"MongoService - could not connect to fs/mongo : {e}")
    
    def get_file(self,file_id):
        try:
            file = self.fs.find_one({"file_id": file_id})

            if file:
                self.logger.debug(f"MongoService - file loded : {file_id}")

                return file
            else:
                self.logger.debug(f"MongoService - file not found: {file_id}")
                return None
        except Exception as e:
            self.logger.error(f"MongoService - could not find the file : {e}")