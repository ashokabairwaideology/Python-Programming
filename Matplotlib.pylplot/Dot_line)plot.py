#plt.plot(x,y,'o-) 
'''x = names/numeric
   y = length of bar
   o- or .-  = instruction of dot line
   go- = dot with green color'''


import matplotlib.pyplot as plt
import numpy as np

x =  np.linspace(0.0,0.5)
y = x*x

#default plot
plt.subplot(3,1,1)
plt.plot(x,y,'o-')
plt.title('Dot-line plot')
plt.ylabel('square')
plt.xlabel('numbers')
plt.show()


#samller dot
plt.subplot(3,1,2)
plt.plot(x,y,'.-')
plt.title('smaller Dot-line plot')
plt.ylabel('square')
plt.xlabel('numbers')
plt.show()

#color change
plt.subplot(3,1,3)
plt.plot(x,y,'g.-')
plt.title('Dot-linr plot')
plt.ylabel('square')
plt.xlabel('numbers')
plt.show()