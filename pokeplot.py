import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error
import unittest

figWidth = 20
figHeight = 15
resolution = 70

plt.figure(figsize=(figWidth, figHeight), dpi=resolution)

pokedata = np.genfromtxt(
    "pokemon.csv", names=True,
    dtype="float", delimiter=",")
plt.xlabel('Pokemon HP')
plt.ylabel('Pokemon Attack')
plt.plot(pokedata["HP"], pokedata["Attack"], "o")
plt.savefig("out.png")


def line(x, slope, intercept):
    return slope * x + intercept


def cal_y_predict(x_values, slope, intercept):
    y_predict_values = []
    for x in x_values:
        y_value = line(x, slope, intercept)
        y_predict_values.append(y_value)
    return y_predict_values


def cal_mse(y_predict_values, y_real_values, ax):
    return ((y_predict_values - y_real_values)**2).mean(axis=ax)


y_predict_values = cal_y_predict(pokedata["HP"], 10, 0)
mse = cal_mse(np.array(y_predict_values), np.array(pokedata["Attack"]), 0)
sklearn_mse = mean_squared_error(y_predict_values, pokedata["Attack"])


class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(mse, sklearn_mse)


unittest.main()
