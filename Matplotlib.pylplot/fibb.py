N = int(input("enter your number:"))
print(N)
fibb = [0,1]

for k in range(N-2):
     fibb_next = fibb[k+1] + fibb[k]
     fibb.append(fibb_next)


print(fibb)

