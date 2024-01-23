# Hero's Inventory
# Demonstrates tuple creation
# create an empty tuple
'''
inventory = ()
# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")
input("\nPress the enter key to continue.")

#Python Programming for the Absolute Beginner, Third Edition
# create a tuple with some items
inventory = ("sword",
"armor",
"shield",
"healing potion")
# print the tuple
print("\nThe tuple inventory is:")
print(inventory)
# print each element in the tuple
print("\nYour items:")
for item in inventory:
    print(item)
input("\n\nPress the enter key to exit.")

'''




# concatenate two tuples
chest = ("gold", "gems")
print("You find a chest.")
print(chest)


#Python Programming for the Absolute Beginner, Third Edition
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)