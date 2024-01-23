x = lambda a : a + 10
print(x(5))

x = lambda a, b : a ** b
print(x(51, 6))

x = lambda a,b : a ** b
print(x(2,365))

#table

# for b in range(11):
#     for a in range(11):
#         y = lambda a, b : a * b 
#         print("\t",y(a,b),"\n")
    
    
    
    
    #define class
    
class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)