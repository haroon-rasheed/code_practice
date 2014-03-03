#!/usr/bin/env python

sord="helloworld"
lt = list(sord)
print lt

def display(a,b):
    return str(a)+str(b)

print reduce(display, lt)
def get_meaning(sord):
    word = ''
    for c in sord:
      word += word.join(c) 
      print word

get_meaning(sord)
