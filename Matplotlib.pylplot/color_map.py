#matplotlib.pyplot.imshow()

import matplotlib.pyplot as plt
import numpy as np

a = np.array([[2,4,2,8],[7,6,8,4],[9,8,7,9],[4,8,8,9],[6,9,7,4]])
[m,n] = np.shape(a)

#color map using matrix
plt.figure()
plt.imshow(a, alpha=0.8)
plt.xticks(np.arange(n))
plt.yticks(np.arange(m))
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('color maps')


#color map using matrix
plt.figure()
plt.imshow(a, alpha=0.8, cmap='twilight_r')
plt.xticks(np.arange(n))
plt.yticks(np.arange(m))
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('color maps')



#color map using matrix
plt.figure()
plt.imshow(a, alpha=0.8,cmap='rainbow_r')
plt.xticks(np.arange(n))
plt.yticks(np.arange(m))
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('color maps')





#color map using matrix
plt.figure()
plt.imshow(a, alpha=0.8,cmap='jet_r')
plt.xticks(np.arange(n))
plt.yticks(np.arange(m))
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('color maps')


#color map using matrix
plt.figure()
plt.imshow(a, alpha=0.8,cmap='Purples_r')
plt.xticks(np.arange(n))
plt.yticks(np.arange(m))
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('color maps')
63.
plt.show()