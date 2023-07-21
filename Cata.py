#here we will try to encode the categorical variables present in the data.csv
#into numbers


#importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#inserting the dataset
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :-1]
Y = dataset.iloc[: 3].values

#taking care of the missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis= 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#encoding the category data
from sklearn.preprocessing import LabelEncoder

