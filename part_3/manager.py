
class Manager():
    def __init__(self,logger,mongo_service,elastice_service,voice_extractor):
        self.logger = logger
        self.mongo = mongo_service
        self.elastic = elastice_service
        self.voice_ex = voice_extractor

        self.logger.info("Manager created")

    def run(self):
        counter = 1
        docs = self.elastic.get_all_doc()

        for doc in docs:
            doc = doc['_source']
            if doc.get("extracted_txt",None):
                continue
            id = doc["id"]

            self.logger.debug(f"Manager - proccessing doc:{id},number:{counter}")
            b_file = self.mongo.get_file(file_id = id)
            if b_file:
                text = self.voice_ex.extract_text(file=b_file)
                doc["extracted_txt"] = text
                self.elastic.update_doc(id=id,doc=doc)
                self.logger.debug(f"Manager - proccess succseed doc:{id},number:{counter}")
            counter +=1

            