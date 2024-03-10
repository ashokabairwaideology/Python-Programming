#plt.scatter(x,y, alpha=0.8,s = area)
#x,y =data point in array
#alpha = 0.8 is (0 for transparent and 1 for opaque)

#s = area (size of each point in term of area)
#c = color


import matplotlib.pyplot as plt
import numpy as np


N = 50
x= np.random.rand(N)
y = np.random.rand(N)*10

#random color for points in the scatter plot
colors = np.random.rand(N)

#area of circle ,vector of length N
area = (30 * np.random.rand(N))**2  


#a normal scatter plot with default feature
plt.scatter(x,y,alpha=0.8)
plt.xlabel('Number ')
plt.ylabel('Value')
plt.title('Normal scatter plot')
plt.subplot(2,4,1)

#scatter plot with differnt color plot
plt.scatter(x,y,c=colors , alpha=0.8)
plt.xlabel('Number ')
plt.ylabel('Value')
plt.title('differnt color')
plt.subplot(2,4,2)

#scatter plot with different size
plt.scatter(x,y,s=area ,alpha = 0.8)
plt.xlabel('Number ')
plt.ylabel('Value')
plt.title('different size')
plt.subplot(2,4,3)

#combine plot with different
plt.scatter(x,y,c=colors ,s=area ,alpha = 0.8)
plt.xlabel('Number ')
plt.ylabel('Value')
plt.title('combine plot')
plt.subplot(2,4,5)
plt.show()
