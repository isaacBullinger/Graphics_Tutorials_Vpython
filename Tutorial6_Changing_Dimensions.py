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

my_sphere=sphere(radius=1,color=color.red,opacity=.25)

while True:
    for my_radius in np.linspace(1,0,1000):
        rate(500)
        my_sphere.radius=my_radius
    for my_radius in np.linspace(0,1,1000):
        rate(500)
        my_sphere.radius=my_radius