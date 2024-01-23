# Python3 program to demonstrate global() function
  
# global variable
name = 'Ashok'
  
print('Before modification:', name)
  
# Calling global()
globals()['name'] = 'Ashoka bairwa'   #we can change variable in global function

print('After modification:', name)