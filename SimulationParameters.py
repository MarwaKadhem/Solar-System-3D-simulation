"""
Creation date: May 19 2022

Author: Marwa Kadhem, 4th year student in aerospace systems engineering
at Institut Polytechnique des Sciences Avancées, France

Purpose: this program provides a 3D simulation of the Solar System by
propagating (Verlet-Störmer integration) the orbit of each celestial body, 
in addition to the interplanetary trajectory of Pioneer 10. The initial 
conditions used to solve the n-body problem are generated using the ephemeris 
imported from the SPICE files (spiceypy library). 

License: MIT License (MIT)

Copyright (C) 2022 Marwa Kadhem 
"""



import numpy as np
import spiceypy as spice


spice.tkvrsn('TOOLKIT')
spice.furnsh('de440.bsp')
spice.furnsh('p10-a.bsp')
spice.furnsh('naif0012.tls')
 

#=======================================================================================================
#                                           Simulation parameters
#=======================================================================================================

t_start = spice.spiceypy.str2et('1974 Jan 02 00:00:00.0000')        # start time of the simulation

t_end = spice.spiceypy.str2et('1990 Jan 02 00:00:00.0000')          # end time of simulation

dt = 3*24*3600                                                        # timestep

G = 6.67430e-11                                                     # Newton's Gravitational Constant m3.kg-1.s-2

num_ts = int(np.ceil(t_end/dt))                                     # number of timesteps

#=======================================================================================================

