#dot plot

import matplotlib.pyplot as plt

#plot using the dot() function, which takes x and y data
plt.plot([7,6,8,1,4,2,5,9],'ro') #r mean red ,o mean dot

#axis labels
plt.xlabel('Number')
plt.ylabel('value')

#fig name 
plt.title('Dot plot')

#show the plot
plt.show()

