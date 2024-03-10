import matplotlib.pyplot as plt
import numpy as np

Q = np.arange(0,2*np.pi,0.1)
x = np.tan(Q)

plt.plot(x,color='red')
plt.show()