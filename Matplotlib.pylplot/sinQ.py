import matplotlib.pyplot as plt
import numpy as np

Q = np.arange(0,2*np.pi,0.1)
x = np.sin(Q)

plt.plot(x,color='red')
plt.show()


#or

s = np.sin(Q)
fig,ax = plt.subplots()
ax.plot(Q,s)
ax.set(xlabel='radian',ylabel='sin(Q)',title='Sine plot')
fig.savefig('sine_plot.png')
plt.show()
       
