# importing poisson from scipy
from scipy.stats import poisson
 
# importing numpy as np
import numpy as np
 
import matplotlib
matplotlib.use('TkAgg')

# importing matplotlib as plt
import matplotlib.pyplot as plt

from env import *

from math import *

lst = []

x = 96

for i in range(x):
    mean = -log(1 - i/x)
    prob1 = exp(-mean) * mean
    
    prob2 = i/x - prob1
    
    percent = exp(prob1 -prob2) * 100

    lst.append([i, int(prob1 * x), int(prob2 * x), int(percent)])

print(np.array(lst))
    

        

 

# # creating a numpy array for x-axis
# x = np.arange(0, 4, 1)
 
# # poisson distribution data for y-axis
# y = poisson.pmf(x, mu=0.3567)

# # plotting the graph
# plt.plot(x, y)
 
# # showing the graph
# plt.show()

