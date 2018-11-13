import logging
import os
import numpy as np
import vficredit.equations as eq

class Economy(object):    
    WAGE_PARAMS = ('z','k','l','alpha')
    INTEREST_PARAMS = ('z','k','l','alpha','delta')
    AGRID_PARAMS = ('minA','nA','nAneg','maxA')
    
    def __init__(self, name = None, **kwargs):
        """
        initialize economy using default settings
        """        
        self.params = {}
        for arg in kwargs:
            self.params[arg]=kwargs[arg]
        
        
        if name is not None:            
            self.alias = name
        else:
            self.alias = hash(str(self.params))
        
        logging.info('Economy class initialized')
        
    def __str__(self):
        """
        This method summarizes all relevant information for the class as a printable string
        """
        params = []
        params.append(f"Economy:{self.alias}")
        
        for key in self.params.keys():
            params.append(f"{key}:{str(self.params[key])}")
        return os.linesep.join(params)
    
    def asset_grid(self,**kwargs):
        """ This methods creates grid points for agent assets in the economy        
        """        
        for arg in kwargs:
            if arg in self.AGRID_PARAMS:
                self.params[arg] = kwargs[arg]
        
        agrid_params = {p: self.params[p] 
                        for p in self.AGRID_PARAMS}
        minA = agrid_params['minA']
        maxA = agrid_params['maxA']
        nAneg = agrid_params['nAneg']
        nA = agrid_params['nA']
        
        negA = np.linspace(minA, 0, nAneg)
        posA = np.linspace(-negA[-2], maxA, nA-nAneg)
               
        self.a = np.concatenate((negA,posA),axis=0)
        logging.info('asset_grid initialized')
        
    def wage(self,**kwargs):
        """calculates wage
        """
        for arg in kwargs:
            if arg in self.WAGE_PARAMS:
                self.params[arg] = kwargs[arg]
        
        
        mpl_params = {p: self.params[p]
                      for p in self.WAGE_PARAMS}
        self.w = eq.MPL(**mpl_params)
        
    def interest_rate(self,**kwargs):
        """calculates deposit interest rate
        """
        for arg in kwargs:
            if arg in self.INTEREST_PARAMS:
                self.params[arg] = kwargs[arg]
        
        mpk_params = {p: self.params[p]
                      for p in self.INTEREST_PARAMS if p not in 'delta'}
        
        self.r = eq.MPK(**mpk_params) - self.params['delta']
    
    def states(self):
        pass
        
    def VFI(self):
        """ this method solves the savings (s), consumption(c) policy functions and value fsunction for all states
        """
        pass