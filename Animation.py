import turtle
import time
import threading


g = 25
h = 250
timestep = 0.03

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
        while True:
            self.velocity -= g*timestep  
            new_y = self.ycor() + self.velocity
            if new_y - self.radius <= -497:  
                break

            self.sety(new_y)    
            time.sleep(timestep)
        



class TennisBall(Ball):
    def __init__(self):
        super().__init__(50.0, 50.0, 0.772)
        self.color('blue')

    def originalHeight(self, radius):
        self.sety(self.height + self.radius + radius)

    def fallDown(self, diameter):
        time.sleep(timestep)
        while True:
            self.velocity -= g*timestep
            new_y = self.ycor() + self.velocity
            if new_y - self.radius - diameter <= -497:  
                break

            self.sety(new_y)    
            time.sleep(timestep)
    




screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')

ball1 = TennisBall()
ball2 = BasketBall()
diameter = ball2.radius * 2

ball1.originalHeight(ball2.radius)
ball2.originalHeight()

thread1 = threading.Thread(target=ball1.fallDown, args=(diameter,))
thread2 = threading.Thread(target=ball2.fallDown)

thread1.start()
thread2.start()

screen.mainloop()
