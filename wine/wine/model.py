import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

"""
MODEL MACHINE LEARNING
"""
path = "~/Documentos/flask/imasd/archive/winequality-red.csv"
wine = pd.read_csv(path, sep=",")

# DATA TO TRAIN AND TEST
target = "quality"
features = list(wine.columns)
features.remove(target)
x = wine[features]
y = wine[target]
x_train, x_test, y_train, y_test =  train_test_split(x, y)

# MODEL MACHINE LEARNING
model = RandomForestRegressor()
model.fit(x_train, y_train)
with open("rf_model.pickle", "wb") as file:
    pickle.dump(model, file)

print ("Model saved.")
