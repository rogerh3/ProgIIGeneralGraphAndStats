#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 00:23:49 2021

@author: rh.hayden
Title: Final Program - Programming II
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y=[3,4,1,7,8,10,13,12,17,20]
z=[21,17,18,16,15,13,10,9,5,1]



plt.plot(x, y)
plt.plot(x, z)
plt.title('X vs. Y and Z')
plt.legend(["Y", "Z"])
plt.show() 

#mean and median of y
c = np.mean(y)
print('The mean of y is:')
print(c)
r = np.median(y)
print('The median of y is:')
print(r)
#mean and median of z
q = np.mean(z)
print('The mean of z is:')
print(q)
e = np.median(z)
print('The median of z is:')
print(e)