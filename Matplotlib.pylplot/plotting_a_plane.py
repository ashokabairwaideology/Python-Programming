import matplotlib.pyplot as plt
import numpy as np


an = np.linspace(0,2*np.pi,100)
plt.figure()
plt.plot(3*np.cos(an),3*np.sin(an))
plt.box()
plt.axis(False)
plt.show()


plt.figure()
plt.plot(np.arange(25),np.random.randint(45,60,25),'o-',color='purple')
plt.box()
plt.axis(False)
plt.show()



plt.figure()
plt.plot(np.arange(25),np.random.randint(45,60,25),color='purple',alpha = 0.8)
plt.box()
plt.axis(False)
plt.show()



plt.figure()
plt.arrow(0.3,0.4,0.3,0,head_width=0.05,head_length=0.07)
plt.text(0.25,0.375,'A',fontsize=18)
plt.text(0.7,0.375,'B',fontsize=18)
plt.box()
plt.axis(False)
plt.show()

