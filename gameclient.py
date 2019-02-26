import pygame
import socket

rec1 = []
rec2 = []
rec3 = []
rec4 = []
rec5 = []

def init():
    sock = socket.socket()
    map = [[0 for i in range(9)] for j in range(9)]
    pygame.init()
    win_height = win_width = 500
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("StepGame")

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
            if map[a][b] == 0:
                map[self.x][self.y] = 0
                self.x = a
                self.y = b
                self.init()
        def destroy(self):
            self.helth -= 1
            if self.helth == 0:
                map[self.x][self.y] = 0
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
            if map[a][b] == 0:
                map[self.x][self.y] = 0
                self.x = a
                self.y = b
                self.init()
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

    units=[]
    unitblue1 = UnitBlue()
    unitblue1.init()
    units.append(unitblue1)
    unitred1 = UnitRed()
    unitred1.init()
    units.append(unitred1)
    interface = Interface()
    bullets = []
    run = True
    sock.connect(('172.20.10.13', 9090))
    while run:
        def reciever():
            data1 = sock.recv(512).decode()
            #print(data)
            dataset = data1.split('/')
            for data in dataset:
                if len(data) != 0:
                    if data[0:3:] == 'map':
                        q = 3
                        for i in range(len(map)):
                            for j in range(len(map[0])):
                                map[i][j] = int(data[q])
                                q += 1
                    elif 'red' in data:
                        unitred1.move(int(data[0]), int(data[1]))
                    elif len(data) == 2:
                        unitblue1.move(int(data[0]), int(data[1]))
                    elif data[1::] == 'fire':
                        a = int(win_height / len(map) * unitred1.x)
                        b = int(win_height / len(map[0]) * unitred1.y)
                        if unitred1.orient == 'up':
                            bullets.append(Bullet(int(a + unitred1.width//2) + 5, b, unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'down':
                            bullets.append(Bullet(int(a + unitred1.width//2) + 5, int(b + unitred1.height + 10), unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'left':
                            bullets.append(Bullet(a, int(b + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'right':
                            bullets.append(Bullet(int(a + unitred1.width) + 10, int(b + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                    elif data[0] == 'q':
                        unitred1.orient = data[1::]

        sock.send('1/'.encode())
        reciever()
        win.fill((0,0,0))
        maindraw()
        interface.draw()
        pygame.display.update()
        sendata = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    unitblue1.orient = 'up'
                    #sock.send('qup'.encode())
                    sendata += 'qup/'
                if event.key == pygame.K_s:
                    unitblue1.orient = 'down'
                    #sock.send('qdown'.encode())
                    sendata += 'qdown/'
                if event.key == pygame.K_a:
                    unitblue1.orient = 'left'
                    #sock.send('qleft'.encode())
                    sendata += 'qleft/'
                if event.key == pygame.K_d:
                    unitblue1.orient = 'right'
                    #sock.send('qright'.encode())
                    sendata += 'qright/'
                if event.key == pygame.K_SPACE:
                    if unitblue1.orient == 'up':
                        bullets.append(Bullet(int(win_height / len(map) * unitblue1.x + unitblue1.width//2) + 5, int(win_height / len(map[0]) * unitblue1.y), unitblue1.orient, (255, 255, 0)))
                    if unitblue1.orient == 'down':
                        bullets.append(Bullet(int(win_height / len(map) * unitblue1.x + unitblue1.width//2) + 5, int(win_height / len(map[0]) * unitblue1.y + unitblue1.height + 10), unitblue1.orient, (255, 255, 0)))
                    if unitblue1.orient == 'left':
                        bullets.append(Bullet(int(win_height / len(map) * unitblue1.x), int(win_height / len(map[0]) * unitblue1.y + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                    if unitblue1.orient == 'right':
                        bullets.append(Bullet(int(win_height / len(map) * unitblue1.x + unitblue1.width) + 10, int(win_height / len(map[0]) * unitblue1.y + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                    #sock.send('2fire/'.encode())
                    sendata += '2fire/'
                if event.key == pygame.K_LEFT:
                    #sock.send('2left'.encode())
                    #reciever()
                    sendata += '2left/'
                if event.key == pygame.K_RIGHT:
                    #sock.send('2right'.encode())
                    #reciever()
                    sendata += '2right/'
                if event.key == pygame.K_UP:
                    #sock.send('2up'.encode())
                    #reciever()
                    sendata += '2up/'
                if event.key == pygame.K_DOWN:
                    #sock.send('2down'.encode())
                    #reciever()
                    sendata += '2down/'
        sock.send(sendata.encode())

    #print(rec1)
    sock.close()
    pygame.quit()
if __name__ == '__main__':
    init()
