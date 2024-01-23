# Python program to illustrate
# Finding common member in list
# using 'in' operator
list1 = [1, 9, 3, 4, 6]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping same number")
    else:
        print("not overlapping same number")