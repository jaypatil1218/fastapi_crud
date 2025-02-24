from pydantic import BaseModel, field_validator
import uuid
from app.security.utils import hash_password

class EmployeeRequestSchema(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str
    company_name: str
    position: str
    @field_validator("password", mode="before")
    @classmethod
    def hash_password(cls, value: str) -> str:
        return hash_password(value)


class EmployeeSchema(EmployeeRequestSchema):
    id: uuid.UUID
