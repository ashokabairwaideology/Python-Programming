def binary_to_gray(n):
      n= int(n,2)   #convert to int
      n ^= (n >> 1)



      return bin(n)[2:]



a= input("enter binary number:")
b = binary_to_gray(a)

print('gray codeword:',b)