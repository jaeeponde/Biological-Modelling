# we make assumption that the expression of gene 1 facilitates the translation of gene 2
# modelling the hill function 

import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
from scipy.integrate import odeint 



y0 = [0,0]
t = np.linspace(0,200, num=100)

k_1 = 0.4
gamma_1 = 0.1
k_2 = 0.9
gamma_2 = 0.1
n = 4
c = 1


params = [k_1, gamma_1, k_2, gamma_2, n, c]



def sim(variables,t,params):

    G1 = variables[0]
    G2 = variables[1]

    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c = params[5]



    dG1dt = k_1 - gamma_1 * G1

    dG2dt = (c**n / (c**n + G1**n)) * k_2 - gamma_2 * G2


    return([dG1dt,dG2dt])



y = odeint(sim,y0,t, args=(params,))



f, ax = plt.subplots(1)

line1, = ax.plot(t , y[:,0], color="b",label="G1")
line2, = ax.plot(t , y[:,1], color="r",label="G2")

ax.set_ylabel('Number')
ax.set_xlabel('Time')

ax.legend(handles=[line1,line2])

plt.show()