from typing import List, Optional
from fastapi import APIRouter, Depends, status,HTTPException, Query
import uuid
from app.schemas.employee.EmployeeSchema import EmployeeRequestSchema, EmployeeSchema, TokenDecode,TokeEncode
from app.configs import constants
from app.security.utils import (create_token,decode_token)
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


@EmployeeRouter.post("/genarete_token",response_model=dict)
def getToken(tokenencode:TokeEncode,employeeService: EmployeeService = Depends()):
    employeeschema=employeeService.getbyUsenameAndPassword(tokenencode.username,tokenencode.password)
    if employeeschema is None:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    payload= employeeschema.model_dump()
    token=create_token(payload)
    return {"Access Token":token }


@EmployeeRouter.post("/decode", response_model=dict)
def getdata(token: TokenDecode):
    token_dict = token.model_dump()
    print("TokenDecode: ", token_dict)

    return decode_token(token_dict["token"])
