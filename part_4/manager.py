
class Manager():
    def __init__(self,logger,elastice_service,consumer,statistic):
        self.logger = logger
        self.elastic = elastice_service
        self.consumer = consumer
        self.statistic = statistic
        self.logger.info("Manager created")


    def callback(self,event):
        id = event["id"]
        doc = self.elastic.get_doc(id)

        self.logger.debug(f"Manager - proccessing doc:{id}")
        statistics = self.statistic.calculate_hate_percent(text=doc["extracted_txt"])
        updeted_doc = doc | statistics
        self.elastic.update_doc(doc_id=id,doc=updeted_doc)
        self.logger.debug(f"Manager - proccess succseed doc:{id}")

    def run(self):
        
        self.consumer.run(self.callback)

            