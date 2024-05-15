import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def strength_prediction(cement,blast_furnace_slag,fly_ass,water,super_plastilizer,coarse_aggregate,fine_aggregate,age):
    X = pd.read_csv('features.csv')
    y = pd.read_csv('target.csv')

    X = X.values
    y = y.values

    X_test = np.array([cement, blast_furnace_slag, fly_ass, water, super_plastilizer, coarse_aggregate, fine_aggregate, age]).reshape(1, -1)
   
    model = LinearRegression()
    model.fit(X,y)

    return model.predict(X_test)

