from pathlib import Path
from models import MetaData



class MetadataExtractor():
    def __init__(self,logger):
        self.logger = logger
    
    def extract_metadata(self,f:Path):
        try:
            metadata = MetaData(name = f.name,
                                ctime = f.stat().st_ctime,
                                size_b = f.stat().st_size,
                                full_path=str(f.absolute()))
            
            
            self.logger.debug(f"MetadataExtractor - {f.name} metadata created")
            return metadata
        
        except FileNotFoundError:
            self.logger.error(f"MetadataExtractor - Error: The file {f} was not found.")
        except Exception as e:
            self.logger.error(f"MetadataExtractor - An error occurred: {e}")

    def handle_dir(self, path):
        for file in Path(path).iterdir():
            if file.is_file():
                yield self.extract_metadata(file)

       






