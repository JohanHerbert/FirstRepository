import inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
from scipy.stats import norm, lognorm # gives us the normal and log normal pdf,cdf and inverse cdf (ppf,point percent function)
from scipy.stats.mstats import gmean #geomeetric mean

x = np.array([1,2,3])
print(x)

type(x)

x = np.arange(1,6)
print(x)


x = np.arange(1,6,0.5)
print(x)

x = np.linspace(1,6,11)
print(x)

#x.shape

#zero vectors
B = np.zeros((2,5))
print(B)

# one vector
C = np.ones((2,5))
print(C)

#identity matrix
I = np.eye(3)
print(I)

A = np.array([1,2,3],[4,5,6])
A.shape







