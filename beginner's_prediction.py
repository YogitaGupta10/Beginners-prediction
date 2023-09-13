# -*- coding: utf-8 -*-
"""Beginner's Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vhkRl1hRaSpGjijMVhdAVqVaWUzviUFP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('/content/train.csv')

df.head()

df.columns

df.dtypes

df.info()

df.describe()

df.isnull().sum()

sns.heatmap(df.corr())

cr= df.corr()
cr_df= cr['gpa'].sort_values(ascending= False)
cr_df

"""DATA CLEANING."""

plt.xticks(rotation=45)
sns.boxplot(data=df, x="state_of_origin", y='gpa')

plt.xticks(rotation=90)
sns.boxplot(data=df, x="hobby", y='gpa')

df.groupby('ethnicity').count()['ID'].plot(kind='bar')
plt.show();

df.groupby('parental_education_level').count()['ID'].plot(kind='bar')
plt.show();

df['parental_education_level'].unique()

df['parental_education_level'] = df['parental_education_level'].apply(lambda x: x.strip())

df['parental_education_level'].unique()

df.groupby('parental_education_level').count()['ID'].plot(kind='bar')
plt.show();

df.groupby('gender').count()['ID'].plot(kind='bar')
plt.show();

df['gender'].unique()

df['gender'] = df['gender'].apply(lambda x: x.strip())

df.groupby('gender').count()['ID'].plot(kind='bar')
plt.show();

# df['gender']= df['gender'].apply(lambda x: 'Female' if 'F'else
#                                       None)

df['gender'] = df['gender'].replace({'F': 'Female'})
df['gender'] = df['gender'].replace({'male': 'Male'})

df.groupby('gender').count()['ID'].plot(kind='bar')
plt.show();

df.groupby('religion').count()['ID'].plot(kind='bar')
plt.show();

df['religion'].unique()

df['religion'] = df['religion'].apply(lambda x: x.strip())

df.groupby('religion').count()['ID'].plot(kind='bar')
plt.show();

df.columns

df.dtypes

df['state_of_origin'].unique()

df['state_of_origin'] = df['state_of_origin'].apply(lambda x: x.strip())

df['school_type'].unique()

df['school_type'] = df['school_type'].apply(lambda x: x.strip())

df['extracurricular_activity'].unique()

df['extracurricular_activity'] = df['extracurricular_activity'].apply(lambda x: x.strip())

df['learning_disability'].unique()

df['learning_disability'] = df['learning_disability'].apply(lambda x: x.strip())

df['school_location'].unique()

df['school_location'] = df['school_location'].apply(lambda x: x.strip())

df['tutoring_mentoring_program'].unique()

df['tutoring_mentoring_program'] = df['tutoring_mentoring_program'].apply(lambda x: x.strip())

cols = df.columns
for col in cols:
  print(col)

  print(df[col].unique())
  print('------------------')

df['parental_involvement_level'] = df['parental_involvement_level'].apply(lambda x: x.strip())
df['bullying_experience'] = df['bullying_experience'].apply(lambda x: x.strip())
df['peer_interaction_level'] = df['peer_interaction_level'].apply(lambda x: x.strip())
df['ethnicity'] = df['ethnicity'].apply(lambda x: x.strip())
df['hobby'] = df['hobby'].apply(lambda x: x.strip())

cols = df.columns
for col in cols:
  print(col)

  print(df[col].unique())
  print('------------------')

df['hobby'].unique()

df['hobby'] = df['hobby'].replace({'Playing the guitar': 'Playing guitar'})

df['hobby'].unique()

df['age'].unique()

df.groupby('age').count()['ID'].plot(kind='bar')
plt.show();

b = np.where(df['age']== -2)
print(b)

c = np.where(df['age']== 0)
print(c)

df = df[df.age != 0]

df = df[df.age != -2]

df.groupby('age').count()['ID'].plot(kind='bar')
plt.show();

"""EDA"""

df.head()

gender_map = {'Male': 0,'Female': 1}
df['gender']= df['gender'].map(gender_map)

religion_map = {'Islam': 0,'Christianity': 1}
df['religion']= df['religion'].map(religion_map)

school_map = {'Government': 0,'Public': 1, 'Private':2}
df['school_type']= df['school_type'].map(school_map)

pel_map = {'Secondary': 0,'Tertiary': 1}
df['parental_education_level']= df['parental_education_level'].map(pel_map)

act_map = {'No': 0,'Yes': 1}
df['extracurricular_activity']= df['extracurricular_activity'].map(act_map)

ld_map = {'No': 0,'Yes': 1}
df['learning_disability']= df['learning_disability'].map(ld_map)

tmp_map = {'No': 0,'Yes': 1}
df['tutoring_mentoring_program']= df['tutoring_mentoring_program'].map(tmp_map)

be_map = {'No': 0,'Yes': 1}
df['bullying_experience']= df['bullying_experience'].map(ld_map)

pil_map = {'Low': 0,'Medium': 1, 'High':2}
df['parental_involvement_level']= df['parental_involvement_level'].map(pil_map)

sl_map = {'Rural': 0,'Suburban': 1, 'Urban':2}
df['school_location']= df['school_location'].map(sl_map)

pinl_map = {'Low': 0,'Medium': 1, 'High':2}
df['peer_interaction_level']= df['peer_interaction_level'].map(pinl_map)

# df.head()

df= pd.get_dummies(data= df, columns= ['ethnicity'], drop_first= True)

df= pd.get_dummies(data= df, columns= ['state_of_origin'], drop_first= True)

df= pd.get_dummies(data= df, columns= ['hobby'], drop_first= True)

df.head()

df.columns

df.isnull().sum()

cols = df.columns
for col in cols:
  print(col)

  print(df[col].unique())
  print('------------------')

df= df.drop(['name','ID'], axis=1)

sns.scatterplot(data=df, x="attendance_percentage", y='gpa')

sns.scatterplot(data=df, x="exam_maths", y='gpa')

sns.scatterplot(data=df, x="exam_english", y='gpa')

sns.scatterplot(data=df, x="exam_social_science", y='gpa')

# target = df.pop('gpa')

# sns.displot(target, kde=True)

# df['ID'] = pd.to_numeric(df['ID'],errors = 'coerce')
# df["ID"] = df.ID.astype(float)

df=df.dropna()



"""MODEL"""

from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import explained_variance_score,mean_absolute_error,r2_score

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X= df.drop(['gpa'], axis=1)
y = df.gpa

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)

# lr = LogisticRegression()
# lr.fit(X_train, y_train)

rf= RandomForestRegressor()
rf.fit(X_train, y_train)

y_pred2= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred2)
r2_square = r2_score(y_test,y_pred2)
rms = np.sqrt(mean_squared_error(y_test, y_pred2))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

dt= DecisionTreeRegressor(max_depth=8)
dt.fit(X_train, y_train)

y_pred3= rf.predict(X_test)

mse = mean_squared_error(y_test, y_pred3)
r2_square = r2_score(y_test,y_pred3)
rms = np.sqrt(mean_squared_error(y_test, y_pred3))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

from sklearn.ensemble import HistGradientBoostingRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.svm import SVR
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

xgb=XGBRegressor()
xgb.fit(X_train, y_train)

y_pred4=xgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred4)
r2_square = r2_score(y_test,y_pred4)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

lgb= LGBMRegressor()
lgb.fit(X_train, y_train)

y_pred5=lgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred5)
r2_square = r2_score(y_test,y_pred5)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

gb= GradientBoostingRegressor()
gb.fit(X_train,y_train)

y_pred6=gb.predict(X_test)

mse = mean_squared_error(y_test, y_pred6)
r2_square = r2_score(y_test,y_pred6)
rms = np.sqrt(mean_squared_error(y_test, y_pred6))
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rms}')

hgb= HistGradientBoostingRegressor()
hgb.fit(X_train,y_train)

y_pred7=hgb.predict(X_test)

mse = mean_squared_error(y_test, y_pred7)
r2_square = r2_score(y_test,y_pred7)
print(f" R-squared: {r2_square}")
print(f'Mean Squared Error: {mse}')

