# '''area1 = np.ma,masked_where(r<r0,area)
#    area2 = np.ma,masked_where(r>=r0,area)
#    plt.scatter(x,y,s=area,marker='^',c=color)
#    plt.scatter(x,y,s=area,marker='o',c=color)'''

import matplotlib.pyplot as plt
import numpy as np

N = 100
r0= 0.6
x = 0.9*np.random.rand(N)
y = 0.9*np.random.rand(N)
area = (20*np.random.rand(N)**2)
color = np.sqrt(area)
r = np.sqrt(x**2 + y**2)
area1 =  np.ma.masked_where(r<r0,area)
area2 = np.ma.masked_where(r>=r0,area)

plt.figure()
plt.scatter(x,y,s=area1,marker = '^',c=color)
plt.scatter(x,y,s=area,marker ='o',c = color)
plt.title("show without boundary")
plt.show()

plt.figure()
plt.scatter(x,y,s=area1,marker = '^',c=color)
plt.scatter(x,y,s=area,marker ='o',c = color)
plt.title("show with boundary")
Q = np.arange(0,np.pi/2,0.01)
plt.plot(r0 * np.cos(Q),r0*np.sin(Q))
plt.show()