import joblib
import numpy as np


saved_model =joblib.load("model.joblib")
print("Loaded the model")


def make_prediction(data :dict) ->float :
    #user send json data we get the dict after that we need to convert them into numpy array 2d
    features =np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']

        ]
    ])
    
    
    return saved_model.predict(features)[0]


