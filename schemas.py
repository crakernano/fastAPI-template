from datetime import date
from pydantic import BaseModel


class mySchema(BaseModel):
    id: int

    class Config:
        orm_mode = True
