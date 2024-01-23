
my_list1 =[1, 2, 3]
my_list2 =[4, 9, 0]
combo_list = my_list1 + my_list2

print(combo_list)


my_nested_list = [my_list1, my_list2]
print(my_nested_list)

alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)

beta_list = ['apple', 'banana', 'orange']
beta_list[1] = 'pear'
print(beta_list)

for x in range(1,5):
    beta_list += ['fruit']
    print(beta_list);


num = [x ** 2 for x in range(100) if x % 2 == 0]
print(num)
