'''-s,_s   is the name of the square point
   -^,_^   is the name of the triangle point
   --,_--  is the name of the dash pattern
   -*,_*   is the name of the star pattern
   
   
   '''

import matplotlib.pyplot as plt 
import numpy as np

t = np.arange(0,8,0.4)


 #figure 1 square point
plt.figure()
plt.plot(t,t,'rs',t,t**2, 'bs',t,t*3,'ys',t,t+t,'gs')
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('square point')
plt.show()


 #figure 2 triangle point
plt.figure()
plt.plot(t,t,'r^',t,t**2, 'b^',t,t*3,'y^',t,t+t,'g^')
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('square point')
plt.show()



 #figure 3 dash point
plt.figure()
plt.plot(t,t,'r--',t,t**2, 'b--',t,t*3,'y--',t,t+t,'g--')
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('square point')
plt.show()



 #figure 4 star point
plt.figure()
plt.plot(t,t,'r*',t,t**2, 'b*',t,t*3,'y*',t,t+t,'g*')
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('square point')
plt.show()


 #figure 5 combines
plt.figure()
plt.plot(t,t,'r*',t,t**2, 'b--',t,t*3,'y^',t,t+t,'gs')
plt.xlabel('numbers')
plt.ylabel('values')
plt.title('square point')
plt.show()