import matplotlib.pyplot as plt
#matplotlib.use('Qt5Agg')
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','vdW-DF','vdW-DF2','optPBE','optB88','optB86b']
lat=[5.743,6.600,5.787,5.646,5.566,6.046,5.938,7.119,5.971,6.069,6.307]
exp=[6.091,5.683,5.764,6.886,5.565,5.574,6.201,5.926,6.963,6.044,5.896]
mad=[0.73,0.44,0.46,0.66,0.51,0.30,0.66,0.26,0.50,0.46,0.48]
difference=[]
zip_object=zip(lat,exp)
for i,j in zip_object:
    difference.append(i-j)
fig,ax = plt.subplots()
# make a plot
ax.plot(method, difference, color="red", marker="o",linestyle='--')
# set x-axis label
ax.set_xlabel("Dispesion Method",fontsize=14)
# set y-axis label
ax.set_ylabel("workfunctioin change (eV)",color="red",fontsize=14)
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(method,mad,color="blue",marker="o", linestyle='--')
ax2.set_ylabel("mean absolte bond length deviation ($\AA$)",color="blue",fontsize=14)
plt.show()
# save the plot as a file
#fig.savefig('work_bond.jpg',
#            format='jpeg',
#            dpi=100,
#            bbox_inches='tight')
#plt.plot(method,difference,'rd')

#plt.axvline(y=3.923)
#plt.xlabel('Dispersion Method')
#plt.axhline(y=5.7, linestyle='--')
#plt.axhline(y=6.1, linestyle='--')
#plt.ylabel(r'$\phi$ (eV)')
#plt.text(0,5.9,'Experimetnal')
#plt.title('Workfunction')
plt.show()
