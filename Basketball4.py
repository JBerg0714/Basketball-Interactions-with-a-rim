#LAB

from __future__ import division, print_function
from visual import *
import numpy as np
scene.forward = vector(0,0,1)
scene.up = vector(0,-1,0)
scene.width=800
scene.height=600


#CONSTANTS 
m_1 = 2
m_2 = 1
l_1 = 2
l_2 = 1
phi_1 = 20
phi_2 = 30  
Rmass_1=0.02
Rmass_2=0.01
r_1 = vector(l_1*np.sin(phi_1), l_1*np.cos(phi_1),0)
r_2 = vector((l_1*np.sin(phi_1))+(l_2*np.cos(phi_2)),(l_1*np.cos(phi_1))+(l_2*np.sin(phi_2)),0)




#Visual 
mass_1 = sphere(pos=r_1, radius=Rmass_1, color=color.red)
mass_2 = sphere(pos=r_2, radius=Rmass_2, color=color.red)
#ceiling = box(pos=vector(0,0,0), length=4, width=1, height=1, color=color.white)
rod_1 = box(pos=vector(0,0,0), axis=r_1, color=color.white)
rod_2 = box(pos=r_1, axis=r_2-r_1, color=color.white) 




dt = 0.01
t=0

while True: 
    
    t = t+dt 
    phi_dot_1 = phi_dot_1 + phi_doubledot_1*dt
    phi_dot_2 = phi_dot_2 + phi_doubledot_2*dt
    phi_1 = phi_1 + phi_dot_1*dt
    phi_2 = phi_2 + phi_dot_2*dt 


