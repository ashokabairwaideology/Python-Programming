#pyplot.streamplot()

import matplotlib.pyplot as plt
import numpy as np

#building a sample meshgrid
w = 6
y ,x = np.mgrid[-w:w:100j, -w:w:100j]
u = -1 -x**2 +y
v = 1 + x - y**2
speed  = np.sqrt(u**2 + v**2)
plt.figure()

plt.figure()
plt.streamplot(x,y,u,v)
plt.title("basic")
plt.show()


plt.figure()
plt.streamplot(x,y,u,v,linewidth=2.0)
plt.title("basic with ,linewidth")
plt.show()

plt.figure()
plt.streamplot(x,y,u,v,linewidth=0.5,color='g')
plt.title("color")
plt.show()