# Python program to explain os.remove() method
	
# importing os module
import os
	
# File name
file = 'a.out'
	
# File location
location = "home/ashoka/Documents/"
	
# Path
path = os.path.join(location, file)
	
# Remove the file
# 'file.txt'
os.remove(path)
