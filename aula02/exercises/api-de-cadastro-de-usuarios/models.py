from pydantic import BaseModel, EmailStr
from datetime import datetime, timezone

class User(BaseModel):
    nome: str
    email: EmailStr
    password:str
    fl_active : bool = True
    created_at: datetime = datetime.now(timezone.utc)

    