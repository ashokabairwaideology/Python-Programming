total = int(input("enter total:"))
num   = int(input("Enter num  :"))
percentage = num/total * 100
if(num>total):
    print("not valid:",num)
    
elif(percentage>90):
    print("you got outstanding:",percentage)
    
elif(percentage>80 and percentage<90):
    print("you got excellent:",percentage)
    
elif(percentage>70 and percentage<80):
    print("you got very good:",percentage)
    
elif(percentage>60 and percentage<70):
    print("you got good:",percentage)
    
elif(percentage>50 and percentage<60):
    print("average:",percentage)
    
else:
    print("FAIL------------:",percentage)