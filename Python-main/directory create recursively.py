# Python program to explain os.makedirs() method
	
# importing os module
import os
	
# Leaf directory
directory = "Ashoka"
	
# Parent Directories
parent_dir = "home/ashoka/Documents/"
	
# Path
path = os.path.join(parent_dir, directory)
	
# Create the directory
# 'Nikhil'
os.makedirs(path)
print("Directory '% s' created" % directory)
	

	
	
	
# Leaf directory
directory = "c"
	
# Parent Directories
parent_dir = "home/ashoka/Documents/"
	
# mode
mode = 0o666
	
path = os.path.join(parent_dir, directory)
	
# Create the directory 'c'
	
os.makedirs(path, mode)
print("Directory '% s' created" % directory)
	
	
# 'Ashoka', 'a', and 'b'
# will also be created if
# it does not exists
	
# If any of the intermediate level
# directory is missing
# os.makedirs() method will
# create them
	
# os.makedirs() method can be
# used to create a directory tree
