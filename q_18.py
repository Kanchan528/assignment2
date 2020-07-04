# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

data={
    'name':'Kanchan',
    'age':16,
}
#serializing JSON
json_string = json.dumps(data, indent=3)
print(type(json_string))
print(json_string)

#deserializing json back to python

json_data = json.loads(json_string)
print(type(json_data))
print(json_data)