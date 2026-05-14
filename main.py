from fastapi import FastAPI,Path 
import json


app =FastAPI()


def load_data():
     with open("patients.json","r") as file:
         data =json.load(file)
     return data

@app.get("/")
def hello_world():
    return {"message": "Patient management system api"}


@app.get("/about")
def about():
    return {"message":"A fully function api to manage your pateint records"}


@app.get("/view")
def view():
    data=load_data()
    
    return data



@app.get('/patient/{patient_id}')
def get_patient(patient_id:str):
    #load data from json file
    data=load_data()
    for patient in data['patients']:
        if patient['patient_id'] == patient_id:
            return patient
    return {"message": "Patient not found"}











