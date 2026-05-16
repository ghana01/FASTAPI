from pydentic import BaseModel

class User(BaseModel):
    username:str
    password:str





class UserInDB(User):
    hashed_password=str