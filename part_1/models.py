from pydantic import BaseModel

class MetaData(BaseModel):
    name: str
    ctime: float
    size_b: int
    full_path:str = None
