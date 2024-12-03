import math

g = 9.81
e1 = 0.772 # coefficient of restitution for a tennis ball
e2 = 0.85  # coefficient of restitution for a basketball
mass1 = float(input('Mass 1/kg: '))
mass2 = float(input('Mass 2/kg: '))
height2 = float(input('Length of mass 2/m: '))
h = float(input('Height/m: '))
t = float(input('Collision time between both masses'))
h += height2

#######################################################################################################################################
#v^2 = u^2 + 2as --> velocity of both balls when they hit the ground
velocity = math.sqrt(2*g*h) 
#######################################################################################################################################
#Velocity a mass 2 after bouncing off the ground
v2 = velocity*e2

#Collision between mass1 and mass2
#Needs work
v1 = 0



#######################################################################################################################################
#SUVAT will be used to get displacement
#######################################################################################################################################

u = 0
v = v1
a = -9.81

s = (v^2 - u^2) /2*a

#Displacement from initial height
s -= h




