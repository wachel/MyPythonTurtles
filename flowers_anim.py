import turtle as t
import random
from typing import List

class Flower:
    def __init__(self, num, pos:t.Vec2D, type, angle, size, speed:t.Vec2D, angle_speed):
        self.pos:t.Vec2D = pos
        self.type = type
        self.angle = angle
        self.num = num
        self.size = size
        self.speed = speed
        self.angle_speed = angle_speed
    
    def update(self, delta_time):
        self.pos += self.speed * delta_time
        self.angle += self.angle_speed * delta_time
        x,y = self.pos
        if x > t.window_width() / 2 + self.size:
            x -= t.window_width() + self.size
        if y < -(t.window_height() / 2 + self.size):
            y += t.window_height() + self.size
        self.pos = t.Vec2D(x,y)

    def draw(self):
        t.up()
        t.goto(self.pos)
        t.down()
        t.seth(self.angle)
        for i in range(self.num):
            t.color("#602dbd" if self.type==0 else "#ffb5ff")
            t.begin_fill()
            t.circle(self.size, 90)
            t.left(90)
            t.circle(self.size, 90)
            t.left(90)
            t.end_fill()

            if self.type == 1:
                t.color("#f36ff3")
                t.begin_fill()
                t.circle(self.size * 0.66,90)
                t.left(90)
                t.circle(self.size * 0.66, 90)
                t.left(90)
                t.end_fill()

                t.color("#ffb5ff")
                t.left(45)
                t.forward(self.size * 0.5)
                t.backward(self.size * 0.5)
                t.right(45)

            t.right(360/self.num)

t.bgcolor("#5322ae")
t.color("white")

w = t.window_width()
h = t.window_height()

flowers:List[Flower] = []

for i in range(5):
    pos = t.Vec2D(random.randint(-w//2,w//2), random.randint(-h//2,h//2))
    size = random.randint(30,100)
    speed = t.Vec2D(random.randint(-1,1),random.randint(-2,-1))
    angle_speed = random.randint(-5,5)
    flowers.append(Flower(5, pos, 0, random.randint(0, 360), size, speed, angle_speed))

for i in range(8):
    pos = t.Vec2D(random.randint(-w//2,w//2), random.randint(-h//2,h//2))
    size = random.randint(20,50)
    speed = t.Vec2D(random.randint(3,6),random.randint(-10,0))
    angle_speed = random.randint(-5,5)
    flowers.append(Flower(5, pos, 1, random.randint(0, 360), size, speed, angle_speed))

for i in range(10):
    pos = t.Vec2D(random.randint(-w//2,w//2), random.randint(-h//2,h//2))
    size = random.randint(20,40)
    speed = t.Vec2D(random.randint(3,6),random.randint(-10,0))
    angle_speed = random.randint(-5,5)
    flowers.append(Flower(1, pos, 1, random.randint(0, 360), size, speed, angle_speed))


t.speed(0)
for flower in flowers:
    flower.update(0.5)
    flower.draw()

t.tracer(0)
t.hideturtle()

while True:
    t.clear()
    for flower in flowers:
        flower.update(0.5)
        flower.draw()
    t.update()
