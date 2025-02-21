from typing import List, Optional
from fastapi import APIRouter, Depends, status
import uuid
from app.schemas.employee.EmployeeSchema import EmployeeRequestSchema, EmployeeSchema
from app.configs import constants

from app.services.employee.EmployeeService import EmployeeService

EmployeeRouter = APIRouter(prefix="/v1/employee", tags=["employee"])



@EmployeeRouter.get("/", response_model=List[EmployeeSchema])
def index(
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    employeeService: EmployeeService = Depends(),
):
    return employeeService.list(pageSize=pageSize, startIndex=startIndex)


@EmployeeRouter.get("/{id}", response_model=EmployeeSchema)
def get(id: uuid.UUID, employeeService: EmployeeService = Depends()):
    return employeeService.get(id)


@EmployeeRouter.post(
    "/",
    response_model=EmployeeSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    employee: EmployeeRequestSchema,
    employeeService: EmployeeService = Depends(),
):
    return employeeService.create(employee)


@EmployeeRouter.patch("/{id}", response_model=EmployeeSchema)
def update(
    id: uuid.UUID,
    employee: EmployeeRequestSchema,
    employeeService: EmployeeService = Depends(),
):
    return employeeService.update(id, employee)


@EmployeeRouter.delete("/{id}", response_model=dict)
def delete(id: uuid.UUID, employeeService: EmployeeService = Depends()):
    employeeService.delete(id)
    return {"message": constants.DATA_DELETED}
