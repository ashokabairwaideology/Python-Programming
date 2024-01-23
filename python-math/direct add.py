def AddIt(Value1, Value2):
    
    return (a+b,a-b,a*b,a/b)
#for input from user

a = int(input("entre 1st no. :  "))
b = int(input("entre 2nd no. :  "))
result = AddIt(a,b)
print(result)




#condition for true false
print("adds :",(AddIt(3,4)==AddIt(5,2)))
