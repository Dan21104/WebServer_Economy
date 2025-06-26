from pydantic import BaseModel

class Entry(BaseModel):
    amount: float
    location: str
