#plt.bar(x,y,color=')       
#x = x-axis    y=height  of the bar


import matplotlib.pyplot as plt
import numpy as np

N= 8
x = np.array([1,2,3,4,5,6,7,8])
xx = np.array(['a', 'b', 'c', 'd', 'e', 'f','g','h'])
y = np.random.rand(N)*10

#normal bar
plt.bar(x,y)
plt.xlabel('Number')
plt.ylabel('values')
plt.title('normal bar plot')
plt.show()


#plot with color
plt.bar(x,y,color='g')
plt.xlabel('Number')
plt.ylabel('values')
plt.title('normal bar plot')
plt.show()


#plot with string
plt.bar(xx,y,color='r')
plt.xlabel('Number')
plt.ylabel('values')
plt.title('normal bar plot')
plt.show()

#combine plot
plt.bar(np.arange(26),np.random.randint(0,50,26),alpha = 0.6)
plt.xlabel('Number')
plt.ylabel('values')
plt.title('normal bar plot')
plt.show()

