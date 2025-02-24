from typing import List, Optional
from fastapi import Depends
from app.models.employee.EmployeeModel import Employee
from app.repositories.employee.EmployeeRepository import EmployeeRepository
from app.schemas.employee.EmployeeSchema import EmployeeRequestSchema, EmployeeSchema
import uuid

from passlib.context import CryptContext



class EmployeeService:
    employeeRepository: EmployeeRepository

    def __init__(self, employeeRepository: EmployeeRepository = Depends()) -> None:
        self.employeeRepository = employeeRepository

    def create(self, employee_body: EmployeeRequestSchema) -> Employee:

        emp_instance=Employee(
            **employee_body.model_dump()
        )
        return self.employeeRepository.create(instance=emp_instance)

    def delete(self, employee_id: uuid.UUID) -> None:
        return self.employeeRepository.delete(employee_id)

    def get(self, employee_id: uuid.UUID) -> Employee:
        return self.employeeRepository.get(employee_id)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Employee]:
        return self.employeeRepository.list( pageSize, startIndex)

    def update(self, employee_id: uuid.UUID, emp_body: EmployeeRequestSchema) -> Employee:
        return self.employeeRepository.update(employee_id, emp_body)
    
    def set_password(self, password: str):
        """Hashes the password before saving."""
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        """Verifies a plain password against the hashed password."""
        return pwd_context.verify(password, self.password_hash)

    def getbyUsenameAndPassword(self,username,password):
        employee=self.employeeRepository.authenticate_user(username=username,password=password)
        if employee is None:
            return None  # Or raise an exception if you want

        return EmployeeSchema(**employee.__dict__)  # Convert SQLAlchemy object to Pydantic model



 