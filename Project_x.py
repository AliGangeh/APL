import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# A class which Details all aspects of a rocket
class Rocket:

    # constructor
    def __init__(self, mass, mass_flow, burntime, isp, cd, diameter):
        # user defined rocket
        self._mass = mass
        self._mass_flow = mass_flow
        self._burntime = burntime
        self._isp = isp
        self._cd = cd
        self._d = diameter
        
        # Define area of rocket
        self._area = np.pi * (self._d/2)**2

    def altitude(self):
        
