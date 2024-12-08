import turtle
import time
import math


g = 25
h = 250
timestep = 0.03
l = -497
stop = False
strike = 0

class Ball(turtle.Turtle):
    def __init__(self, mass=0.0, radius=0.0, COR=0.0 ):
        super().__init__()
        self.floor = False
        self.shape('circle')
        self.penup()
        self.radius = radius
        self.velocity = 0.0
        self.height = h
        self.mass = mass
        self.e = COR
        self.shapesize(self.radius/10, self.radius/10)

    def move(self):
        self.velocity -= g * timestep
        new_y = self.ycor() + self.velocity
        if new_y - self.radius <= l:  
            new_y = l + self.radius
            self.velocity = -self.velocity * self.e  
            if abs(self.velocity) < 1:  
                self.floor = True
        self.sety(new_y)

            

class BasketBall(Ball):
    def __init__(self):
        super().__init__(100.0, 100.0, 0.85)
        self.color('orange')

    def originalHeight(self):
        self.sety(self.height)
   
        

class TennisBall(Ball):
    def __init__(self):
        super().__init__(50.0, 50.0, 0.772)
        self.color('blue')

    def originalHeight(self, radius):
        self.sety(self.height + self.radius + radius)
   


def handle_collision(ball1, ball2):
    distance = abs(ball1.ycor() - ball2.ycor())
    combined_radius = ball1.radius + ball2.radius
    if distance <= combined_radius:  
        e = math.sqrt(ball1.e * ball2.e)
        v1_initial = ball1.velocity
        v2_initial = ball2.velocity
        ball1.velocity = ((ball1.mass - e * ball2.mass) * v1_initial + (1 + e) * ball2.mass * v2_initial) / (ball1.mass + ball2.mass)
        ball2.velocity = ((ball2.mass - e * ball1.mass) * v2_initial + (1 + e) * ball1.mass * v1_initial) / (ball1.mass + ball2.mass)



def update_simulation():
    global strike
    global stop
    if ball1.ycor() < (l + ball1.radius +  ball2.radius *2):
        if stop:
            print("Both balls have stopped bouncing.")
            quit()
        
        if strike == 10:
            stop = True
        else: strike += 1
        
    if not (ball1.floor and ball2.floor):   
        ball1.move()
        ball2.move()
        handle_collision(ball1, ball2)
        screen.ontimer(update_simulation, int(timestep * 1000))

    
    


screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor('black')

ball1 = TennisBall()
ball2 = BasketBall()
diameter = ball2.radius * 2

ball1.originalHeight(ball2.radius)
ball2.originalHeight()


update_simulation()
    

screen.mainloop()
