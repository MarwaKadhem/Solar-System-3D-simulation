# Solar System 3D simulation

![This is an image](solarsys_im.jpg)

General description: 3D simulation of the Solar System by propagating (Verlet-Störmer integration) the orbit of each celestial body,  in addition to the interplanetary trajectory of Pioneer 10. The initial  conditions used to solve the n-body problem are generated using the ephemeris  imported from the SPICE files (spiceypy library). 

This code was written to be as understandable as possible for begineers in astronomical programming on Python 3. 
The program is structured in 3 files:
- **Module (PropagationModule.py)** which contains all the functions needed to solve the n-body problem applied on the Solar System. This includes getting the initial conditions from NASA SPICE (Spacecraft, Planet, Instrument, C-matrix, Events ephemeris) files through the spiceypy SPK kernel. 
- **Parameters (SimulationParameters.py)** PLEASE ENTER YOUR PARAMETERS HERE!
- **Main (SolarSystemSimulation.py)** which contains the main program including the animation of the plots using Matplotlib. PLEASE RUN THIS CODE!

## Solving the N-body problem

The n-body problem is the problem of predicting the individual motions of a group of celestial objects interacting with each other gravitationally.
