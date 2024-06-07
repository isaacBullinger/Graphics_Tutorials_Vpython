from vpython import *
import numpy as np
from threading import Thread

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

radius=2
theta=-np.pi/2
thickness=radius/10
hand_thickness=radius/20

major_tick_length=radius/7
major_tick_thickness=2*np.pi*radius/300
major_tick_width=thickness*1.2

minor_tick_length=radius/12
minor_tick_thickness=2*np.pi*radius/600
minor_tick_width=thickness*1.2

hour_angle=np.pi/2
minute_angle=np.pi/2
second_angle=np.pi/2

minute_increment=.0001
hour_increment=minute_increment/12
second_increment=minute_increment*60

minute_hand_length=radius-major_tick_length
hour_hand_length=minute_hand_length*.75
second_hand_length=radius-minor_tick_length

face=cylinder(radius=radius,length=thickness,axis=vector(0,0,1,),pos=vector(0,0,-thickness/2),color=color.white)

hub=cylinder(axis=vector(0,0,1),radius=radius/20,length=2*thickness,color=color.red,pos=vector(0,0,-thickness/2))

hour_hand=arrow(color=color.black,length=hour_hand_length,shaftwidth=hand_thickness,pos=vector(0,0,thickness))

minute_hand=arrow(color=color.black,length=minute_hand_length,shaftwidth=hand_thickness,pos=vector(0,0,thickness))

second_hand=arrow(color=color.black,length=second_hand_length,shaftwidth=hand_thickness*.75,pos=vector(0,0,thickness))

for theta in np.linspace(0,2*np.pi,13):
    major_tick=box(axis=vector(radius*np.cos(theta),radius*np.sin(theta),0),color=color.black,length=major_tick_length,width=major_tick_width,height=major_tick_thickness,pos=vector((radius-major_tick_length/2)*np.cos(theta),(radius-major_tick_length/2)*np.sin(theta),0))

for theta in np.linspace(0,2*np.pi,61):
    minor_tick=box(axis=vector(radius*np.cos(theta),radius*np.sin(theta),0),color=color.black,length=minor_tick_length,width=minor_tick_width,height=minor_tick_thickness,pos=vector((radius-minor_tick_length/2)*np.cos(theta),(radius-minor_tick_length/2)*np.sin(theta),0))

while True:
    rate(17)
    hour_angle=hour_angle-hour_increment
    minute_angle=minute_angle-minute_increment
    second_angle=second_angle-second_increment
    hour_hand.axis=vector(hour_hand_length*np.cos(hour_angle),hour_hand_length*np.sin(hour_angle),0)
    minute_hand.axis=vector(minute_hand_length*np.cos(minute_angle),minute_hand_length*np.sin(minute_angle),0)
    second_hand.axis=vector(second_hand_length*np.cos(second_angle),second_hand_length*np.sin(second_angle),0)

