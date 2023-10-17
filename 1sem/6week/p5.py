from random import randint
from tkinter import *

width = 300
height = 200


class Ball:
    def __init__(self):
        self.R = randint(10, 30)
        self.x = randint(self.R, width - self.R)
        self.y = randint(self.R, height - self.R)
        self.dx, self.dy = (10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R,
                                          fill=rand_color())

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > width or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > height or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


def add_new(*args):
    balls.append(Ball())


def rand_color():
    a, b, c = hex(randint(0, 255)).strip('0x'), hex(randint(0, 255)).strip('0x'), hex(randint(0, 255)).strip('0x')
    s = '#'
    for x in (a, b, c):
        match len(x):
            case 0:
                s += '00'
            case 1:
                s += '0' + x
            case 2:
                s += x
    return s


root = Tk()
root.geometry(f'{width}x{height}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', add_new)
balls = []
tick()
root.mainloop()
