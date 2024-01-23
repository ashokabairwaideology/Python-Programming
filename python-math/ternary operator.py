# Program to demonstrate conditional operator
a = int(input("enter a:"))
b =  int(input("enter b:"))

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print("minimum",min)

max = a if a > b else b

print("maximum",max)


'''[on_true] if [expression] else [on_false] 
'''