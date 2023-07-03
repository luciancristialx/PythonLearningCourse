import json

# x = { "name": "alex", "age": 120, "job": "developer" }
x = '{ "name": "alex", "age": 120, "job": "developer" }'

# y = json.dumps(x)
y = json.loads(x)

print(y["name"])
