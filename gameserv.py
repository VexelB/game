import pygame
import random
import socket

rec1 = []
rec2 = []
rec3 = []
rec4 = []
rec5 = []

def init():

    pygame.init()
    win_height = win_width = 500
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("StepGame")

    map = [[0 for i in range(9)] for j in range(9)]

    def gen():
        i = 1
        while i != 8:
            k = random.randint(1,3)
            while k >0:
                j = random.randint(1,7)
                map[j][i] = 3
                k -= 1
            i += 1
        pass

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
        def draw(self):
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
        speed = win_height//50;
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
                unitblue1.init()
        def destroy(self):
            self.helth -= 1
            conn.send('4'.encode())
            if self.helth == 0:
                map[self.x][self.y] = 0
                conn.send(('5'+str(self.x)+str(self.y)).encode())
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
                unitred1.init()
        def destroy(self):
            self.helth -= 1
            if self.helth == 0:
                map[self.x][self.y] = 0
                del self

    def maindraw():
        for bullet in bullets:
            x, y = int(bullet.x*len(map)/win_height), int(bullet.y*len(map[0])/win_width)
            if x > 8:
                x -= 1
            if y > 8:
                y -= 1
            if map[x][y] != 0:
                bullets.pop(bullets.index(bullet))
                for unit in units:
                    if unit.x == x and unit.y == y:
                        unit.destroy()
            elif bullet.x < win_height and bullet.x > 0 and bullet.y < win_width and bullet.y > 0:
                bullet.move()
            else:
                bullets.pop(bullets.index(bullet))

        for i in range(len(map)):
            for j in range(len(map[0])):
                x = win_height / len(map) * i
                y = win_width / len(map[0]) * j
                if map[i][j] == 1:
                    pygame.draw.rect(win, (250, 0, 0), (x+5, y+5, UnitRed.width, UnitRed.height))
                    if unitred1.orient == 'up':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+unitred1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if unitred1.orient == 'down':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+unitred1.width//2)-win_height//200, y+5+unitred1.height, win_height//100, win_height//100))
                    if unitred1.orient == 'left':
                        pygame.draw.rect(win, (250, 0, 0), (x+5-win_height//100, (y+5+unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                    if unitred1.orient == 'right':
                        pygame.draw.rect(win, (250, 0, 0), (x+unitred1.width+5, (y+5+unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                if map[i][j] == 2:
                    pygame.draw.rect(win, (0, 0, 250), (x+5, y+5, UnitBlue.width, UnitBlue.height))
                    if unitblue1.orient == 'up':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+unitblue1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if unitblue1.orient == 'down':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+unitblue1.width//2)-win_height//200, y+5+unitblue1.height, win_height//100, win_height//100))
                    if unitblue1.orient == 'left':
                        pygame.draw.rect(win, (0, 0, 250), (x+5-win_height//100, (y+5+unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                    if unitblue1.orient == 'right':
                        pygame.draw.rect(win, (0, 0, 250), (x+unitblue1.width+5, (y+5+unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                if map[i][j] == 3:
                    pygame.draw.rect(win, (250, 250, 250), (x+5, y+5, UnitRed.width, UnitRed.height))

    def parser():
        data = conn.recv(512).decode()
        if len(data) != 0:
            if data[0] == 'q':
                unitblue1.orient = data[1::]
            elif data[0] == '2':
                if data[1::] == 'left' and unitblue1.x>0:
                    unitblue1.move(unitblue1.x-1,unitblue1.y)
                    conn.send((str(unitblue1.x)+str(unitblue1.y)).encode())
                elif data[1::] == 'right' and unitblue1.x<8:
                    unitblue1.move(unitblue1.x+1, unitblue1.y)
                    conn.send((str(unitblue1.x)+str(unitblue1.y)).encode())
                elif data[1::] == 'up' and unitblue1.y>0:
                    unitblue1.move(unitblue1.x, unitblue1.y-1)
                    conn.send((str(unitblue1.x)+str(unitblue1.y)).encode())
                elif data[1::] == 'down' and unitblue1.y<8:
                    unitblue1.move(unitblue1.x,unitblue1.y+1)
                    conn.send((str(unitblue1.x)+str(unitblue1.y)).encode())
                elif data[1::] == 'fire':
                    a = int(win_height / len(map) * unitblue1.x)
                    b = int(win_height / len(map[0]) * unitblue1.y)
                    if unitblue1.orient == 'up':
                        bullets.append(Bullet(int(a + unitblue1.width//2) + 5, b, unitblue1.orient, (255, 255, 0)))
                    elif unitblue1.orient == 'down':
                        bullets.append(Bullet(int(a + unitblue1.width//2) + 5, int(b + unitblue1.height + 10), unitblue1.orient, (255, 255, 0)))
                        a += unitblue1.width//2 + 5
                        b += unitblue1.height + 10
                    elif unitblue1.orient == 'left':
                        bullets.append(Bullet(a, int(b + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                        b += unitblue1.width//2 + 5
                    elif unitblue1.orient == 'right':
                        bullets.append(Bullet(int(a + unitblue1.width) + 10, int(b + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                        a += unitblue1.width + 10
                        b += unitblue1.width//2 + 5
                    #conn.send(('5'+str(int(a))+'/'+str(int(b))+'/'+unitblue1.orient).encode())

    def mapsender():
        map1 = ''
        for i in map:
            for j in i:
                map1 += str(j)
        conn.send(('map'+map1).encode())

    units=[]
    unitblue1 = UnitBlue()
    unitblue1.init()
    units.append(unitblue1)
    unitred1 = UnitRed()
    unitred1.init()
    units.append(unitred1)
    interface = Interface()
    gen()
    bullets = []
    run = True
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    while run:
        parser()
        win.fill((0,0,0))
        maindraw()
        interface.draw()
        pygame.display.update()
        #pygame.time.delay(10)
        mapsender()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    unitred1.orient = 'up'
                    conn.send('qup'.encode())
                if event.key == pygame.K_s:
                    unitred1.orient = 'down'
                    conn.send('qdown'.encode())
                if event.key == pygame.K_a:
                    unitred1.orient = 'left'
                    conn.send('qleft'.encode())
                if event.key == pygame.K_d:
                    unitred1.orient = 'right'
                    conn.send('qright'.encode())
                if event.key == pygame.K_SPACE:
                    conn.send('2fire'.encode())
                    if unitred1.orient == 'up':
                        bullets.append(Bullet(int(win_height / len(map) * unitred1.x + unitred1.width//2) + 5, int(win_height / len(map[0]) * unitred1.y), unitred1.orient, (255, 255, 0)))
                    if unitred1.orient == 'down':
                        bullets.append(Bullet(int(win_height / len(map) * unitred1.x + unitred1.width//2) + 5, int(win_height / len(map[0]) * unitred1.y + unitred1.height + 10), unitred1.orient, (255, 255, 0)))
                    if unitred1.orient == 'left':
                        bullets.append(Bullet(int(win_height / len(map) * unitred1.x), int(win_height / len(map[0]) * unitred1.y + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                    if unitred1.orient == 'right':
                        bullets.append(Bullet(int(win_height / len(map) * unitred1.x + unitred1.width) + 10, int(win_height / len(map[0]) * unitred1.y + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                if event.key == pygame.K_LEFT and unitred1.x>0:
                    unitred1.move(unitred1.x-1,unitred1.y)
                    conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red').encode())
                if event.key == pygame.K_RIGHT and unitred1.x<8:
                    unitred1.move(unitred1.x+1, unitred1.y)
                    conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red').encode())
                if event.key == pygame.K_UP and unitred1.y>0:
                    unitred1.move(unitred1.x, unitred1.y-1)
                    conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red').encode())
                if event.key == pygame.K_DOWN and unitred1.y<8:
                    unitred1.move(unitred1.x, unitred1.y+1)
                    conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red').encode())


    conn.close()
    pygame.quit()
if __name__ == '__main__':
    init()
