from sqlalchemy import true



num1 = int(input("Enter the num 1:"))
num2 = int(input("Enter the num 2:"))
result = str(input("choose action: Add(a),sub(s),mult(m),div(d),average(av)->"))
print("the result is :", end ="")
if result == "a":
    print(num1 + num2)
    
elif result =="s":
    print(num1-num2)
    
elif result == "m":
    print(num1*num2)
    
elif result == "av":
    print((num1+num2)/2)
    
else :
    print(num1/num2)
    
    
             

