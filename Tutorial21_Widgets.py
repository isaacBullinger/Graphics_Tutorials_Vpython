from vpython import *
from time import *

m_radius=1
m_color=color.red
wall_thickness=.1
room_length=20
room_width=20
room_height=12

delta_x=.1
delta_y=.1
delta_z=.1

x_pos=5
y_pos=0
z_pos=0
run=0

def runRadio(x):
    print(x.checked)
    global run
    if x.checked==True:
        run=1
    if x.checked==False:
        run=0

def bigBall(x):
    global m_radius
    if x.checked==True:
        m_radius=m_radius*2
    if x.checked==False:
        m_radius=m_radius/2

    marble.radius=m_radius
    
radio(bind=runRadio, text='Run')
scene.append_to_caption('\n')
checkbox(bind=bigBall,text='Big Ball')

floor=box(
    pos=vector(0,-room_height/2,0),
    color=color.white,
    size=vector(room_length,wall_thickness,room_width))

ceiling=box(
    pos=vector(0,room_height/2,0),
    color=color.white,
    size=vector(room_length,wall_thickness,room_width))

right_wall=box(
    pos=vector(-room_length/2,0,0),
    color=color.white,
    size=vector(wall_thickness,room_height,room_width))

left_wall=box(
    pos=vector(room_length/2,0,0),
    color=color.white,
    size=vector(wall_thickness,room_height,room_width))

back_wall=box(
    pos=vector(0,0,-room_width/2),
    color=color.white,
    size=vector(room_length,room_height,wall_thickness))

marble=sphere(
    color=m_color,
    radius=m_radius)

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

while True:
    rate(20)
    x_pos+=delta_x*run
    y_pos+=delta_y*run
    z_pos+=delta_z*run
    if (x_pos+m_radius)>=((room_length/2)-(wall_thickness/2)) or ((x_pos-m_radius)<(-room_length/2)+(wall_thickness/2)):
        delta_x=delta_x*-1
        marble.color=color.blue
    if (y_pos+m_radius)>=((room_height/2)-(wall_thickness/2)) or ((y_pos-m_radius)<(-room_height/2)+(wall_thickness/2)):
        delta_y=delta_y*-1
        marble.color=color.green
    if (z_pos+m_radius)>=((room_width/2)-(wall_thickness/2)) or ((z_pos-m_radius)<(-room_width/2)+(wall_thickness/2)):
        delta_z=delta_z*-1
        marble.color=color.red
    marble.pos=vector(x_pos,y_pos,z_pos)