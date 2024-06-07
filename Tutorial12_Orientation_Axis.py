from vpython import *
import numpy as np

#          height
#       ^    y
#        \   |
#         \  |
#          \ |
#           \|
# <----------|---------x length
#            |\
#            | \
#            |  \
#            |   \
#            v    z width

arrow_length=2
arrow_thickness=.02
theta=0
point_arrow_thickness=.04

x_arrow=arrow(axis=vector(1,0,0),color=color.red,length=arrow_length,shaftwidth=arrow_thickness)

y_arrow=arrow(axis=vector(0,1,0),color=color.green,length=arrow_length,shaftwidth=arrow_thickness)

z_arrow=arrow(axis=vector(0,0,1),color=color.blue,length=arrow_length,shaftwidth=arrow_thickness)

point_arrow=arrow(axis=vector(arrow_length*np.cos(theta),arrow_length*np.sin(theta),0),color=color.orange,length=arrow_length,shaftwidth=point_arrow_thickness)

while True:
    for my_angle in np.linspace(0,2*np.pi,1000):
        rate(100)
        point_arrow.axis=vector(arrow_length*np.cos(my_angle),arrow_length*np.sin(my_angle),0)
        point_arrow.length=arrow_length

    for my_angle in np.linspace(0,5*np.pi/2,1000):
        rate(100)
        point_arrow.axis=vector(arrow_length*np.cos(my_angle),0,arrow_length*np.sin(my_angle))
        point_arrow.length=arrow_length

    for my_angle in np.linspace(0,2*np.pi,1000):
        rate(100)
        point_arrow.axis=vector(0,arrow_length*np.sin(my_angle),arrow_length*np.cos(my_angle))
        point_arrow.length=arrow_length

    for my_angle in np.linspace(np.pi/2,2*np.pi,1000):
        rate(100)
        point_arrow.axis=vector(arrow_length*np.cos(my_angle),0,arrow_length*np.sin(my_angle))
        point_arrow.length=arrow_length
