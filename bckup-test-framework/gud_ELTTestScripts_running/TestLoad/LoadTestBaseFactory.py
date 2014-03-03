#from ELTTestBaseFactory import ELTTestBaseFactory
#from TestLoad.UnitTest.LoadUnitTestBase import LoadUnitTestBase

"""
class ELTTestBaseFactory:
	pass

class LoadUnitTestBase:
	pass
"""
#@ELTTestBaseFactory.registersub
class LoadTestBaseFactory(ELTTestBaseFactory):

	def get_unittest(self, test_case):
		return LoadUnitTestBase(test_case)

	def get_regntest(self, test_case):
		return LoadRegnTestBase(test_case)

