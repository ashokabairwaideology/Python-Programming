y = pow(2,6)
print(y)

#math
import math

z = math.sqrt(64)
c = math.sqrt(625)

print(z)
print(c)


#square
a = input("enter first no. : ")
b = input("enter second no : ")

x = pow(int(a),int(b))

print(x)


#pi
import math

x = math.pi

print(x)



#or'
num = int(input("Enter num:"))
pow = int(input("Enter power"))

a = num
for i in range(0,pow-1):
    a = a*num
print("result:",a)