import numpy as np

def predict_flower(trained_classifer, input_features):
    """
    predict iris type

    :param trained_classifer: sklearn estimator class
    :param input_features: numpy array like (4 numeric values)
    :return: numpy array of string dtype (the model's prediction)

    """
    return trained_classifer.predict(input_features.reshape(1, -1))