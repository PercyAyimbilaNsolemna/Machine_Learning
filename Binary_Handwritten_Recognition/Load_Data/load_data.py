
## Defines a function that loads the handwritten data into the jupyter notebook

import numpy as np

def load_data():
    X = np.load('../Data/X.npy')
    y = np.load('../Data/y.npy')
    X = X[0:1000]
    y = y[0:1000]
    return X, y