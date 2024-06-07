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

thermometer_height=50

glass_bulb=sphere(radius=4,color=color.white,opacity=.25)
glass_rod=cylinder(radius=2,color=color.white,opacity=.25,axis=vector(0,thermometer_height,0))
mercury_dot=sphere(radius=3,color=color.red,opacity=.75)
mercury_column=cylinder(radius=1,axis=vector(0,thermometer_height,0),color=color.red,opacity=.75)
glass_tip=sphere(radius=2,color=color.white,pos=vector(0,thermometer_height,0),opacity=.25)

for tick in np.linspace(1,thermometer_height,100):
    cylinder(radius=1,length=.2,pos=vector(0,tick,0),color=color.white,axis=vector(0,1,0),opacity=.25)

while True:
    for my_length in np.linspace(1,thermometer_height,1000):
        rate(250)
        mercury_column.length=my_length
    for my_length in np.linspace(thermometer_height,1,1000):
        rate(250)
        mercury_column.length=my_length
