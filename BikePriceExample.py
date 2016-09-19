# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:23:28 2016

@author: Sachin Hooda
"""

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

x=np.array([100,125,158,179,250,420,600,1000])
y=np.array([12000,15000,16021,18000,25034,45020,53456,82010])

slope,intercept,r_value,p_value,std_err=stats.linregress(x,y)

plt.plot(x,y,'ro',color='black')
plt.ylabel('Price')
plt.xlabel('CC Engine')
plt.axis([0,1200,0,85000])
plt.show()

newBikeCC=350
print(newBikeCC*slope+intercept)