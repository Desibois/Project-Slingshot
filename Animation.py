import turtle
import time
import threading


g = 25
h = 250
timestep = 0.03
l = -497
f = False

class Ball(turtle.Turtle):
    def __init__(self, mass=0.0, radius=0.0, COR=0.0 ):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.radius = radius
        self.velocity = 0.0
        self.height = h
        self.mass = mass
        self.e = COR
        self.shapesize(self.radius/10, self.radius/10)

class BasketBall(Ball):
    def __init__(self):
        super().__init__(100.0, 100.0, 0.85)
        self.color('orange')

    def originalHeight(self):
        self.sety(self.height)

    def fallDown(self):
        global f
        self.velocity -= g*timestep  
        new_y = self.ycor() + self.velocity
        if new_y - self.radius <= l:
            new_y = l + self.radius
            f = True
        self.sety(new_y)    

        

class TennisBall(Ball):
    def __init__(self):
        super().__init__(50.0, 50.0, 0.772)
        self.color('blue')

    def originalHeight(self, radius):
        self.sety(self.height + self.radius + radius)

    def fallDown(self, diameter):
        global f
        self.velocity -= g*timestep
        new_y = self.ycor() + self.velocity
        if new_y - self.radius - diameter <= l:      
            new_y = l + diameter + self.radius
            f = True
        self.sety(new_y)    
 
    


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')

ball1 = TennisBall()
ball2 = BasketBall()
diameter = ball2.radius * 2

ball1.originalHeight(ball2.radius)
ball2.originalHeight()

def update_simulation():
    if not f:
        ball1.fallDown(ball2.radius*2)
        ball2.fallDown()

        screen.ontimer(update_simulation, int(timestep * 1000))
    else:
        print(f)

update_simulation()

screen.mainloop()
