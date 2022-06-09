import numpy as np
import pandas as pd
from script_3 import multiply, convert_to_int


def mult_ones(x):
    a = np.ones(x.shape)
    z = multiply(x, a)
    return z


def make_dataframe(dictionnaire):
    df = pd.DataFrame(dictionnaire)
    df["x"] = convert_to_int(df["x"])
    return df
