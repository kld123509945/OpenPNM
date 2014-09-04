"""
===============================================================================
module __FickianDiffusion__: Diffusive mass transfer
===============================================================================

"""
import scipy as sp
import OpenPNM
from .__GenericLinearTransport__ import GenericLinearTransport

class FickianDiffusion(GenericLinearTransport):
    r'''
    A subclass of GenericLinearTransport to simulate binary diffusion.  The 2
    main roles of this subclass are to set the default property names and to
    implement a method for calculating the effective diffusion coefficient
    of the network.

    Examples
    --------
    >>> pn = OpenPNM.Network.TestNet()
    >>> geo = OpenPNM.Geometry.TestGeometry(network=pn,pores=pn.pores(),throats=pn.throats())
    >>> phase1 = OpenPNM.Phases.TestPhase(network=pn)
    >>> phys1 = OpenPNM.Physics.TestPhysics(network=pn, phase=phase1,pores=pn.pores(),throats=pn.throats())
    >>> alg = OpenPNM.Algorithms.FickianDiffusion(network=pn, phase=phase1)
    >>> BC1_pores = pn.pores('top')
    >>> alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.6, pores=BC1_pores)
    >>> BC2_pores = pn.pores('bottom')
    >>> alg.set_boundary_conditions(bctype='Dirichlet', bcvalue=0.4, pores=BC2_pores)
    >>> alg.run()
    >>> alg.update_results()
    >>> Deff = round(alg.calc_eff_diffusivity(), 3)
    >>> print(Deff) #unless something changed with our test objects, this should print "0.025"
    0.025
    
    
    '''

    def __init__(self,**kwargs):
        r'''
        
        '''
        super(FickianDiffusion,self).__init__(**kwargs)
        self._logger.info('Create '+self.__class__.__name__+' Object')
        
    def run(self,conductance='diffusive_conductance',quantity='mole_fraction',**params):
        r'''
        '''  
        self._logger.info("Setup "+self.__class__.__name__)   
        super(FickianDiffusion,self).setup(conductance=conductance,quantity=quantity)
        
        super(GenericLinearTransport,self).run()
        
    def calc_eff_diffusivity(self):
        r'''
        '''
        D_normal = self._calc_eff_prop()
        self._eff_property = D_normal/sp.mean(self._phase['pore.molar_density'])
        return self._eff_property
        



