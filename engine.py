import random

win_height = win_width = 500
map = [[0 for i in range(9)] for j in range(9)]
score = []

class Bullet:
    radius = win_width//100
    speed = win_height//15;
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
    def __init__(self, q):
        self.reload = 'no'
        self.bullet = 'no'
        self.bullets = 5
        self.helth = 5
        self.orient = 'down'
        self.move(int(len(map[0])/2), 0, q)
    def draw(self, q):
        maps[q][self.x][self.y] = 2
    def move(self, a, b, q):
        if maps[q][a][b] == 0 or maps[q][a][b] == 2:
            maps[q][self.x][self.y] = 0
            self.x = a
            self.y = b
            self.draw(q)
    def destroy(self, j):
        self.helth -= 1
        if self.helth == 0:
            maps[j//2][self.x][self.y] = 0
            score[j//2][0] += 1
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
    def __init__(self, q):
        self.reload = 'no'
        self.bullet = ''
        self.bullets = 5
        self.helth = 5
        self.orient = 'up'
        self.move(int(len(map[0])/2), len(map)-1, q)
    def draw(self, q):
        maps[q][self.x][self.y] = 1
    def move(self, a, b, q):
        if maps[q][a][b] == 0 or maps[q][a][b] == 1:
            maps[q][self.x][self.y] = 0
            self.x = a
            self.y = b
            self.draw(q)
    def destroy(self, j):
        self.helth -= 1
        if self.helth == 0:
            maps[j][self.x][self.y] = 0
            score[j][1] += 1
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
    map[int(len(map[0])/2)][len(map)-1] = 1
    map[int(len(map[0])/2)][0] = 2
maps = []
units=[]
