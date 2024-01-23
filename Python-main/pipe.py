import os
fd = "GFG.txt"

# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")
# File not closed, shown in next function.





#for read or write
# os.popen(command[, mode[, bufsize]])
#
#os.popen(): This method opens a pipe to or from command. The return value can be read or written depending on whether the mode is ‘r’ or ‘w’. 