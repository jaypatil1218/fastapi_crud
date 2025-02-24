from typing import List, Optional
import uuid
from fastapi import Depends
from sqlalchemy.orm import Session
from app.configs.Database import get_db_connection
from app.models.employee.EmployeeModel import Employee
from app.repositories.BaseRepository import (
    BaseRepository,
)


class EmployeeRepository(BaseRepository[Employee, uuid.UUID]):  
    def __init__(self, db: Session = Depends(get_db_connection)):
        super().__init__(db, Employee)  


    def authenticate_user(self, username: str, password: str):
        employee = self.db.query(Employee).filter(Employee.username == username, Employee.password == password).first()
    
        #if employee and utils.verify_password(password, user.hashed_password):
        return employee  
 
        
    # def list(
    #     self, name: Optional[str] = None, limit: int = 100, start: int = 0
    # ) -> List[Employee]:
    #     query = self.db.query(self.model_class)
    #     if name:  # ✅ Apply filter if name is provided
    #         query = query.filter(self.model_class.name.ilike(f"%{name}%"))
    #     return query.offset(start).limit(limit).all()
