import sys

class T(object):
	a = 1


class A(T):
	pass

class B(T):
	a = 2

class C(A,B):
	pass

c = C()
print super(C, c).a
print A.a
