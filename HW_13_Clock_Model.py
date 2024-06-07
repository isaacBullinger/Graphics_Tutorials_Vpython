from vpython import *
import numpy as np

#          height
#       ^    y
#        \   |
#         \  |
#          \ |
#           \|
# <--------------------x length
#            |\
#            | \
#            |  \
#            |   \
#            v    z width

radius=2
thickness=radius/10
major_tick_length=radius/7
major_tick_thickness=2*np.pi*radius/300
major_tick_width=thickness*1.2

minor_tick_length=radius/12
minor_tick_thickness=2*np.pi*radius/600
minor_tick_width=thickness*1.2

for theta in np.linspace(0,2*np.pi,13):
    major_tick=box(axis=vector(radius*np.cos(theta),radius*np.sin(theta),0),color=color.black,length=major_tick_length,width=major_tick_width,height=major_tick_thickness,pos=vector((radius-major_tick_length/2)*np.cos(theta),(radius-major_tick_length/2)*np.sin(theta),0))

for theta in np.linspace(0,2*np.pi,61):
    minor_tick=box(axis=vector(radius*np.cos(theta),radius*np.sin(theta),0),color=color.black,length=minor_tick_length,width=minor_tick_width,height=minor_tick_thickness,pos=vector((radius-minor_tick_length/2)*np.cos(theta),(radius-minor_tick_length/2)*np.sin(theta),0))
face=cylinder(radius=radius,length=thickness,axis=vector(0,0,1,),pos=vector(0,0,-thickness/2),color=color.white)

while True:
    pass
