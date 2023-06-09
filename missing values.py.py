# -*- coding: utf-8 -*-
"""week7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18PPwc6I6_JRdqWWzRDj39YTLd3PzXAzH
"""

import pandas as pd
import numpy as np

s1=pd.Series([2,3,np.nan,4,np.nan])

s1.isnull()



s1.dropna()

data = pd.DataFrame([[1.0,6.5,3.0],[1.0,np.nan,np.nan],[np.nan,np.nan,np.nan],[np.nan,6.5,3.0]])

data

""" # to remove all the rows which contains null values """

data.dropna(how ='all')

del data['null_col']

data[3]=([np.nan,np.nan,np.nan,np.nan])

data

data.dropna(axis=1,how = 'all')

"""# creating a data frame with 7rows and 3 columns"""

data1=pd.DataFrame(np.random.randn(7,3))
data1

data1.iloc[:4,1] = np.nan

data1.iloc[:2,2] = np.nan

data1

"""# delete a row if it does not contain a minimum of two non missing values"""

data1.dropna(thresh = 2)

"""# fill all the null values with 0"""

data1.fillna(0)

"""# fill all the null values at column index 1 with 50 and column index 2 with 100"""

data1.fillna({1:50,2:100})

"""# fill all the null values with forward value"""

data1.fillna(method = 'ffill')

"""# fill only two null values with forward values"""

data.fillna(method = 'ffill',limit = 1)

data

"""# to fill all the null values with mean value of a column"""

data.fillna(data.mean())

data.mean()

"""# create the following DataFrame containing 2 columns k1 and k2"""

data3 = pd.DataFrame({'k1':['one','two','one','two','one','two'],'k2':[1,1,2,3,3,4]})

data3

data3.drop_duplicates(['k1'])

data4 = pd.DataFrame({"name" :['alex','bob','alice','john'],'age':[20,30,25,40]})
def age_months(age):
  return age*12
data4['age_in_months'] = data4['age'].map(age_months)
data4

data5 = pd.DataFrame({"name" :['surya','star','arya','varun'],'age':[25,30,35,40]})
age_groups = {18:'18-24',25:'25-34',35:'35-44',45:'45+'}
data5['age_groups'] = data5['age'].map(age_groups)
data5

