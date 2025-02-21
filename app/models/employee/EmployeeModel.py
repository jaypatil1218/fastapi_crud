from sqlalchemy import (
    Column,
    String,
)

from app.models.BaseModel import BaseModel


class Employee(BaseModel):
    __tablename__ = "employees"

    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False) 
    company_name = Column(String, nullable=False)
    position = Column(String, nullable=True)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "first_name": self.firstname.__str__(),
            
        }
