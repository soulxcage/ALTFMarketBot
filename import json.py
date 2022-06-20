import json

with open("generated.json","r") as json_file:
    a=json.load(json_file)

del a["name"]["Kristin Baldwin"]
print(a)
