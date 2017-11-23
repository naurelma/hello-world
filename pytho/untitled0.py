# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 21:16:36 2017

@author: Niko
"""

from statistics import mean
import numpy as np
from matplotlib import pyplot as plt

xs = np.array([1, 2, 3, 4, 5], dtype=np.float64)
ys = np.array([5, 4, 3, 2, 6], dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)

    return m, b

m, b = best_fit_slope_and_intercept(xs, ys)

print(m, b)

plt.scatter(xs, ys)

ys2 = [(m*x+b) for x in xs]
plt.plot(xs, ys2)
plt.show()
