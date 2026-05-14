


from fastapi import FastApi,HTTPException

from models import Employees
from typing import List
employees_db:List[Employees] =[]

app =FastApi()

#1.Read all employees

@app.get('/employees',response_model=List[Employees])
def get_employees():
    return employees_db 


#2 Read specific employees

@app.get('/employees/{emp_id}',response_model=Employees)
def get_employee(emp_id:int):
    #in this we have list of employee but inside the list we are storing 
    # dict->many info of employee then how will we iterate and return
    
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404,detail='Employee Not Found')
        
#add and employee

@app.post('/employee')
def add_employee(new_emp:Employees):
    for employee in employeed_db:
        if employee.id ==new_emp.id:
            raise HTTPException(statis_code=404,detail='Employee already present')
    employees_db.append(new_emp)
    return new_emp

#4 update an employee
@app.put('/update_employee/{emp_id}')
def update_employee(emp_id:int,updated_employee:Employees):
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            employees_db[index]=updated_employee
            return updated_employee
    raise HTTPException(status_code=404,detail='Employee not Found')

#Delete employee    
@app.delete('/delete_employee/{emp_id}')
def update_employee(emp_id:int):
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            del employees_db[index]
            return  {'message':"Employee delted successfully"}
    raise HTTPException(status_code=404,detail='Employee not Found')

