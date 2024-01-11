import numpy as np
import matplotlib.pyplot as plt
import random 

X=[0]
t=[0] #as the simulation goes on new values will be appended to this array 

k=2
gamma=0.1 
tend=1000

while t[-1] < tend :

    current=X[-1]

    rates = [k, gamma*current]

    rsum= sum(rates)

    tau = np.random.exponential(scale = 1/rsum) #selects random time points from an exponential distribution 

    t.append(t[-1]+tau)

    rand = random.uniform(0,1)

    # production event
    if rand * rsum > 0 and rand * rsum <= rates[0]: #lesser than K 
                X.append(X[-1] + 1) #X gets updated with X+1

    # decay event
    elif rand * rsum > rates[0] and rand * rsum <= rates[0] + rates[1]: #between K and gamma.x
                X.append(X[-1] - 1) #X gets updated with X-1

    
plt.plot(t,X)
plt.xlabel("time")
plt.ylabel("mRNA quantity")
plt.show()


