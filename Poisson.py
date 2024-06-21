# importing poisson from scipy
from scipy.stats import poisson
 
# importing numpy as np
import numpy as np
 
import matplotlib
matplotlib.use('TkAgg')

# importing matplotlib as plt
import matplotlib.pyplot as plt

from bacteria import *

from math import *

def calc_conc(num_empty):
    mean = calc_mean(num_empty)
    return mean / vol_well * 1000 ## in mL

num_wells = 96
vol_well = 150

power = int(input("Starting density (powers of 10), bacteria/gram: "))
start_conc = 10 ** power
start_conc = start_conc / 1000 * 5 / 1.5 / 15

singles = np.array(run_pops(WellPlate(vol_well, num_wells), 100)[:-1])
conc = []

for i, _ in enumerate(singles):
    conc.append(calc_conc(96 - i)/ start_conc)
np.array(conc)

plt.plot(conc, np.array([96 - i for i in range(num_wells)]), "g", label="Total Growth")
plt.plot(conc, singles, "r", label="Single Growths")
plt.xlabel("Concentration (bacteria / mL)")
plt.ylabel("Number of wells with growth")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.legend(loc="upper right")
plt.title(f"Dilutions for starting density: $10^{{{power}}}$ bacteria / gram")
plt.show()



    



# for i in range(x):
#     mean = -log(1 - i/x)
#     prob1 = exp(-mean) * mean
    
#     prob2 = i/x - prob1
    
#     percent = exp(prob1 -prob2) * 100

#     lst.append([i, int(prob1 * x), int(prob2 * x), int(percent)])

# print(np.array(lst))
    
# plt.plot()

 

# # creating a numpy array for x-axis
# x = np.arange(0, 4, 1)
 
# # poisson distribution data for y-axis
# y = poisson.pmf(x, mu=0.3567)

# # plotting the graph
# plt.plot(x, y)
 
# # showing the graph
# plt.show()

