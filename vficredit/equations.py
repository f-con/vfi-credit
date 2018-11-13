import numpy as np

def MPL(z,k,l, alpha):
    mpl=(1-alpha)*z*(k**(alpha))* (l**(-alpha))
    return mpl

def MPK(z,k,l, alpha):
    mpk=(alpha)*z*(k**(alpha-1))* (l**(1-alpha))
    return mpk

def util(c,gamma):
    if gamma == 1:
        return np.log(c)
    else:
        return (c ** (1-gamma))/(1-gamma)