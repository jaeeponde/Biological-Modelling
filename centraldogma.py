import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
from scipy.integrate import odeint 

#first we name initial conditions 
y0=[0,0] # we are starting with 0 mrnas and 0 proteins

t = np.linspace(0,200,num=100) #100 different timepoints between 0 and 200 

k_m = 0.4
gamma_m=0.05
k_p = 0.2
gamma_p=0.08

params = [k_m,gamma_m,k_p,gamma_p] # list of parameters

#differential expression function

def centraldogma(variables, timepoints, parameters):
    m = variables[0]
    p = variables[1]

    k_m=params[0]
    gamma_m=params[1]
    k_p=params[2]
    gamma_p=params[3]

    dmdt = k_m - gamma_m*m
    dpdt = k_p*m - gamma_p*p

    return([dmdt,dpdt]) #make sure this order corresponds to the variable array

y = odeint(centraldogma, y0, t, args =(params,))

f,ax = plt. subplots (1)

line1, = ax.plot(t,y[:,0], color="b", label="M")
line2, = ax.plot(t,y[:,1], color="r", label="p")
ax. set_ylabel("Abundance")
ax.set_xlabel("Time")
ax. legend (handles= [line1, line2])
plt.show ()










