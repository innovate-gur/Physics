from ursina import *

class Physics(object):
    def __init__(self, obj):
        self.x_a = 0
        self.x_v = 0
        self.y_a = 0
        self.y_v = 0
        self.pre_y = 0
        self.pre_x = 0
        self.F = 0
        self.obj = obj
        self.onfloor = False
    
    def refresh(self, obj):
        self.obj = obj
        
    def calculate_s(self):
        self.x_v += self.x_a
        self.y_v += self.y_a
        self.obj.x += self.x_v
        self.obj.y += self.y_v
        if self.onfloor:
            self.obj.y = self.pre_y
            self.y_v = 0
        else:
            self.pre_y = self.obj.y
            self.pre_x = self.obj.x
    def calculate_g(self):
        if self.onfloor:
            self.y_a = 0
        else:
            self.y_a -= 0.001
    
    def calculate_f(self):
        self.F = self.x_v * 0.01
        self.x_a -= self.F
    def movement(self):

        if held_keys['w']:
            self.y_a = 0.001
        elif held_keys['a']:
            self.x_a = -0.001
        elif held_keys['d']:
           self. x_a = 0.001
        elif held_keys['s']:
            self.y_a = -0.001
        else:
            self.y_a, self.x_a = 0, 0
            
app = Ursina()

ball = Entity(model='sphere', scale=0.5, position=(0, 2, 10), collider='box')
ground = Entity(model='cube', texture="ground.jpeg", scale=(40, 10, 4), position=(0, -10, 10), collider='box')

P = Physics(ball)

def update():
    global P
    if held_keys['r']:
        P = Physics(ball)
        ball.position = (0, 2, 10)
    P.movement()
    #P.calculate_g()
    P.calculate_s()
    #P.calculate_f()
    P.refresh(ball)
    
    hit_info = ball.intersects()
    P.onfloor = hit_info.hit



app.run()
