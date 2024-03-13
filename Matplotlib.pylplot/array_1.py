a = []
lower = input("enter your lower range:")

upper = input("enter upper range:")

print("print number btween {} to {}".format(lower,upper))



for num in range(int(lower),int(upper) + 1):
     if num > 1:
          for i in range(2,num):
               if (num%i)==0:
                    break
               else:
                    print(num)