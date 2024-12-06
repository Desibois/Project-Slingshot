import math

#######################################################################################################################################
                                             # CONSTANTS
#######################################################################################################################################

g = 9.81 
e1 = 0.85  # coefficient of restitution for a basketball
e2 = 0.772 # coefficient of restitution for a tennis ball
e = math.sqrt(e1 * e2) # coefficient of restitution between tennis ball and basketball

#######################################################################################################################################
                                             # INPUTS
#######################################################################################################################################

mass1 = float(input('Mass 1/kg: '))
radius1 = float(input('Radius of mass 1/m: '))
mass2 = float(input('Mass 2/kg: '))
radius2 = float(input('Radius of mass 2/m: '))
h = float(input('Height/m: '))

#######################################################################################################################################
                                             # BALLS HIT THE GROUND
#######################################################################################################################################

#Velocity of balls before they hit the ground
velocity = math.sqrt(2*g*h) 
v1 = velocity*e1
v2 = -velocity

#######################################################################################################################################
                                             # COLLISION BETWEEN BALLS
#######################################################################################################################################

#Equation derived from combining Conservation of Momentum and Coefficient of Restitution
v = ((mass1 - mass2)*v1 + (1+e)*mass2*v2)/(mass1+mass2)

#######################################################################################################################################
                                             #SUVAT 
#######################################################################################################################################

#s = ?
#u = 0
#v 
a = abs(g)
#t - Unnecessary

d = (v**2) / (2 * a)

#Displacement from initial height
s = d + h + radius1 + radius2 

#######################################################################################################################################
                                             #FINALE
#######################################################################################################################################


print(f'''
v: {v:.2f}
h: {d:.2f}
s: {s:.2f}
''')
