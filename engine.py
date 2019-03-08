#import pygame
import random

win_height = win_width = 500
map = [[0 for i in range(9)] for j in range(9)]
score = [0, 0]

class Bullet:
    radius = win_width//100
    speed = win_height//30;
    def __init__(self, x, y, orient, color):
        self.x = x
        self.y = y
        self.orient = orient
        self.color = color
    def move(self):
        if self.orient == 'up':
            self.y -= self.speed
        if self.orient == 'down':
            self.y += self.speed
        if self.orient == 'left':
            self.x -= self.speed
        if self.orient == 'right':
            self.x += self.speed
        #self.draw(win)
    #def draw(self, win):
    #    pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class UnitBlue:
    reload = 'no'
    bullets = 5
    bullet = 'no'
    helth = 5
    orient = 'down'
    y = 0
    x = int(len(map[0])/2)
    width = win_width/10
    height = win_height/10
    def init(self):
        self.reload = 'no'
        self.bullet = 'no'
        self.bullets = 5
        self.helth = 5
        self.orient = 'down'
        self.move(int(len(map[0])/2), 0)
    def draw(self):
        map[self.x][self.y] = 2
    def move(self, a, b):
        if map[a][b] == 0 or map[a][b] == 2:
            map[self.x][self.y] = 0
            self.x = a
            self.y = b
            self.draw()
    def destroy(self):
        self.helth -= 1
        #conn.send('4'.encode())
        if self.helth == 0:
            map[self.x][self.y] = 0
            #conn.send(('5'+str(self.x)+str(self.y)).encode())
            score[0] += 1
            del self

class UnitRed:
    reload = 'no'
    bullets = 5
    bullet = 'no'
    helth = 5
    orient = 'up'
    y = len(map)-1
    x = int(len(map[0])/2)
    width = win_width/10
    height = win_height/10
    def init(self):
        self.reload = 'no'
        self.bullet = ''
        self.bullets = 5
        self.helth = 5
        self.orient = 'up'
        self.move(int(len(map[0])/2), len(map)-1)
    def draw(self):
        map[self.x][self.y] = 1
    def move(self, a, b):
        if map[a][b] == 0 or map[a][b] == 1:
            map[self.x][self.y] = 0
            self.x = a
            self.y = b
            self.draw()
    def destroy(self):
        self.helth -= 1
        if self.helth == 0:
            map[self.x][self.y] = 0
            score[1] += 1
            del self
def gen():
    i = 1
    while i != 8:
        k = random.randint(1,3)
        while k >0:
            j = random.randint(1,7)
            map[j][i] = 3
            k -= 1
        i += 1

units=[]
unitblue1 = UnitBlue()
unitblue1.init()
units.append(unitblue1)
unitred1 = UnitRed()
unitred1.init()
units.append(unitred1)
