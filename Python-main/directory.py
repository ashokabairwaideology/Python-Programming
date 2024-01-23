bio = {"name":  " My name is ashoka",
       "qualify": "Btech",
       "age": "my age is 22year",
       "phone": "9053189901",
       "address": "haryana"
       }
print(bio)
print(bio["name"])
print(bio["phone"])

print(bio.get("address"))

'''add new term'''
term = input("\nWhat term do you want me to add?: ")
print(bio)
if term not in bio:
    definition = input("\nWhat's the definition?: ")
bio[term] = definition
print("\n", term, "has been added.\n",bio)


'''delete a term'''

term = input("What term do you want me to delete?: ")
if term in bio:
    del bio[term]
print("\nOkay, I deleted\n", bio)
