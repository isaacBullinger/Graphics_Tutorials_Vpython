from vpython import *
from threading import Thread
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

thermometer_height=50
speed_1=500
speed_2=1000

def thermometer_1(speed):
    while True:
        for my_length in np.linspace(1,thermometer_height,speed):
            rate(250)
            mercury_column_1.length=my_length
        for my_length in np.linspace(thermometer_height,1,speed):
            rate(250)
            mercury_column_1.length=my_length

def thermometer_2(speed):
    while True:
        for my_length in np.linspace(1,thermometer_height,speed):
            rate(250)
            mercury_column_2.length=my_length
        for my_length in np.linspace(thermometer_height,1,speed):
            rate(250)
            mercury_column_2.length=my_length

glass_bulb_1=sphere(pos=vector(-5,0,0),radius=4,color=color.white,opacity=.25)
glass_rod_1=cylinder(pos=vector(-5,0,0),radius=2,color=color.white,opacity=.25,axis=vector(0,thermometer_height,0))
mercury_dot_1=sphere(pos=vector(-5,0,0),radius=3,color=color.red,opacity=.75)
mercury_column_1=cylinder(pos=vector(-5,0,0),radius=1,axis=vector(0,thermometer_height,0),color=color.red,opacity=.75)
glass_tip_1=sphere(radius=2,color=color.white,pos=vector(-5,thermometer_height,0),opacity=.25)

glass_bulb_2=sphere(pos=vector(5,0,0),radius=4,color=color.white,opacity=.25)
glass_rod_2=cylinder(pos=vector(5,0,0),radius=2,color=color.white,opacity=.25,axis=vector(0,thermometer_height,0))
mercury_dot_2=sphere(pos=vector(5,0,0),radius=3,color=color.red,opacity=.75)
mercury_column_2=cylinder(pos=vector(5,0,0),radius=1,axis=vector(0,thermometer_height,0),color=color.red,opacity=.75)
glass_tip_2=sphere(radius=2,color=color.white,pos=vector(5,thermometer_height,0),opacity=.25)

thermometer_1_thread=Thread(target=thermometer_1,args=(speed_1,))
thermometer_2_thread=Thread(target=thermometer_2,args=(speed_2,))
thermometer_1_thread.daemon=True
thermometer_2_thread.daemon=True
thermometer_1_thread.start()
thermometer_2_thread.start()
