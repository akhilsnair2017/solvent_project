import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
# y-axis in bold
#rc('font', weight='bold')

# Values of each group
#O2_bars1 = [0.63,1,0.88,0.80,0.23,0.43,0.63,0.47,0.67,0.57,0.73]
OH_1ML=[0.89,0.92,0.92,1.30,1.13,0.12,0.89,-0.29,0.78,0.66,0.75]
#O_bars2 = [0.34,0.95,0.7,0.27,0.60,0.62,0.49,0.83,0.5,0.78,0.70]
OH_2ML=[1.88,1.70,1.78,2.31,1.85,-0.47,1.71,0.10,1.63,0.83,1.35]
#OH_bars3 = [-0.09,0.15,0.03,0.1,0.31,-0.82,0.12,-0.86,0.08,-0.09,-0.03]
OH_3ML=[2.60,2.10,2.45,3.22,2.46,0.30,1.27,0.79,2.16,1.38,1.97]

# Heights of bars1 + bars2
#O2_O_bars = np.add(O2_bars1,O_bars2).tolist()
#O_OH_bars=np.add(O2_bars1,O_bars2,OH_bars3).tolist()
#OH_OOH_bars=np.add(OH_bars3,OOH_bars4).tolist()
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9,10,11]

# Names of group and bar width
names = ['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
barwidth = 0.2

x_1=np.arange(len(OH_1ML))
x_2=[i+barwidth for i in x_1]
x_3=[i+barwidth for i in x_2]
#x_4=[i+barwidth for i in x_3]

plt.bar(x_1,OH_1ML,color='k',width=barwidth,edgecolor='black',label='0.11 ML OH')
plt.bar(x_2,OH_2ML,color='c',width=barwidth,edgecolor='black',label='0.22 ML OH')
plt.bar(x_3,OH_3ML,color='y',width=barwidth,edgecolor='black',label='0.33 ML OH')
#plt.bar(x_4,OOH_bars4,color='brown',width=barwidth,edgecolor='black',label='*OOH')

plt.xlabel('Dispersion Method',fontweight='bold',fontsize=12)
plt.ylabel('OH Binding energy (eV)',fontweight='bold',fontsize=12)
plt.xticks([i+barwidth for i in range(len(OH_1ML))],names)
plt.axhline(0.0,color='black')
plt.legend()
#plt.savefig('Solvation energy.png')
plt.show()

