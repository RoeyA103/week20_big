
class EventHandler():
    def __init__(self,k_consumer, es_client, logger,bs_model,mongo_fs):
        self.k_consumer = k_consumer
        self.es_client = es_client
        self.bs_model = bs_model
        self.mongo_fs = mongo_fs
        self.logger = logger

        self.logger.info("EventHandler created successfuly")

    def handel_event(self,event):
        metadata = self.bs_model(**event)
        self.es_client.insert(doc= metadata.model_dump(),id= metadata.id)
        self.send_to_mongo(file_name=metadata.name,file_path=metadata.full_path,id = metadata.id)

        self.logger.debug(f"EventHandler - event: {event['name']} handel successfuly")

    def send_to_mongo(self,file_name:str,file_path:str,id:str):
        try:
            with open(file_path,"rb") as f:
                self.mongo_fs.save(file_bytes = f, filename = file_name , id=id)
        except Exception as e:
            self.logger.error(f"EventHandler - erorr in opening:{file_path}\n{e}")


    def run(self):
        self.logger.info("EventHandler - runing")
        self.k_consumer.run(self.handel_event)