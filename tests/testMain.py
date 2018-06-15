"""
Authors: Stefan Strang
University of Freiburg - 2018

"""

"""from LTL.tools.ltlToPred import translate
from LTL.tools.getInp import getInp
from LTL.tools.lf import lf
from LTL.tools.toPnfObjects import toPnf
from LTL.tools.derivative import derivatives"""
import doctest
from LTL.tests.unitTests import test
from LTL.tests.unitTest2 import test2
from LTL.tests.unitTestDef8ex2 import testgfp
from LTL.tests.testDef10 import test10



def testMain():
    """doctest.testmod()
    # testing the strucutre
    doctest.testfile("../tools/getInp.py")
    doctest.testfile("../tools/ltlToPred.py")
    doctest.testfile("../tools/toPnfObjects.py")
    # testing linear factors
    doctest.testfile("../tools/lf.py")
    doctest.testfile("../tests/unitTestDef8ex2.py")
    test()
    test2()
    testgfp()"""
    # testing partial derivatives
    test10()


