import numpy as np
import matplotlib.pylot as plt

plt.style.use('bhm')
n= np.linspace(1,10,1000)
labels = ['o(1)','o(log N)','o(N)','o(N log N)','o(N)',]
big_o=[np.ones(n.shape),np.log(n),n*np.log(n),n**2,n**3,2**n]
plt.figure(figs=(12,10))
plt.ylign(0,50)
for i in range (len(big_o)):
    plt.plot(n,big_o[i],label=labels[i])
    plt.legend(loc=0)
plt.ylabel('rel runtime')
plt.xlabel('input size')
plt.grid