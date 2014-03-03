# Base class definition
class ClassA(object):
	def __init__(self):
		print("Initializing A")
		# hoping that this function is called by this class's printFnX
	
	def fnX(self, x):
		return x**2
		__fnX = fnX

	def printFnX(self, x):
		print("ClassA:", self.__fnX(x))


# Inherits from ClassA above
class ClassB(ClassA):
	def __init__(self):
		print("initizlizing B")

	def fnX(self, x):
		return 2*x

	def printFnX(self, x):
		print("ClassB:", self.fnX(x))
		ClassA.printFnX(self,x)

bx = ClassB()
#bx.printFnX(3)

d1 = {}
print "Len =>", len(d1)

d2 = { "one" : "11" }
try:
    var = d2['tw']
except KeyError as e:
    print "Key Fail"
