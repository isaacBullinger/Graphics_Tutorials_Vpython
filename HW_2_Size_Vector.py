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

floor=box(pos=vector(0,-5,0),color=color.white,size=vector(10,.1,10))

ceiling=box(pos=vector(0,5,0),color=color.white,size=vector(10,.1,10))

right_wall=box(pos=vector(-5,0,0),color=color.white,size=vector(.1,10,10))

left_wall=box(pos=vector(5,0,0),color=color.white,size=vector(.1,10,10))

back_wall=box(pos=vector(0,0,-5),color=color.white,size=vector(10,10,.1))

marble=sphere(color=color.red,radius=.75)

delta_x=.1
x_pos=0

while True:
    rate(20)
    x_pos+=delta_x
    if x_pos>5 or x_pos<-5:
        delta_x=delta_x*-1
    marble.pos=vector(x_pos,0,0)