from fastapi import FastAPI

from pydentic import BaseModel


class User(BaseModel):
    id:int
    name:str
    
    
app =FastApi()

@app.get('/user',response_model=User)
def get_user():
    return User(id=1,name='ghan')
