#!/usr/bin/python
'''
A MonkeyPatch is a piece of Python code which extends or modifies other code at
runtime (typically at startup). MonkeyPatching? would be the practice of
writing, or running, a monkeypatch.
'''


class Monkey:
    def speak(self):
        print repr("I'm a Monkey")

      
def monkey_patch_fun():
    print repr("I'm a Dog")

m1 = Monkey()
m1.speak()
m1.speak = monkey_patch_fun
m1.speak()

