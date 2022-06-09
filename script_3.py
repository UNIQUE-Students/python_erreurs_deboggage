import numpy as np


def transpose(y):
    y = y.moveaxis(0, 1)
    return y


def multiply(x, y):
    y = transpose(y)
    z = np.matmul(x, y)
    return z


def convert_to_int(x):
    return x.astype("int")
