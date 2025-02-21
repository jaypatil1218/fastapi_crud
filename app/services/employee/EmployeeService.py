from typing import List, Optional
from fastapi import Depends
from app.models.employee.EmployeeModel import Employee
from app.repositories.employee.EmployeeRepository import EmployeeRpository
from app.schemas.employee.EmployeeSchema import EmployeeRequestSchema
import uuid

class EmployeeService:
    employeeRepository: EmployeeRpository

    def __init__(self, employeeRepository: EmployeeRpository = Depends()) -> None:
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


 