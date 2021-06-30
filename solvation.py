import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
# y-axis in bold
#rc('font', weight='bold')

# Values of each group
O2_bars1 = [0.63,1,0.88,0.80,0.23,0.43,0.63,0.47,0.67,0.57,0.73]
O_bars2 = [0.34,0.95,0.7,0.27,0.60,0.62,0.49,0.83,0.5,0.78,0.70]
OH_bars3 = [-0.09,0.15,0.03,0.1,0.31,-0.82,0.12,-0.86,0.08,-0.09,-0.03]
OOH_bars4=[0.20,0.66,0.46,-0.02,0.61,0.26,0.32,-0.78,0.32,0.32,0.32]

# Heights of bars1 + bars2
#O2_O_bars = np.add(O2_bars1,O_bars2).tolist()
#O_OH_bars=np.add(O2_bars1,O_bars2,OH_bars3).tolist()
#OH_OOH_bars=np.add(OH_bars3,OOH_bars4).tolist()
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9,10,11]

# Names of group and bar width
names = ['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
barwidth = 0.2

x_1=np.arange(len(O2_bars1))
x_2=[i+barwidth for i in x_1]
x_3=[i+barwidth for i in x_2]
x_4=[i+barwidth for i in x_3]

plt.bar(x_1,O2_bars1,color='r',width=barwidth,edgecolor='black',label='$*O_2$')
plt.bar(x_2,O_bars2,color='b',width=barwidth,edgecolor='black',label='*O')
plt.bar(x_3,OH_bars3,color='g',width=barwidth,edgecolor='black',label='*OH')
plt.bar(x_4,OOH_bars4,color='brown',width=barwidth,edgecolor='black',label='*OOH')

plt.xlabel('Dispersion Method',fontweight='bold',fontsize=12)
plt.ylabel('Solvation Energy (eV)',fontweight='bold',fontsize=12)
plt.xticks([i+barwidth for i in range(len(O2_bars1))],names)
plt.axhline(0.0,color='black')
plt.legend()
#plt.savefig('Solvation energy.png')
plt.show()
