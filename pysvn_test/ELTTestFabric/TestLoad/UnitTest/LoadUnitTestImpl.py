import abc
import unittest

class LoadUnitTestImpl(unittest.TestCase, object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def runTest(self):
        pass

    @abc.abstractmethod
    def set_up(self):
        pass
    
    @abc.abstractmethod
    def execute_tc(self):
        pass

    @abc.abstractmethod
    def verify(self):
        pass

    @abc.abstractmethod
    def tearDown(self):
        pass

    def dump_vars(self):
        for k,v in self.__dict__.iteritems():
            print "Var =>", k, "Value =>", v

    def shortDescription(self):
        """"
        Enable __str__() in your implementation class, rest will go automatically
        """
        #print self
        pass
