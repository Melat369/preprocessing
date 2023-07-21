#importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#trying to take care of the missing data sets

from sklearn.preprocessing import Imputers


#creating Imputers object
imputer = Imputers(missing_values = 'NaN', strategy = 'mean', axis = 0)



#fitting the imputer object
imputer=imputer.fit(x[:, 1:3]) 
x[:, 1:3] = imputer.transform(x[:, 1:3])
