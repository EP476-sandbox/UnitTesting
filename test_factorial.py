from nose.tools import *
from factorial import factorial

def test_factorial0():
    # test edge 0
    obs = factorial(0)
    assert_equal(1, obs)

def test_factorial4():
    # test 4
    obs = factorial(4)
    assert_equal(24, obs)

@raises(Exception)
def test_factorialm1():
    # test edge -1
    obs = factorial(-1)
