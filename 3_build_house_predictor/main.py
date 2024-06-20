#!usr/bin/python3

from sklearn import datasets # Load Datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data_house = datasets.fetch_california_housing()
X = data_house['data']
y = data_house['target']

# Partition into Train and test dataset
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.3)

clf = DecisionTreeRegressor() # Init model

clf.fit(train_x, train_y) # Train model

test_r2_score = clf.score(test_x, test_y) # Test model
# Output will be available in logs of SAP AI Core.

'''
Not the ideal way of storing /reporting metrics in SAP AI Core,
but that is not the focus this tutorial
'''

print(f"Test Data Score {test_r2_score}")
