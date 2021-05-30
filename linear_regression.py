import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from scipy import stats
import numpy as np
from statistics import mean
import pandas as pd
method=['PBE','PBE-D2','PBE-D3','RPBE','RPBE-D2','RPBE-D3','revPBE','rPW86','optPBE','optB88','optB86b']
O2_G=[4.06,3.77,3.84,4.16,3.87,3.75,3.51,3.31,3.60,3.59,3.53]
O_G=[1.36,1.39,1.30,1.44,1.49,1.31,1.07,0.88,1.06,1.02,1.04]
OH_G=[0.89,0.54,0.69,0.98,0.68,0.73,0.65,0.49,0.59,0.57,0.61]
OOH_G=[3.71,3.20,3.39,3.80,3.34,3.31,3.15,2.96,3.17,3.21,3.14]
O2_s=[4.69,4.77,4.72,4.96,4.10,4.18,4.14,3.78,4.27,4.16,4.26]
O_s=[1.83,2.33,2.10,1.77,2.14,2.07,1.66,1.83,1.76,1.73,1.83]
OH_s=[0.81,0.62,0.72,1.01,0.90,0.02,0.78,-0.45,0.70,0.54,0.58]
OOH_s=[3.91,3.86,3.85,3.78,3.9,3.57,3.47,2.18,3.49,3.53,3.46]
#hb=[0.404,0.464,0.454,0.335,0.384,0.380,0.351,0.497,0.411,0.411,0.410]
#REGRESSION FUNCTION
def linear_regression(x, y):
    N = len(x)
    x_mean = x.mean()
    y_mean = y.mean()
    B1_num = ((x - x_mean) * (y - y_mean)).sum()
    B1_den = ((x - x_mean)**2).sum()
    B1 = B1_num / B1_den
    B0 = y_mean - (B1*x_mean)
    reg_line = 'y = {} + {}β'.format(B0, round(B1, 3))
    num = (N * (x*y).sum()) - (x.sum() * y.sum())
    den = np.sqrt((N * (x**2).sum() - x.sum()**2) * (N * (y**2).sum() - y.sum()**2))
    R = num / den
    text = '''
            $R^2$: {}
            O_BE = {}*OH_BE + {}'''.format(
                       round(R**2, 2),
                       round(B1, 2),
                       round(B0, 2))
    return (B0,B1,reg_line,R,R**2,text)
#######################################
oh_vs_o={'OH':OH_G,'O':O_G,'OOH':OOH_G}
df=pd.DataFrame(oh_vs_o)
o_be=df['O']
oh_be=df['OH']
ooh_be=df['OOH']
fig=plt.figure(figsize=(10,60))
ax1=plt.subplot(1,2,1,ylabel='Adsorption Energy (eV)')
plt.scatter(oh_be,o_be)
plt.xlim(0.1,1.6)
plt.ylim(0,4)

plt.plot(oh_be, linear_regression(oh_be,o_be)[0]+ linear_regression(oh_be,o_be)[1]*oh_be, c = 'black', linewidth=5, alpha=.5, solid_capstyle='round')
plt.text(x=0.2,y=0.2, s=linear_regression(oh_be,o_be)[5], fontsize=8, bbox={'facecolor': 'grey', 'alpha': 0.1, 'pad': 8})

plt.scatter(oh_be,ooh_be)
plt.plot(oh_be, linear_regression(oh_be,ooh_be)[0]+ linear_regression(oh_be,ooh_be)[1]*oh_be, c = 'black', linewidth=5, alpha=.5, solid_capstyle='round')
plt.text(x=0.2,y=2.3, s=linear_regression(oh_be,ooh_be)[5], fontsize=8, bbox={'facecolor': 'grey', 'alpha': 0.1, 'pad': 8})


ax2=plt.subplot(1,2,2,ylabel='Adsorption Energy (eV)')
s_be={'OH':OH_s,'O':O_s,'OOH':OOH_s}
df_s=pd.DataFrame(s_be)
so_be=df_s['O']
soh_be=df_s['OH']
sooh_be=df_s['OOH']
plt.scatter(soh_be,so_be)
plt.xlim(-0.6,1.6)
plt.ylim(1.5,4)
plt.plot(soh_be, linear_regression(soh_be,so_be)[0]+ linear_regression(soh_be,so_be)[1]*soh_be, c = 'black', linewidth=5, alpha=.5, solid_capstyle='round')
plt.text(x=0.2,y=2.1, s=linear_regression(soh_be,so_be)[5], fontsize=8, bbox={'facecolor': 'grey', 'alpha': 0.1, 'pad': 8})

plt.scatter(soh_be,sooh_be)
plt.plot(soh_be, linear_regression(soh_be,sooh_be)[0]+ linear_regression(soh_be,sooh_be)[1]*soh_be, c = 'black', linewidth=5, alpha=.5, solid_capstyle='round')
plt.text(x=0.2,y=2.5, s=linear_regression(soh_be,sooh_be)[5], fontsize=8, bbox={'facecolor': 'grey', 'alpha': 0.1, 'pad': 8})

#plt.bar(bar_2,hb,color='r',width=0.25,edgecolor='black',label='Hydrogen Bonding Energy')
#plt.axvline(y=3.923)
plt.xlabel('Dispersion Method',fontsize=15)
#plt.axhline(y=5.7, linestyle='--')
#plt.axhline(y=6.1, linestyle='--')
#plt.ylabel('Energy (eV)',fontsize=15)
#plt.text(0,5.9,'Experimetnal')
#leg=["Bilayer adsorption","Hydrogen bonding" ]
plt.rcParams["font.family"] = "Times New Roman"
#plt.legend(leg,loc=1,fontsize=12)
#plt.xticks(fontsize=12)
#plt.yticks(fontsize=12)
#plt.title('Water bilayer binding energy')
plt.show()
