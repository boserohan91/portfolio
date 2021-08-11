from pydantic import BaseModel
from sqlalchemy.sql.sqltypes import Date

class BasicDetails(BaseModel):
    name: str
    address: str
    telephone: str
    email: str
    gender: str
    dob: Date
    nationality: str

class User(BaseModel):
    id: int
    name: str