from django.db import models

from sklearn.preprocessing import StandardScaler
import joblib

class IrisModel:
    def __init__(self):
        self.model = joblib.load('iris_model.joblib')
        self.scaler = StandardScaler()

    def predict(self, sepal_length, sepal_width, petal_length, petal_width):
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        input_data_scaled = self.scaler.transform(input_data)
        prediction = self.model.predict(input_data_scaled)[0]
        return prediction

