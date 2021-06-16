from math import *
import pandas as pd
from statistics import *
import sympy
from sympy import symbols, Eq, solve

kbt=0.026 #eV
pref=10E9
def thermo_equb_const(G):
    return exp(-G/kbt)
def electro_equb_const(G,U):
    return exp(-(U-G)/kbt)
def thermo_rate_const(ea,pref):
    return pref*exp(-ea/kbt)
def electro_rate_const(pref,ea,U,G):
    return pref*exp(-ea/kbt)*exp(-0.5*(U-G)/kbt)
reactions=['O2(aq)--O2(dl)','O2(dl)+*--O2_s1*','O2_s1*+H--OOH_s1*','OOH_s1*+H--O_s1*+H2O','O_s1*+H--OH*','OH_s1*+H--*+H2O','*O2 →*O_s1+*O_s2','*O_s1 + *O_s2 + (H++e-) → *O_s1+ *OH_s2','*O_s1 + *OH_s2 + (H++e-) → *OH_s1+ *OH_s2','*OOH_s1 →*O_s1+*OH_s2','*O_s1 + *OH_s2 + (H++e-) → *O_s1+ H2O','*OOH_s1+(H++e-) →*H2O2_s1','*H2O2 → *OH_s1+ *OH_s2','*OH_s1+*OH_s2 + (H++e-) →*OH_s1+ H2O']
pref=[8E5,1E8,1E9,1E9,1E9,1E9,1E9,1E9,1E9,1E9,1E9,1E9,1E9,1E9]
pref=[float(i) for i in pref]
#print(G)
G_0=[0.00,-0.345,-0.688,-2.185,-0.905,-0.797,-0.773,-0.905,-0.784,-0.99,-1.193,-0.556,-1.22,-1.314]
G_0=[float(i) for i in G_0]
ea=[0.00,0.00,0.26,0.26,0.26,0.26,0.77,0.26,0.26,0.26,0.26,0.26,0.02,0.26]
ea=[float(i) for i in ea]
U=[0,0.2,0.4,0.6,0.8,1.0,1.2,1.4]
U_list=[float(i) for i in U]
#j=float(input('Potential: '))
for j in U_list:
    Ea_list=[]
    eq_list=[]
    kf_list=[]
    kb_list=[]
    delta_G_list=[]
    for i,react in enumerate(reactions):
        if i==0 or i==1 or i==6 or i==9 or i==12:
            K_eq=thermo_equb_const(G_0[i])
            k_f=thermo_rate_const(ea[i],pref[i])
            k_b=k_f/K_eq
            delta_G=G_0[i]
            Ea=ea[i]
        else:
            K_eq=electro_equb_const(-G_0[i],j)
            k_f= electro_rate_const(pref[i],ea[i],j,-G_0[i])
            k_b=k_f/K_eq
            delta_G=G_0[i]+j
            Ea=ea[i]
    #        tof_h2o=electro_rate_const(pref[i],ea[i],j,-G[i])
        eq_list.append('{:.3e}'.format(K_eq))
        kf_list.append('{:.3e}'.format(k_f))
        kb_list.append('{:.3e}'.format(k_b))
        delta_G_list.append(delta_G)
        Ea_list.append(Ea)
    #    Ea_list
    d={'Reactions':reactions,'Equb_Constant':eq_list,'Forward_rate':kf_list,'Backward_rate':kb_list,'Free Energy':delta_G_list,'Barrier': Ea_list}
    s = pd.DataFrame(d)
    print('\nPotential(U): {}\n'.format(j))
    print(s)

#####Differential Equation Solving#############
##x=theta_*
##y=theta_O*
##z=theta_OH*
##a=theta_OOH*
##b=theta_xo2(dl)
## defining symbols used in equations
## or unknown variables
    a,b,c,d,e,f = symbols('a b c d e f')
#kf_1,kb_1,kf_2,kb_2,kf_3,kb_3,kf_4,kb_4,kf_5,kb_5,kf_6,kb_6=8.000e+05,8.000e+05,1.000e+08,1.727e+02,2.530e+10,8.147e-02,8.050e+22,2.561e-14,1.642e+12,1.255e-03,2.058e+11,1.002e-02
## defining equations
    kf_list=[float(i) for i in kf_list]
    kb_list=[float(i) for i in kb_list]
    kf_1,kb_1,kf_2,kb_2,kf_3,kb_3,kf_4,kb_4,kf_5,kb_5,kf_6,kb_6=kf_list[0],kb_list[0],kf_list[1],kb_list[1],kf_list[2],kb_list[2],kf_list[3],kb_list[3],kf_list[4],kb_list[4],kf_list[5],kb_list[5]

####################
    eq1 = Eq((kf_1-kb_1*a-kf_2*a*b+kb_2*c), 0)
    print("Equation 1:")
    print(eq1)

    eq2 = Eq((kf_2*a*b-kb_2*c-kf_3*c+kb_3*d), 0)
    print("Equation 2")
    print(eq2)

    eq3 = Eq((kf_3*c-kb_3*d-kf_4*d+kb_4*e), 0)
    print("Equation 3")
    print(eq3)


    eq4 = Eq((kf_4*d-kb_4*e-kf_5*e+kb_5*f), 0)
    print("Equation 4")
    print(eq4)

    eq5 = Eq((kf_5*e-kb_5*f-kf_6*f+kb_6*b), 0)
    print("Equation 5")
    print(eq5)

    eq6 = Eq((a+b+c+d+e+f), 1)
    print("Equation 6")
    print(eq6)
    #
    print("Values of 6 unknown variable are as follows:")
    sol_dict=sympy.solve([eq1,eq2,eq3,eq4,eq5,eq6], (a,b,c,d,e,f))
    print(sol_dict)
    print('xO2(dl):{:.3e}'.format(sol_dict[0][0]))
    print(r'Θ*:{:.3e} '.format(sol_dict[0][1]))
    print(r'Θ_O2*: {:.3e}'.format(sol_dict[0][2]))
    print(r'Θ_OOH*: {:.3e}'.format(sol_dict[0][3]))
    print(r'Θ_O*:{:.3e}'.format(sol_dict[0][4]))
    print(r'Θ_OH*:{:.3e}'.format(sol_dict[0][5]))
#
