

from pydentic import BaseModel,Feild,strictInt
from typing import Optional
class Employees(BaseModel):
    id:int =Feild(...,gt=0,title='Emp ID')
    name:str =Feild(...,min_length=3,max_length=50)
    department:str =Feild(...,min_length=3,max_length=50)
    age:Optional[int] =Feild(default=None)
    

