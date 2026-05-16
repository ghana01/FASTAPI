from fastapi import FastAPi,Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

from auth import create_access_token,verify_token
from models import UserInDB
from utils import get_user,verify_password


app=FastAPI()



oauth2_scheme=OAuth2PasswordBearer(tokenUrl='token')


@app.post('/token')
def login(form_data:OAuth2PasswordRequestForm=Depends()):
    user_dict =get_user(form_data.username)
    if user_dict is None:
        raise HTTPException(status_code=400,detail='Invalid user')
    if not verify_password(form_data.password,user_dict['hashed_password']):
        raise HTTPException(400,detail='Invalid password')
    
    access_token =create_access_token(data={'sub':form_data.username})
    return {'access_token' :access_token , 'token_type':'bearer'}

@app.get('/user')
def read_user(token:str=Depends(oauth2_schema)):
    username=verify_token(token)
    return {'username':username}


