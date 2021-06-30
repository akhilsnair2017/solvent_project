import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker
from shapely.geometry import LineString

fig,ax=plt.subplots()
u=[0.4,1.24,1.4]
ph=list(np.arange(0,16,2))
x_1=[u[0]-0.059*i for i in ph]
x_2=[u[1]-0.059*i for i in ph]
#x_3=[u[2]-0.059*i for i in ph]
count=len(x_2)
x_3=[1.4]*count
#x_4=[u[3]-0.059*i for i in ph]

ax.plot(ph,x_1,c='gray',label='Pt (111)')
ax.fill_between(ph,x_1,color='gray')
ax.plot(ph,x_2,c='red',label='0.33 ML OH')
ax.fill_between(ph,x_1,x_2,np.min(x_2),color='red')
ax.plot(ph,x_3,c='blue',label='0.33 ML O')
#ax.fill_between(ph,x_2,x_3,np.min(x_3),color='green')
#ax.plot(ph,x_4,c='blue',label='1/3 ML O')
ax.fill_between(ph,x_2,x_3,np.max(x_3),color='blue')

#plt.axhline(y=0.0,linestyle='--',color='black')
ax.set_xlim(0.0,14)
ax.set_ylim(0.0,1.4)
#ax.legend()
#fig.tight_layout(pad=0.1)
plt.rcParams["font.family"] = "Times New Roman"
#plt.figure(figsize=(10,80))
#plt.xticks(np.arange(min(x), max(x)+1, 0.2))
ax.set_ylabel(r'$U_{SHE}$(eV)')
ax.set_xlabel('pH')
plt.legend(facecolor='white',framealpha=1)
################################
#e=np.array(
#id_b_c = np.argwhere(np.diff(np.sign(b - c))).flatten()
#id_d_b=np.argwhere(np.diff(np.sign(b - d))).flatten()
#plt.plot(U_list[idx],GO_list[idx], 'ro')
plt.show()

#print(U_list)
