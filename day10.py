import tkinter
import tkinter.messagebox

def example1():
    flag = True

    def change_lable():
        nonlocal flag
        flag = not flag
        color, msg = ('green','Hello World')\
            if flag else ('red', 'Goodbye World')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askyesno('Alert', message='Are you sure you want to quit?'): 
            main_window.quit()
            
    main_window = tkinter.Tk()
    main_window.geometry('300x260')
    main_window.title('game')

    label = tkinter.Label(main_window,text='Hello World',font='Arial -32',fg='Green')
    label.pack(expand=1)
    panel = tkinter.Frame(main_window)
    panel.pack(side='bottom')

    button1 = tkinter.Button(panel,text='edit',command=change_lable)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text='quit',command=confirm_to_quit)
    button2.pack(side='right')
   

    tkinter.mainloop()

## example2, big balls eat small balls
from enum import Enum, unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    @staticmethod
    def random_color():
        return(randint(0,255),randint(0,255),randint(0,255))

class Ball(object):

    def __init__(self, screen, x, y, sx, sy, radius, color = Color.RED):
        if x - radius <= 0 or \
                x + radius >= screen.get_width():
            sx = -sx
        if y - radius <= 0 or \
                y + radius >= screen.get_height():
            sy = -sy
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.radius = radius
        self.color = color
        self.alive = True
        
    
    def move(self, screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx 
        if self.y - self.radius <= 0 or \
                self.y + self.radius >=screen.get_height():
            self.sy = -self.sy
    
    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx = self.x - other.x
            dy = self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)

def example2():
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((1000,800))
    pygame.display.set_caption('Big circle eat Small circle')

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                radius = randint(10,30)
                balls.append(Ball(screen,x,y,sx,sy,radius,color))

        screen.fill((255,255,255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    example2()