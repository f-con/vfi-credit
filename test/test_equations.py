import vficredit.equations as eq
import numpy as np

def test_MPL():
    assert eq.MPL(1.,1.,1.,1.) == 0.
    assert eq.MPL(1.,1.,1.,0.) == 1.
    assert eq.MPL(0.,1.,1.,1.) == 0.
    assert eq.MPL(0.,1.,1.,0.) == 0.   
    assert eq.MPL(0.5,1.,1.,0.5) == 0.25
    assert eq.MPL(0.5,1.,1.,0) == 0.5
    
def test_MPK():
    assert eq.MPK(1.,1.,1.,1.) == 1.
    assert eq.MPK(1.,1.,1.,0.) == 0.
    assert eq.MPK(0.5,1.,1.,0.5) == 0.25
    assert eq.MPK(0.5,1.,1.,1.) == 0.5

def test_util():
    assert eq.util(1.,0.) == 1
    assert eq.util(1.,1.) == 0
    assert eq.util(1.,2.) == -1
    assert eq.util(1.,3.) == -0.5
    
