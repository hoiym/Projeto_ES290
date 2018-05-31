import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.multioutput import MultiOutputRegressor

# >>> Commands for avss' machine
# sudo apt-get install python3-pip
# python3 -m pip install --user scikit-learn

data = pd.read_csv('dados/medicoes.csv')
test = pd.read_csv('dados/testLoc.csv')

# Dividing data from labels to be predicted
train_labels = data.iloc[:, 0:2]
train_data = data.iloc[:, 2:]

test_labels = test.iloc[:, 0:2]
test_data = test.iloc[:, 2:]

# Defining parameters for the SVM classifier
# TODO: use grid search to find best parameters
svm_reg = svm.SVR(C=10000.0, epsilon=0.0000005)

pred_labels = MultiOutputRegressor(svm_reg).fit(train_data, train_labels).predict(test_data)

print(pred_labels)
