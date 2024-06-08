from vpython import *
import numpy as np
import time

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
my_time=time.localtime(time.time())

major_tick_length=radius/7
major_tick_thickness=2*np.pi*radius/300
major_tick_width=thickness*1.2

minor_tick_length=radius/12
minor_tick_thickness=2*np.pi*radius/600
minor_tick_width=thickness*1.2

minute_increment=.0001
hour_increment=minute_increment/12
second_increment=minute_increment*60

minute_hand_length=radius-major_tick_length
hour_hand_length=minute_hand_length*.75
second_hand_length=radius-minor_tick_length

face=cylinder(
    radius=radius,
    length=thickness,
    axis=vector(0,0,1,),
    pos=vector(0,0,-thickness/2),
    color=color.cyan)

hub=cylinder(
    axis=vector(0,0,1),
    radius=radius/20,
    length=2*thickness,
    color=color.red,
    pos=vector(0,0,.01-thickness/2))

text_height=radius/4
my_label=text(
    text='Texas Time',
    align='center',
    color=color.orange,
    height=text_height,
    pos=vector(0,1.1*radius,-thickness/2),depth=thickness)

hour_hand=arrow(
    color=color.red,
    length=hour_hand_length,
    shaftwidth=hand_thickness,
    pos=vector(0,0,thickness))

minute_hand=arrow(
    color=color.red,
    length=minute_hand_length,
    shaftwidth=hand_thickness,
    pos=vector(0,0,thickness))

second_hand=arrow(
    color=color.red,
    length=second_hand_length,
    shaftwidth=hand_thickness*.65,
    pos=vector(0,0,thickness))

for theta in np.linspace(0,2*np.pi,13):
    major_tick=box(
        axis=vector(
            radius*np.cos(theta),
            radius*np.sin(theta),
            0),
        color=color.black,
        length=major_tick_length,
        width=major_tick_width,
        height=major_tick_thickness,
        pos=vector(
            (radius-major_tick_length/2)*np.cos(theta),
            (radius-major_tick_length/2)*np.sin(theta),
            0)),

text_string=13

for theta in np.linspace(np.pi/2,2*np.pi+np.pi/3,12):
    text_string=text_string-1
    clock_num=text(
        text=str(text_string),
        align='center',
        pos=vector(
            (radius-major_tick_length-.2)*np.cos(theta),
            (radius-major_tick_length-.2)*np.sin(theta)-text_height/4,
            thickness/2),
        color=color.orange,
        height=text_height/2)

for theta in np.linspace(0,2*np.pi,61):
    minor_tick=box(
        axis=vector(radius*np.cos(theta),radius*np.sin(theta),0),
        color=color.black,
        length=minor_tick_length,
        width=minor_tick_width,
        height=minor_tick_thickness,
        pos=vector(
            (radius-minor_tick_length/2)*np.cos(theta),(radius-minor_tick_length/2)*np.sin(theta),
            0))

while True:
    rate(5000)
    second=time.localtime(time.time())[5]
    minute=time.localtime(time.time())[4]
    hour=time.localtime(time.time())[3]
    if hour>12:
        hour=hour-12
    second_angle=(-(second*np.pi)/30+np.pi/2)
    minute_angle=-(minute*np.pi)/30-(second*np.pi)/1800+np.pi/2
    hour_angle=-(hour*np.pi)/6-(minute*np.pi)/360+np.pi/2
    hour_hand.axis=vector(hour_hand_length*np.cos(hour_angle),hour_hand_length*np.sin(hour_angle),0)
    minute_hand.axis=vector(minute_hand_length*np.cos(minute_angle),minute_hand_length*np.sin(minute_angle),0)
    second_hand.axis=vector(second_hand_length*np.cos(second_angle),second_hand_length*np.sin(second_angle),0)