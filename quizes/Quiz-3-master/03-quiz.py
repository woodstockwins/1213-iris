#!/usr/bin/env python3

"""
Quiz 3

Task:
Your task for quiz 3 is to write a python script that:
- Imports the libraries you need
- Reads in the data: data/nba_rookies.csv
- Processes data:
    1. Set the 'Name' column as the index
    2. Converts the 'TARGET_5Yrs' column to 0/1 using 0 for 'No' and 1 for 'Yes'
- Models data using any classification algorithm you would like
    - If you do not know what to do here, feel free to fit a Logistic Regression model with default hyperparameters. But you are free to use any other model or 
      methods that you know if you think that would be better!
    - Use a random state of 42 when splitting your data into training and testing
    - Use ALL columns (except your target) as your X matrix
- Generates predictions on your test data
- Creates a new DataFrame that has:
    1. One column called 'predictions' which is the predictions from your model on your test data
    2. An index that is the name of the player associated with the prediction from your test data
- Writes the DataFrame with the predictions to a csv called 'predictions.csv' in the data folder in this repository

This script should be able to be run in your terminal: python 03-quiz.py


Fill in this .py file with your solutions. Comments of the above instructions are included to guide your workflow.
"""

#################################
# Your Info
# Please fill out the following questions:

# Your name: Gene Woodstock

# Your section: DSI-R 1213

# Your email: genewoodstock@gmail.com

#################################

# Import the libraries you need
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score

# Read in the data: data/nba_rookies.csv
data = pd.read_csv('./data/nba_rookies.csv')

# Process data:
# 1. Set the 'Name' column as the index
data.columns = data.columns.str.lower()
data.index = data['name']
data.drop(columns=['name'], inplace=True)

# 2. Convert the 'TARGET_5Yrs' column to 0/1 using 0 for 'No' and 1 for 'Yes'
data['target_5yrs'] = data['target_5yrs'].map({'No':0, 'Yes':1})

# Model data using any classification algorithm you would like
# If you do not know what to do here, feel free to fit a Logistic Regression model with default hyperparameters
# But you are free to use any other model or methods that you know if you think that would be better!
# Use a random state of 42 when splitting your data into training and testing
knn = KNeighborsClassifier(25)
ss = StandardScaler()

X = data.drop(columns=['target_5yrs'])
y = data['target_5yrs']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)
X_train_sc = ss.fit_transform(X_train)
X_test_sc = ss.transform(X_test)

knn.fit(X_train_sc, y_train)

# Generate predictions on your test data
# Create a new DataFrame for predictions
# 2. Have one column called 'predictions'
# which is the predictions from your model on your test data
# 1. Have an index that is the name of the player
y_preds = pd.DataFrame(knn.predict(X_test_sc), columns=['predictions'], index=y_test.index)

# Write the DataFrame you created to a csv called 'predictions.csv'
# in the data folder in this repository
y_preds.to_csv('./data/predictions.csv')
