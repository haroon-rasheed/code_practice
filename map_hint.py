#!/usr/bin/python


class Test:
    def one(self):
        pass

    def two(self):
        pass

lt = [getattr(Test(), "one"), getattr(Test(), "two")]
print "LT =>", lt
name = Test
map(Test,lt)
