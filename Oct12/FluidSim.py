"""
A module for simulating fluid flow between tanks using pipes.

"""

import numpy as np

class Fluid:
    """
    A class describing a typical fluid
    """

    def __init__(self, density, viscosity):
        """
        Initialize the fluid with density and viscosity

        Parameters
        ----------
        density : float
            The density of the fluid [kg/m^3]
        viscosity : float
            The viscosity of the fluid [kg/m/s]
        """
        self.density = density
        self.viscosity = viscosity



class Pipe:
    """
    A class describing a pipe with dimensions
    """

    def __init__(self, length, diameter, fluid, friction_factor=0.0119):
        """
        Intiialize a pipe of a certain length and diameter

        Parameters
        ----------
        length : float
            The length of the pipe [m] 
        diameter : float
            The diameter of the pipe [m]
        fluid : Fluid
            The fluid flowing through the pipe
        friction_factor : float
            The friction factor of the pipe
            The default value is 0.0119 for a smooth pipe
        """

        self.length = length
        self.diameter = diameter
        self.fluid = fluid
        self.friction_factor = friction_factor
        self.cross_sectional_area = np.pi * (diameter / 2)**2

    def pressure_drop(self, Q):
        """
        Calculate the pressure drop across the pipe
        
        Parameters
        ----------
        Q : float
            The volumetric flow rate through the pipe [m^3/s]
        """
        return 0
    
    def flow_rate(self, deltaP):
        """
        Calculate the flow rate through the pipe
        
        Parameters
        ----------
        deltaP : float
            The pressure drop across the pipe [Pa]
        """
        if(deltaP < 0):  # edge case -- we don't want back flow
            return 0
        
        Vavg = self.diameter**2 * deltaP / (32 * self.fluid.viscosity * self.length)
        Q = Vavg * self.cross_sectional_area

        # Assuming non-turbulent flow
        return Q
    
    def isTurbulent(self, Q):
        """
        Determine if the flow through the pipe is turbulent

        Parameters
        ----------
        Q : float
            The volumetric flow rate through the pipe [m^3/s]
        """

        return False
    

class Tank:
    """
    A class describing a tank with dimensions
    """

    def __init__(self, height, diameter, fluid, fluid_height, inlet_height, outlet_height):
        """
        Intiialize a tank of a certain height and diameter

        Parameters
        ----------
        height : float
            The height of the tank [m] 
        diameter : float
            The diameter of the tank [m]
        fluid : Fluid
            The fluid in the tank
        fluid_height : float
            The height of the fluid in the tank [m]
        inlet_height : float
            The height of the inlet pipe [m]
        outlet_height : float
            The height of the outlet pipe [m]
        """

        self.height = height
        self.diameter = diameter
        self.fluid = fluid
        self.fluid_height = fluid_height
        self.inlet_height = inlet_height
        self.outlet_height = outlet_height
        self.tank_area = np.pi * (diameter / 2)**2


    def outlet_pressure(self):
        """
        Calculate the pressure at the outlet of the tank
        """
        dHeight = self.fluid_height - self.outlet_height
        if(dHeight < 0):  # edge case where fluid is below the outlet
            dHeight = 0
        return self.fluid.density * dHeight * 9.81
    
    def inlet_pressure(self):
        """
        Calculate the pressure at the inlet of the tank
        """
        dHeight = self.fluid_height - self.inlet_height
        if(dHeight < 0):
            dHeight = 0
        return self.fluid.density * dHeight * 9.81
    
    def drain_tank(self, V):
        """
        Drain the tank of a certain volume

        Parameters
        ----------
        V : float
            The volume to drain from the tank [m^3]
        """
        dHeight = V / self.tank_area
        self.fluid_height -= dHeight
    
    def fill_tank(self, V):
        """
        Fill the tank with a certain volume

        Parameters
        ----------
        V : float
            The volume to fill the tank with [m^3]
        """

        dHeight = V / self.tank_area
        self.fluid_height += dHeight