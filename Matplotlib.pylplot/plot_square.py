import matplotlib.pyplot as plt
import numpy as np


Q = np.arange(0,10*np.pi,0.1)#(start,stop,step)


x = np.sin((Q)**2)
plt.title("sinQ")
plt.subplot(6,1,1)
plt.plot(Q,x,color='black')


y = np.cos((Q)**2)
plt.title("cosQ")
plt.subplot(6,1,2)
plt.plot(Q,y,color='blue')


z = np.tan((Q)**2)
plt.title("tanQ")
plt.subplot(6,1,3)
plt.plot(Q,z,color='yellow')

a = np.sin(-Q)
plt.title("cosecQ")
plt.subplot(6,1,4)
plt.plot(Q,a,color='orange')


b = np.cos(-Q)
plt.title("secQ")
plt.subplot(6,1,5)
plt.plot(Q,b,color='pink')


c = np.tan(-Q)
plt.title("cotQ")
plt.subplot(6,1,6)
plt.plot(Q,c,color='brown')


plt.show()

