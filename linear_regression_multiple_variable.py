# age = m1 *overall + m2* potential + m3* gkr  + intercept
# coeficient m1,2,3 at line 25
import pandas as pd
import numpy as np
from sklearn import linear_model
df = pd.read_csv("FIFA19.csv")
df
median_Age=df.Age.median()
df.Age = df.Age.fillna(median_Age)
reg= linear_model.LinearRegression()
reg.fit(df[['Overall','Potential','GKReflexes']],df.Age)
reg.coef_
array([ 0.74266732, -0.74235788,  0.02000405])
reg.intercept_
reg.predict([[4,69,4]])
0.742*4+-0.7423*69+0.02*4+28.53
