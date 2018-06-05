import pandas as pd
import numpy as np
import math
from sklearn import svm
from sklearn.multioutput import MultiOutputRegressor

# >>> Commands for avss' machine
# sudo apt-get install python3-pip
# python3 -m pip install --user scikit-learn

data = pd.read_csv('dados/medicoes.csv')
test = pd.read_csv('dados/testLoc.csv')

# Search space where the best params will be chosen
c_values = [1.0, 10.0, 50.0, 100.0, 500.0, 1000.0,
			5000.0, 10000.0, 50000.0]
c_val_len = len(c_values)

eps_values = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005,
			  0.0001, 0.00005, 0.00001, 0.000005, 0.000001,
			  0.0000005, 0.0000001]
eps_val_len = len(eps_values)

# Dividing data from labels to be predicted
train_labels = data.iloc[:, 0:2]
train_data = data.iloc[:, 2:]

test_labels = test.iloc[:, 0:2]
test_data = test.iloc[:, 2:]

# Code commented below does grid search to find best C and epsilon for the SVM
# The best values found are set in the SVM to predict the labels for the test dataset
'''
test_len = len(test)

# Variables to be set according to the RMSEs to be calculated
min_rmse_sum = 1e10
c_idx = -1
eps_idx = -1

for i in range(c_val_len):
	for j in range(eps_val_len):
		svm_reg = svm.SVR(C=c_values[i], epsilon=eps_values[j])

		pred_labels = MultiOutputRegressor(svm_reg).fit(train_data, train_labels).predict(test_data)
		rmse_lat = 0.0
		rmse_long = 0.0
		
		for k in range(test_len):
			rmse_lat = rmse_lat + (pred_labels[k][0] - test_labels.iloc[k, 0])**2
			rmse_long = rmse_long + (pred_labels[k][1] - test_labels.iloc[k, 1])**2
			
		rmse_lat = math.sqrt(rmse_lat/test_len)
		rmse_long = math.sqrt(rmse_long/test_len)
		
		if(rmse_lat + rmse_long < min_rmse_sum):
			min_rmse_sum = rmse_lat + rmse_long
			c_idx = i
			eps_idx = j

print('Best C', c_values[c_idx])
print('Best EPS', eps_values[eps_idx])
'''

svm_reg = svm.SVR(C=1.0, epsilon=0.000001)
pred_labels = MultiOutputRegressor(svm_reg).fit(train_data, train_labels).predict(test_data)

print(pred_labels)
