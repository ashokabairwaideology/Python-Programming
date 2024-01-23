# Python program to demonstrate nested ternary operator
a, b = 10, 20

print ("Both a and b are equal" if a == b else "a is greater than b"
		if a > b else "b is greater than a")







'''second'''

a=52
b=7

# [statement_on_True] if [condition] else [statement_on_false]

print(a,"is greater") if (a>b) else print(b,"is Greater")








'''third'''

	
# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note : it doesn't
# work if a is 0.
min = a < b and a or b

print(min)
