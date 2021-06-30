import numpy as np
import matplotlib.pyplot as plt
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
lat=[0.233,0.121,0.34,0.023,0.357,0.05,0.112,-0.234,0.162,0.176,0.281]
num=list(range(1,12))
plt.plot(num,lat,'b*')
#plt.axvline(y=3.923)
#plt.annotate("Point 1", ('PBE',0.233))
#plt.xlabel('Dispersion Method')
plt.axhline(y=0.0, linestyle='--',color='r')
plt.xticks(np.arange(1,12,1))
plt.ylabel('Relative stabiity (eV)',fontsize=15)
plt.xticks([])
plt.ylim(-0.3,0.4,7)
#plt.text(0,3.93,'Experimetnal')

for x,y in zip(num,lat):
    for i in method:
        if num.index(x)==method.index(i):
            label = i
            plt.annotate(i, # this is the text
            (x,y), # this is the point to label
            textcoords="offset  points", # how to position the text
            xytext=(0,6), # distance from text to points (x,y)
            ha='center')
plt.title('Relative Stability difference for water bilayer configurations')
plt.rcParams["font.family"] = "Times New Roman"

plt.show()
