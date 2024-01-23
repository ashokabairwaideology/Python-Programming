'''
»» append(): Adds a new entry to the end of the list.
»» clear(): Removes all entries from the list.
»» copy(): Creates a copy of the current list and places it in a new list.
»» extend(): Adds items from an existing list and into the current list.
»» insert(): Adds a new entry to the position specified in the list.
»» pop(): Removes an entry from the end of the list.
»» remove(): Removes an entry from the specified position in the list.
'''

# list = ["1:ashoka","2:name","3:address"]
# print(list)
# for item in list:
#     print(item)
    
    
    #sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#add

thislist = ["apple", "banana", "cherry"]
thislist.append("ashoka")
print(thislist)

#merge


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)