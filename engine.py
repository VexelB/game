import pygame
pygame.init()
win_height = win_width = 500
map = [[0 for i in range(9)] for j in range(9)]
class Interface:
    myfont = pygame.font.SysFont('Comic Sans MS', win_height//19,5)
    info = myfont.render('Переключение:', False, (250, 250, 250))
    atck = myfont.render('1: Атаковать (СПАСЕ)', False, (250, 250, 250))
    heal = myfont.render('2: Хилить (СПАСЕ)', False, (250, 250, 250))
    deff = myfont.render('3: Поддержка (КОНСТ)', False, (250, 250, 250))
    opts = myfont.render('Управление:', False, (250, 250, 250))
    wsad = myfont.render('Целиться: WSAD', False, (250, 250, 250))
    udrl = myfont.render('ЕЗДЕТЬ: стрелочки', False, (250, 250, 250))
    spce = myfont.render('Стрилять: SPACE', False, (250, 250, 250))
    rrrr = myfont.render('R', False, (250, 250, 250))
    def draw(self, win):
        pygame.draw.rect(win, (250, 250, 250), (0, win_height+5, win_width, 5))
        win.blit(self.info, (win_width//50, win_height+win_height//5//10*1))
        win.blit(self.atck, (win_width//50, win_height+win_height//5//10*3))
        win.blit(self.heal, (win_width//50, win_height+win_height//5//10*5))
        win.blit(self.deff, (win_width//50, win_height+win_height//5//10*7))
        win.blit(self.opts, (win_width//2, win_height+win_height//5//10*1))
        win.blit(self.udrl, (win_width//2, win_height+win_height//5//10*3))
        win.blit(self.wsad, (win_width//2, win_height+win_height//5//10*5))
        win.blit(self.spce, (win_width//2, win_height+win_height//5//10*7))
        win.blit(self.rrrr, (win_height//20*19, win_height+win_height//5//2))

class Bullet:
    radius = win_width//100
    speed = win_height//25;
    def __init__(self, x, y, orient, color):
        self.x = x
        self.y = y
        self.orient = orient
        self.color = color
    def move(self, win):
        if self.orient == 'up':
            self.y -= self.speed
        if self.orient == 'down':
            self.y += self.speed
        if self.orient == 'left':
            self.x -= self.speed
        if self.orient == 'right':
            self.x += self.speed
        self.draw(win)
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class UnitBlue:
    helth = 3
    orient = 'down'
    y = 0
    x = int(len(map[0])/2)
    width = win_width/10
    height = win_height/10
    def init(self):
        map[self.x][self.y] = 2
    def move(self, a, b):
        if map[a][b] == 0 or map[a][b] == 2:
            map[self.x][self.y] = 0
            self.x = a
            self.y = b
            self.init()
    def destroy(self):
        self.helth -= 1
        #conn.send('4'.encode())
        if self.helth == 0:
            map[self.x][self.y] = 0
            #conn.send(('5'+str(self.x)+str(self.y)).encode())
            del self

class UnitRed:
    helth = 3
    orient = 'up'
    y = len(map)-1
    x = int(len(map[0])/2)
    width = win_width/10
    height = win_height/10
    def init(self):
        map[self.x][self.y] = 1
    def move(self, a, b):
        if map[a][b] == 0 or map[a][b] == 1:
            map[self.x][self.y] = 0
            self.x = a
            self.y = b
            self.init()
    def destroy(self):
        self.helth -= 1
        if self.helth == 0:
            map[self.x][self.y] = 0
            del self
