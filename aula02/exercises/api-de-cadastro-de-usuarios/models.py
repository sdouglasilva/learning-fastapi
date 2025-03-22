from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    nome: str
    email: EmailStr
    password:str
    fl_active : bool = True
    created_at: datetime = datetime.now(timezone.utc)

    