from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
##print bob

##def square(t, length):
##    for i in range(4):
##        fd(t, length)
##        lt(t)
##fd(bob, 100)
##lt(bob)
##fd(bob, 100)
##lt(bob)
##fd(bob, 100) 
##
##for i in range(4):
##    print 'Hello!'

##print square(bob,50)

##def polygon(t, length, n):
##    for i in range(n):
##        angle = 360/n
##        fd(t, length)
##        lt(t, angle)
####
####print polygon(bob, 100, 6)
##
##def circle(t, r):
##    circumference = 2* math.pi* r
##    n = int(circumference / 3)
##    print n
##    length = circumference / n + 1
##    print polygon(t, length, n)
##
##print circle(bob, 50)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

##print circle(bob, 50)

print arc(bob,100, 25)


wait_for_user()

