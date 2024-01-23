a = int(input("enter no.:"))
b = int(input("enter no.:"))
c = int(input("enter no.:"))
d = int(input("enter no.:"))
e = int(input("enter no.:"))
f = int(input("enter no.:"))

if(a>b and a>c and a>d and a>e and a>f):
    print("the greatest no.: " ,a)
    
elif(b>c and b>d and b>e and b>f):
    print("the greatest no.: " ,b)
    
elif(c>d and c>e and c>f):
    print("the greatest no.: " ,c)
    
elif(d>e and d>f):
    print("the greatest no.: " ,d)
    
elif(e>f):
    print("the greatest no.: " ,e)
    
else:
    print("the greatest no.: " ,f)