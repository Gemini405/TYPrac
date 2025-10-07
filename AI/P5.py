import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def importData():
  balance_data = pd.read_csv("P5-balance-scale.data")
  print(f"Dataset length: {len(balance_data)}")
  print(f"Dataset: {balance_data.head()}")
  return balance_data

def split_data_set(balance_data):
  X = balance_data.values[:, 1:5]
  Y = balance_data.values[:, 0]

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=100)
  return X, Y, X_train, X_test, Y_train, Y_test

def train_using_entropy(X_train, X_test, Y_train, Y_test):
  clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)

  clf_entropy.fit(X_train, Y_train)
  return clf_entropy

def prediction(X_test, clf_object):
  Y_pred = clf_object.predict(X_test)
  print(f"Predicted Values: {Y_pred}")
  return Y_pred

def cal_accuracy(Y_test, Y_pred):
  print(f"Accuracy: {accuracy_score(Y_test, Y_pred) * 100}")

def main():
  data = importData()
  X, Y, X_train, X_test, Y_train, Y_test = split_data_set(data)

  clf_entropy = train_using_entropy(X_train, X_test, Y_train, Y_test)

  print("Results using entropy: ")
  Y_pred_entropy = prediction(X_test, clf_entropy)
  cal_accuracy(Y_test, Y_pred_entropy)

main()
