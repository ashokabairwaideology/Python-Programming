import json
x = '{"name":"ashoka","age":23,"gender":"male"}'

y = json.loads(x)

print(y["age"])
print(y["gender"])
print(y["name"])

y = json.dumps(x)
print(y)


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))
