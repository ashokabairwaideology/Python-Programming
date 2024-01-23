flag = 0
num = eval(input('Enter number: '))
for i in range(2, num):
    if num % i == 0:
        flag = 1
    print(i, flag)
