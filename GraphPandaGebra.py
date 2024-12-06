import math
import numpy as np
import pandas as pd


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


x_values = np.linspace(0, 10, 100)
y_values = np.array([simulation(h) for h in x_values])
df = pd.DataFrame({'Starting Height /m': x_values, 'Maximum Height /m': y_values})
df.to_csv('simulation.csv', index=False)

print("CSV file 'simulation.csv' created.")