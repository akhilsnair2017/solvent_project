import numpy as np
import matplotlib.pyplot as plt
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
bl=[0.536,0.937,0.769,0.382,0.681,0.635,0.542,0.709,0.663,0.691,0.729]
hb=[0.404,0.464,0.454,0.335,0.384,0.380,0.351,0.497,0.411,0.411,0.410]
barwidth=0.25
fig=plt.subplots(figsize=(12,8))
bar_1=np.arange(len(bl))
bar_2=[i+barwidth for i in bar_1]
plt.bar(method,bl, color='b',width=0.25,edgecolor='black',label="Bilayer adsorption Energy")
plt.bar(bar_2,hb,color='r',width=0.25,edgecolor='black',label='Hydrogen Bonding Energy')
#plt.axvline(y=3.923)
plt.xlabel('Dispersion Method',fontsize=15)
#plt.axhline(y=5.7, linestyle='--')
#plt.axhline(y=6.1, linestyle='--')
plt.ylabel('Energy (eV)',fontsize=15)
#plt.text(0,5.9,'Experimetnal')
leg=["Bilayer adsorption","Hydrogen bonding" ]
plt.rcParams["font.family"] = "Times New Roman"
plt.legend(leg,loc=1,fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
#plt.title('Water bilayer binding energy')
plt.show()
