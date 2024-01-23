# Python program to explain os.mkdir() method

# importing os module
import os

# Directory
directory = "Ashoka"

# Parent Directory path
parent_dir = "/home/ashoka/Documents/"

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)






# Directory
directory = "bairwa"

# Parent Directory path
parent_dir = "/home/ashoka/Documents/"

# mode
mode = 0o666

# Path
path = os.path.join(parent_dir, directory)

# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
