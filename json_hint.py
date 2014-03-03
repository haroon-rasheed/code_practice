#!/usr/bin/python

dt = {
        "firstName": "John",
        "lastName": "Smith",
        "age": 25,
        "address": {
                    "streetAddress": "21 2nd Street",
                    "city": "New York",
                    "state": "NY",
                    "postalCode": 10021
                },
        "phoneNumber": [
                    {
                                    "type": "home",
                                    "number": "212 555-1234"
                                },
                    {
                                    "type": "fax",
                                    "number": "646 555-4567"
                                }
                ]
}

#print "Addr =>", dt["address"]
#print "Ph =>", dt["phoneNumber"]
import json
print "Creating JSON from DICT"
js_data = json.dumps(dt)
print js_data

class one(object):
    def __init__(self, name, choice):
        self.name = name
        self.choice =  choice

    def __call__(self):
        print("in _-call__")

    def __str__(self):
        print("Type = ", type(self.__class__.__name__))
        return repr(self.__class__.__name__)

    def get_it(self):
        print("In Base CLass")
        print("Base", self.get_it.__name__)        # How to print a method name

def serialize_obj(obj):
  dt = { '__class__':obj.__class__.__name__, '__module__':obj.__module__}
  dt.update(obj.__dict__)
  print "ohaaiyyyo", dt 
  return dt


obj = one("harppn", "sv")
print "Module", obj.__module__
d = { '__class__':obj.__class__.__name__, '__module__':obj.__module__}
d.update(obj.__dict__)
print "DDDD ===>", d
"""
print "obj dict", obj.__dict__
print "dict", d
print "converting a python object in to json object"
print json.dumps(obj, default=serialize_obj)
print "two", json.dumps(obj.__dict__)
"""
module = d['__module__']
module = __import__(module)
class_name = d['__class__']
print module
class_ = getattr(module,class_name)
print "KLASS ==>", class_ 
args = dict( (key.encode('ascii'), value) for key, value in d.items())
print "ARGS ==", args
inst = class_(**args)
print "INST===>", inst
