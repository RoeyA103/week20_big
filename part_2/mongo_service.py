from pymongo import MongoClient
from gridfs import GridFS
import io

class GFSSERVICE():
    def __init__(self,logger,mongo_uri:str,database_name:str):
        self.logger = logger
        self.mongo_uri = mongo_uri
        self.database_name = database_name

    def get_fs(self):
        """Establish connection to MongoDB and GridFS"""
        client = MongoClient(self.mongo_uri)
        db = client[self.database_name]
        fs = GridFS(db)
        self.logger.info(f"GridFSStorage - Connected to MongoDB database: {self.database_name}")

        return fs

    def save(self, file_bytes: bytes, filename: str, id: str):
        fs = self.get_fs()
        try:
            file_object_id = fs.put(
                file_bytes,
                filename=filename,
                metadata={"file_id": id}
            )

            self.logger.debug(f"GridFSStorage - gridfs_id: {str(file_object_id)} file_id: {id}")
            return file_object_id
        except Exception as e:
            self.logger.error("GridFSStorage - " + str(e))


    