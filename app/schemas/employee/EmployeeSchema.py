from pydantic import BaseModel
import uuid


class EmployeeRequestSchema(BaseModel):
    username: str
    firstname: str
    lastname: str
    company_name: str
    position: str

# Employee schema with UUID as the type for id
class EmployeeSchema(EmployeeRequestSchema):
    id: uuid.UUID
