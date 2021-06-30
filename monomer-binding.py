import matplotlib.pyplot as plt
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
lat=[0.209,0.652,0.456,0.036,0.440,0.417,0.255,0.364,0.383,0.427,0.458]
plt.bar(method,lat, color='r',width=0.35)
#plt.axvline(y=3.923)
plt.xlabel('Dispersion Method')
#plt.axhline(y=5.7, linestyle='--')
#plt.axhline(y=6.1, linestyle='--')
plt.ylabel('Energy (eV)')
#plt.text(0,5.9,'Experimetnal')
plt.title('Water monomer adsorption energy')
plt.rcParams['font.serif'] = "Times New Roman"
plt.xticks(fontsize=8)
plt.yticks(fontsize=12)
plt.show()
