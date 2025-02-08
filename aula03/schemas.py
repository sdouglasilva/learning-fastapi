from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime, timezone

class UserIn(BaseModel):
    name:str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: UUID
    name:str
    email:str
    fl_active:bool
    created_at: datetime = datetime.now(timezone.utc)