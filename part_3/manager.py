
class Manager():
    def __init__(self,logger,mongo_service,elastice_service,voice_extractor,consumer,producer):
        self.logger = logger
        self.mongo = mongo_service
        self.elastic = elastice_service
        self.voice_ex = voice_extractor
        self.consumer = consumer
        self.producer = producer
        self.logger.info("Manager created")


    def callback(self,event):
        id = event["id"]
        doc = self.elastic.get_doc(id)

        self.logger.debug(f"Manager - proccessing doc:{id}")
        b_file = self.mongo.get_file(file_id = id)
        if b_file:
            text = self.voice_ex.extract_text(file=b_file)
            doc["extracted_txt"] = text
            self.elastic.update_doc(id=id,doc=doc)
            self.producer.produce(data={"id":id})
            self.logger.debug(f"Manager - proccess succseed doc:{id}")

    def run(self):
        
        self.consumer.run(self.callback)

            