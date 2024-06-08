from vpython import *
from time import *

m_radius=1
m_color=color.white
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
my_speed=1

def ballColorRed(x):
    marble.color=color.red

def ballColorGreen(x):
    marble.color=color.green

def ballColorBlue(x):
    marble.color=color.blue

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

def ballOpacity(x):
    opacity=x.value
    marble.opacity=opacity

def speed(x):
    global my_speed
    if x.selected=='1':
        my_speed=1
    if x.selected=='2':
        my_speed=2
    if x.selected=='3':
        my_speed=3
    if x.selected=='4':
        my_speed=4
    if x.selected=='5':
        my_speed=5
    
button(
    bind=ballColorRed,
    text='Red',
    color=color.black,
    background=color.red)

scene.append_to_caption('   ')

button(
    bind=ballColorGreen,
    text='Green',
    color=color.black,
    background=color.green)

scene.append_to_caption('   ')

button(
    bind=ballColorBlue,
    text='Blue',
    color=color.black,
    background=color.blue)

scene.append_to_caption('\n')

radio(
    bind=runRadio,
    text='Run')

checkbox(
    bind=bigBall,
    text='Big Ball')

scene.append_to_caption(' ')

menu(bind=speed,
    choices=['1','2','3','4','5'])

scene.append_to_caption(' Speed')

scene.append_to_caption('\n')

scene.append_to_caption('Opacity\n')
slider(
    bind=ballOpacity,
    vertical=False,
    min=0,
    max=1,
    value=1)

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
    x_pos+=delta_x*run*my_speed
    y_pos+=delta_y*run*my_speed
    z_pos+=delta_z*run*my_speed
    if (x_pos+m_radius)>=((room_length/2)-(wall_thickness/2)) or ((x_pos-m_radius)<(-room_length/2)+(wall_thickness/2)):
        delta_x=delta_x*-1
    if (y_pos+m_radius)>=((room_height/2)-(wall_thickness/2)) or ((y_pos-m_radius)<(-room_height/2)+(wall_thickness/2)):
        delta_y=delta_y*-1
    if (z_pos+m_radius)>=((room_width/2)-(wall_thickness/2)) or ((z_pos-m_radius)<(-room_width/2)+(wall_thickness/2)):
        delta_z=delta_z*-1
    marble.pos=vector(x_pos,y_pos,z_pos)