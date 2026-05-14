import models,schemas,crud
from fastapi import FastAPI,HTTPException,Depends

from sqlalchemy.orm import Session
from database import engine,SessionLocal,Base
from typing import List



Base.metadata.create_all(bind=engine)

app=FastApi()


#dependecy with Db

def get_db():
    db =SessionaLocal()
    try:
        yeild db
    finally:
        db.close()
        
#endpoint

#1.create an employee

@app.post('/employees',response_model=schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate,db:Session=Depends(get_db)):
    return crud.create_employee(db,employee)



#get all employee
@app.get('/emlpoyees',response_model=List[schemas.EmployeeOut])
def get_employess(db:Session=Depends(get_db)):
    return crud.get_employees(db)



#3.get specific employee
@app.get('/employess/{emp_id}',response_model=schemas.EmployeeOut)
def get_employee(emp_id:int ,db:Session=Depeends(get_db)):
    employee =crud.get_employee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404,detail='employee not found')
    return employee


#update an employee 
@app.put('/employee/{emp_id}',response_model =schemas.EmployeeOut)
def update_employee(emp_id:int,employee:schemas.EmployeeUpdate,db:Session=Depends(get_db)):
    db_employee=crud.update_employee(db,emp_id,employee)
    if db_employee is None:
        raise HTTPException(status_code=404,detail='employee not found')
    return db_employee



#5 delete and employee
@app.delete('/employee/{emp_id}',response_model =dict)
def delete_employee(emp_id:int,db:Session=Depends(get_db)):
    employee=crud.delete_employee(db,emp_id)
    
    if employee is None:
        raise HTTPException(status_code=404,detail='employee not found')
    
    return {'detail':'Employee Deleted'}
        
        
        
        
        
        
        
        
        