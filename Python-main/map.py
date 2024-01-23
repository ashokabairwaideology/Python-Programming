def square(num):
    return num**2

mynums = [1,2,3,4,5]

sqrnum = list(map(square,mynums))

print(sqrnum)