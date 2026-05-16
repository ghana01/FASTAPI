from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer

app =FastAPI()


oauth2_schema =OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
def login(username:str=Form(...), password:str=Form(...)):
    if username=='ghan' and password=='12345':
        return {'access_token':'valid_token','token_type':'beared'}
    raise HTTPException(status_code=401
                         ,detail='Invalid credential')


def decode_token(token:str):
    if token=='valid_token':
        return {'name':'ghan'}
    raise HTTPException(status_code=400 ,detail='Invalid Token') 



def get_current_user(token:str =Depends(oauth2_schema)):
    return decode_token(token)
    



@app.get('/profile')
def get_profile(user=Depends(get_current_user)):
    return {'username':user['name']}

