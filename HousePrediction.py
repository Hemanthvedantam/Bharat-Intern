# -*- coding: utf-8 -*-
"""Untitled61.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zpdaqb00vERC6yjlQLGH2D0Rz7FNbfSY
"""

#House Prediction Model using Sklearn Library

import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from google.colab import files
uploded=files.upload()

data=pd.read_csv('train.csv')
#importing the csv file of house data from kaggle
print(data.head())
data.dropna(inplace=True)
ct = ColumnTransformer([("ADDRESS", OneHotEncoder(), ["ADDRESS"])], remainder="passthrough")
#the column transformer will convert the addresss -String column to integer using the HotEncoder
X = ct.fit_transform(data.drop(columns=['SQUARE_FT']))
y=data['TARGET'].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5,random_state=0)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
#mse and r2 the problem metrics to find the accuracy and underfitting or overfitting
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
plt.plot(y_test,y_pred)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.show()
