from fastapi import FastAPI


from schemas import InputSchema ,OutputSchema

from predict import make_prediction


app=FastAPI()



@app.get('/')
def index():
    return {'message':'welcome to the ml model prediction API'}


@app.post('/prediction',response_model=OutputSchema)
def predict(user_input:InputSchema):
    prediction =make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=prediction)
    
    
    