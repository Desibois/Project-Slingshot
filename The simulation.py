import math

#######################################################################################################################################
                                             # CONSTANTS
#######################################################################################################################################

g = 9.81 
e1 = 0.772 # coefficient of restitution for a tennis ball
e2 = 0.85  # coefficient of restitution for a basketball
e = math.sqrt(e1 * e2) # coefficient of restitution between tennis ball and basketball

#######################################################################################################################################
                                             # INPUTS
#######################################################################################################################################

mass1 = float(input('Mass 1/kg: '))
mass2 = float(input('Mass 2/kg: '))
height2 = float(input('Length of mass 2/m: '))
h = float(input('Height/m: '))  
h += height2

#######################################################################################################################################
                                             # BALLS HIT THE GROUND
#######################################################################################################################################

#Velocity of balls before they hit the ground
velocity = math.sqrt(2*g*h) 
v1 = velocity

#Velocity a mass 2 after bouncing off the ground
v2 = velocity*e2

#######################################################################################################################################
                                             # COLLISION BETWEEN BALLS
#######################################################################################################################################

#Equation derived from combining Conservation of Momentum and Coefficient of Restitution
v = ((mass1 - mass2)*v1 + (1+e)*mass2*v2)/(mass1+mass2)

#######################################################################################################################################
                                             #SUVAT 
#######################################################################################################################################

#s = ?
u = 0
v 
a = -9.81
#t - Unnecessary

s = (v**2 - u**2) /2*a

#Displacement from initial height
s -= h




