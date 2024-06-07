from vpython import *
from threading import Thread
import time

# color=vector(r,g,b)

my_sphere=sphere(radius=1,color=vector(1,1,0))
pause=5
red_increment=.001
green_increment=-.001
blue_increment=.001
red=1
green=1
blue=0

while True:
    rate(250)
    
    red=red+red_increment
    green=green+green_increment
    blue=blue+blue_increment

    if red<=1:
        red_apply=red      
    if red>1:
        red_apply=1
        
    if green<=1:
        green_apply=green          
    if green>1:
        green_apply=1
        
    if blue<=1:
        blue_apply=blue        
    if blue>1:
        blue_apply=1

    my_sphere.color=vector(red_apply,green_apply,blue_apply)

    if red>=1.5 or red<=0:
        red_increment=red_increment*(-1)
    
    if green>=1.5 or green<=0:
        green_increment=green_increment*(-1)
    
    if blue>=1.5 or blue<=0:
        blue_increment=blue_increment*(-1)
        
    print(red_apply+green_apply+blue_apply)
