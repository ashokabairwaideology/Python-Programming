# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


f = open("a.txt")


#read
f = open("a.txt", "r")
print(f.read())


# #different location
# f = open("D:\\myfiles\welcome.txt", "r")
# #D:\\myfiles\welcome.txt ===== for location
# print(f.read())


#read only part of file
f = open("a.txt", "r")
print(f.read(6))


#READ LINE.PY
f = open("a.txt", "r")
print(f.readline())

#read two line
f = open("a.txt", "r")
print(f.readline())
print(f.readline())

#loop line by line
f = open("a.txt", "r")
for x in f:
  print(x)
  
  
  #close file
  f = open("a.txt", "r")
print(f.readline())
f.close()


#write
f = open("a.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("a.txt", "r")
print(f.read())


#create new file
f = open("myfile.txt", "x")

f = open("myfile.txt", "w")  #if file not exist

#delete
import os
os.remove("a.txt")