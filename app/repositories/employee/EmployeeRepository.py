from typing import List, Optional
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from app.security.utils import verify_password
from app.configs.Database import get_db_connection
from app.models.employee.EmployeeModel import Employee
from app.repositories.BaseRepository import (
    BaseRepository,
)


class EmployeeRepository(BaseRepository[Employee, uuid.UUID]):  
    def __init__(self, db: Session = Depends(get_db_connection)):
        super().__init__(db, Employee)  


 
 

    def authenticate_user(self, username: str, password: str):
        employee = self.db.query(Employee).filter(Employee.username == username).first()

        if not employee:
            return None  

        if not verify_password(password, employee.password):
            return None  
        return employee 
  
