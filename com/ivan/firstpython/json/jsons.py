import json

# serialize an object to string
print(json.dumps({'age': 2, 'name': "John"}))

# deserialize an object from string
user_string = '{"age": 22, "name": "Jane"}'
user = json.loads(user_string)
print(type(user))
print(user['name'])
print(user['age'])

