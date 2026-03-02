from pydantic import BaseModel , model_validator
import hashlib

class MetaData(BaseModel):
    id: str | None = None
    name: str
    ctime: float
    size_b: int
    full_path:str | None = None

    @model_validator(mode="after")
    def generate_id(self):
        raw_string = f"{self.full_path}-{self.ctime}-{self.size_b}"
        self.id = hashlib.sha256(raw_string.encode()).hexdigest()
        return self

