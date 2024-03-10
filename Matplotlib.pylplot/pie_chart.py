import matplotlib.pyplot as plt


labels='A','B','C','D','E','F'
sizes = [15,20,30,40,50,60]
alp = (0.9,0.9,0.9,0,0.9,0.9)




plt.figure()
plt.title('pie plot')
plt.pie(sizes,labels=labels,counterclock = False, autopct='%1.1f%%',shadow=True)
plt.axis('equal')
plt.show()

plt.figure()
plt.title('Bar plot')
plt.bar(labels,sizes,color='red')
plt.show()

plt.figure()


plt.subplot(121)
plt.pie(sizes,labels=labels,counterclock=False,autopct='%1.1f%%',shadow=True)
plt.axis('equal')



plt.subplot(122)
plt.title('Bar plot')
plt.bar(labels,sizes,color='yellow')
plt.show()