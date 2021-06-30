import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as plticker
from shapely.geometry import LineString

method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
U_list=list(np.linspace(0,1.4,8))
GOH_list=[0.06,0.04,0.02,-0.01,-0.03,-0.05,-0.07,-0.10]
G2OH_list=[0.19,0.10,0.01,-0.07,-0.16,-0.25,-0.34,-0.43]
G3OH_list=[0.39,0.19,-0.01,-0.21,-0.41,-0.61,-0.81,-1.01]
GO_list=[0.15,0.11,0.07,0.02,-0.02,-0.07,-0.11,-0.16]
G2O_list=[0.70,0.52,0.35,0.17,-0.01,-0.19,-0.37,-0.54]
G3O_list=[1.63,1.23,0.83,0.43,0.03,-0.37,-0.77,-1.17]
GPt_list=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
###############################
fig,ax=plt.subplots()
ax.plot(U_list,GOH_list,c='m',label='0.11 ML OH')
ax.plot(U_list,G2OH_list,c='y',label='0.22 ML OH')
ax.plot(U_list,G3OH_list,c='c',label='0.33 ML OH')
ax.plot(U_list,GO_list,c='r',label='0.11 ML O')
ax.plot(U_list,G2O_list,c='g',label='0.22 ML O')
ax.plot(U_list,G3O_list,c='b',label='0.33 ML O')
ax.plot(U_list,GPt_list,c='black',label='Pt(111)')

########################################
stepsize=0.1
loc_x = plticker.MultipleLocator(base=0.1)
loc_y=plticker.MultipleLocator(base=0.4)
ax.xaxis.set_major_locator(loc_x)
plt.axhline(y=0.0,linestyle='--',color='black')
ax.set_xlim(0.0,1.4,0.2)
ax.legend()
#fig.tight_layout(pad=0.1)
plt.rcParams["font.family"] = "Times New Roman"
#plt.figure(figsize=(10,80))
ax.set_xticks([0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4])
ax.set_xlabel('$U_{SHE}$(eV)')
ax.set_ylabel('$\Delta$G (eV/surface atom)')
################################
a=np.array(U_list)
b=np.array(GO_list)
c=np.array(GPt_list)
d=np.array(G2O_list)
e=np.array(G3OH_list)
j=np.array(G3O_list)
#e=np.array(
#id_b_c = np.argwhere(np.diff(np.sign(b - c))).flatten()
#id_d_b=np.argwhere(np.diff(np.sign(b - d))).flatten()
f=LineString(np.column_stack((a,b)))
g=LineString(np.column_stack((a,c)))
h=LineString(np.column_stack((a,d)))
i=LineString(np.column_stack((a,e)))
k=LineString(np.column_stack((a,j)))
f_g_inter= f.intersection(g)
b_d_inter=f.intersection(h)
d_e_inter=h.intersection(i)
e_k_inter=i.intersection(k)
##########GO_vs_GPt##############
if f_g_inter.geom_type == 'Point':
    x, y = f_g_inter.xy
    print(x,y)
###########GOvsG2O#################
if b_d_inter.geom_type == 'Point':
   x,y=b_d_inter.xy
   print(x,y)
###########G2OvsG3OH###################
if d_e_inter.geom_type == 'MultiPoint':
   x,y=d_e_inter.xy
   print(x,y)
#########G3OHvsG3O###############
if e_k_inter.geom_type == 'Point':
   x,y=e_k_inter.xy
   print(x,y)

#print(a[id_b_c])
#print(a[id_d_b],d[id_d_b])
#plt.axvline(
#plt.plot(U_list[idx],GO_list[idx], 'ro')
plt.show()
#print(U_list)
