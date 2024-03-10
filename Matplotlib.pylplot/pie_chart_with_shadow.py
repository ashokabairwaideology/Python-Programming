import matplotlib.pyplot as plt 
labels= 'a', 'b', 'c', 'd', 'e', 'f'
sizes = [12,23,24,25,26,27]
explode = (0,0.1,0,0,0,0)


plt.figure()
plt.pie(sizes,labels=labels,explode=explode,autopct='%1.1f%%',shadow=True)
plt.axis('equal')
plt.show()