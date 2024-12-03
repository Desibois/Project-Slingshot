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

#v^2 = u^2 + 2as --> velocity of both balls when they hit the ground
velocity = math.sqrt(2*g*h) 

#######################################################################################################################################
#Ball 2 hits the ground at the v and there is a reaction force from the ground which makes Ball 2 go up at v*e2
#Ball 2 collides with Ball 1 and momentum is transferred between the 2 balls
#Newton's 2nd law - F = Δp/Δt --> Δp =F*Δt 




#v1=(1−e)v2
#This is the formula for the collision between the 2 balls and v1 is the final velocity going up
#######################################################################################################################################


#InitialMomentum = mass1 * velocity
#rForce = (mass1 + mass2) * g
#AddedMomentum = rForce*t
#FinalMomentum = InitialMomentum + AddedMomentum

v2 = velocity*e2
v1 = (1-e1)*v2



#######################################################################################################################################
#We have the momentum of Ball1 going up
#It's initial velocity can now be calculated
#From that, displacement can also be calculated using SUVAT



#We now have the final velocity of the ball going up
#SUVAT will be used to get displacement
#######################################################################################################################################


u = 0
#v = FinalMomentum / mass1
v = v1
a = -9.81

s = (v^2 - u^2) /2*a

#Displacement from initial height
s -= h




