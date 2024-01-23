a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
n = int(input("enter the range:"))


print(a,b,end=" ")

while(n-2):
      c = a+b 
      a=b
      b=c
      print(c,end=" ")
      n= n-1