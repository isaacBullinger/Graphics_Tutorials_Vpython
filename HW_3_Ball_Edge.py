from vpython import *
from time import *

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

m_radius=2
wall_thickness=1
room_length=15
room_width=12
room_height=8

floor=box(pos=vector(0,-room_height/2,0),color=color.white,size=vector(room_length,wall_thickness,room_width))
ceiling=box(pos=vector(0,room_height/2,0),color=color.white,size=vector(room_length,wall_thickness,room_width))
right_wall=box(pos=vector(-room_length/2,0,0),color=color.white,size=vector(wall_thickness,room_height,room_width))
left_wall=box(pos=vector(room_length/2,0,0),color=color.white,size=vector(wall_thickness,room_height,room_width))
back_wall=box(pos=vector(0,0,-room_width/2),color=color.white,size=vector(room_length,room_height,wall_thickness))
marble=sphere(color=color.red,radius=m_radius)

delta_x=.1
x_pos=0

while True:
    rate(20)
    x_pos+=delta_x
    if (x_pos+m_radius)>=((room_length/2)-(wall_thickness/2)) or ((x_pos-m_radius)<(-room_length/2)+(wall_thickness/2)):
        delta_x=delta_x*-1
    marble.pos=vector(x_pos,0,0)