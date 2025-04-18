# -*- coding: utf-8 -*-
"""my_first_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a7XVhUp0bpVhU2VwawY9lcQHZMSTq5uF

### **`my first ML model`**
"""

import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv")
df

y=df['logS']
y

"""# New section

##data splitting
"""

x=df.drop('logS', axis=1)
x

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=100)
x_test

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train, y_train)

y_lr_train_pred=lr.predict(x_train)
y_lr_test_pred=lr.predict(x_test)

y_lr_train_pred

y_lr_test_pred

y_train

"""###evaluate model performance###"""

from sklearn.metrics import mean_squared_error, r2_score
lr_train_mse=mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2=r2_score(y_train, y_lr_train_pred)
lr_test_mse=mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2=r2_score(y_test, y_lr_test_pred)

print('LR MSE (Train):', lr_train_mse)
print('LR R2 (Train):', lr_train_r2)
print('LR MSE (Test):', lr_test_mse)
print('LR R2 (Test):', lr_test_r2)

lr_results=pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()

lr_results

lr_results.columns=['Model', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
lr_results

"""##**random forest**

##**training the model**
"""

from sklearn.ensemble import RandomForestRegressor
rf=RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(x_train,y_train)

"""##**applying the model to make a prediction**"""

y_rf_train_pred=rf.predict(x_train)
y_rf_test_pred=rf.predict(x_test)

"""##**evaluate model performance**"""

from sklearn.metrics import mean_squared_error, r2_score
rf_train_mse=mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2=r2_score(y_train, y_rf_train_pred)
rf_test_mse=mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2=r2_score(y_test, y_rf_test_pred)

rf_results=pd.DataFrame(['random forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns=['Model', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
rf_results

"""##**model comparison**"""

df_models=pd.concat([lr_results, rf_results], axis=0)
df_models

df_models.reset_index(drop=True)

"""##**data visualization of prediction results**"""

import matplotlib.pyplot as plt
plt.scatter(x=y_train, y=y_lr_train_pred, c='red', alpha=0.4)
plt.plot()