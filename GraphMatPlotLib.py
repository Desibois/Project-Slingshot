import math
import matplotlib.pyplot as plt
import numpy as np 

def simulation(h):
    g = 9.81 
    e1 = 0.85 
    e2 = 0.772 
    e = math.sqrt(e1 * e2) 

    mass1, mass2 = 0.625, 0.057
    velocity = math.sqrt(2*g*h) 
    v1, v2 = velocity*e1, -velocity
    v = ((mass1 - mass2)*v1 + (1+e)*mass2*v2)/(mass1+mass2)

    s = (v**2) / (2 * abs(g))
    h += s
    return h

x = np.linspace(0, 100, 1000)  
y= np.array([simulation(h) for h in x])

plt.plot(x, y)  
plt.xlabel('Starting height/m')
plt.ylabel('Maximum height/m')
plt.title('Predicted h of tennis ball')
plt.grid(True)
plt.show()
