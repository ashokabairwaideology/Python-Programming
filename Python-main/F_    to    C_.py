def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

x = float(input("enter temp:"))
print(convert(x))