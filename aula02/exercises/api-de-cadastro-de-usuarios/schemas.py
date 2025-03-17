from pydantic import BaseModel, EmailStr, Field
from datetime import datetime,timezone
from uuid import UUID, uuid4

class MessageOut(BaseModel):
    message:str

class UserIn(BaseModel):
    nome:str
    email:EmailStr
    password:str
    

class UserOut(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome:str
    email:str
    fl_active: bool =  True
    created_at: datetime = datetime.now(timezone.utc)