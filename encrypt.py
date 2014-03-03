#!/usr/bin/python

import hashlib, uuid
salt = uuid.uuid4().hex
password = "test"
hashed_password = hashlib.sha512(password + salt).hexdigest()
hashed_password1 = hashlib.sha512(password + salt).hexdigest()
print hashed_password
print hashed_password1
