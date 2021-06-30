import matplotlib.pyplot as plt
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
lat=[3.962,3.836,3.913,3.986,3.854,3.934,4.034,4.111,3.986,3.975,3.942]
plt.plot(method,lat,'rd',markersize=12)
#plt.axvline(y=3.923)
plt.xlabel('Dispersion Method',size=15)
plt.axhline(y=3.923, linestyle='--')
plt.ylabel('Lattice Constant',size=15)
plt.xticks(fontsize=10)
plt.text(0,3.93,'Experimetnal')
plt.title('Platinum Bulk Lattice Parameters',size=15)
plt.rcParams["font.family"] = "Times New Roman"
plt.show()
