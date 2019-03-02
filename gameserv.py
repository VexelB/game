import pygame
import random
import socket
import engine

rec1 = []
rec2 = []
rec3 = []
rec4 = []
rec5 = []

def init():
    r = 0
    def reinit():
        if engine.unitblue1.reload == 'yes' and engine.unitred1.reload == 'yes':
            conn.send('reinit/'.encode())
            engine.map = [[0 for i in range(9)] for j in range(9)]
            gen()
            bullets = []
            engine.unitblue1.init()
            engine.unitred1.init()
            interface.draw(win)

    pygame.init()
    win_height = win_width = 500
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("StepGame")

    #map = [[0 for i in range(9)] for j in range(9)]

    def gen():
        i = 1
        while i != 8:
            k = random.randint(1,3)
            while k >0:
                j = random.randint(1,7)
                engine.map[j][i] = 3
                k -= 1
            i += 1
        pass



    def maindraw():
        win.fill((0,0,0))
        for bullet in bullets:
            x, y = int(bullet.x*len(engine.map)/win_height), int(bullet.y*len(engine.map[0])/win_width)
            if x >= 9:
                x -= 1
            if y >= 9:
                y -= 1
            if engine.map[x][y] != 0:
                bullets.pop(bullets.index(bullet))
                for unit in engine.units:
                    if unit.x == x and unit.y == y:
                        unit.destroy()
                        if unit.x == engine.unitred1.x and unit.y == engine.unitred1.y:
                            conn.send('dr/'.encode())
                        if unit.x == engine.unitblue1.x and unit.y == engine.unitblue1.y:
                            conn.send('db/'.encode())
            elif bullet.x < win_height and bullet.x > 0 and bullet.y < win_width and bullet.y > 0:
                bullet.move(win)
            else:
                bullets.pop(bullets.index(bullet))
        for i in range(len(engine.map)):
            for j in range(len(engine.map[0])):
                x = win_height / len(engine.map) * i
                y = win_width / len(engine.map[0]) * j
                if engine.map[i][j] == 1:
                    pygame.draw.rect(win, (250, 0, 0), (x+5, y+5, engine.UnitRed.width, engine.UnitRed.height))
                    if engine.unitred1.orient == 'up':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+engine.unitred1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if engine.unitred1.orient == 'down':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+engine.unitred1.width//2)-win_height//200, y+5+engine.unitred1.height, win_height//100, win_height//100))
                    if engine.unitred1.orient == 'left':
                        pygame.draw.rect(win, (250, 0, 0), (x+5-win_height//100, (y+5+engine.unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                    if engine.unitred1.orient == 'right':
                        pygame.draw.rect(win, (250, 0, 0), (x+engine.unitred1.width+5, (y+5+engine.unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                if engine.map[i][j] == 2:
                    pygame.draw.rect(win, (0, 0, 250), (x+5, y+5, engine.UnitBlue.width, engine.UnitBlue.height))
                    if engine.unitblue1.orient == 'up':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+engine.unitblue1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if engine.unitblue1.orient == 'down':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+engine.unitblue1.width//2)-win_height//200, y+5+engine.unitblue1.height, win_height//100, win_height//100))
                    if engine.unitblue1.orient == 'left':
                        pygame.draw.rect(win, (0, 0, 250), (x+5-win_height//100, (y+5+engine.unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                    if engine.unitblue1.orient == 'right':
                        pygame.draw.rect(win, (0, 0, 250), (x+engine.unitblue1.width+5, (y+5+engine.unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                if engine.map[i][j] == 3:
                    pygame.draw.rect(win, (250, 250, 250), (x+5, y+5, engine.UnitRed.width, engine.UnitRed.height))
        for unit in engine.units:
            if unit.helth != 0:
                pygame.draw.rect(win, (0, 0, 0), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 , engine.UnitRed.width, 10))
                pygame.draw.rect(win, (250, 250, 250), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 + 2 , engine.UnitRed.width * unit.helth // 3, 6))
                #pygame.draw.rect(win, (250, 250, 250), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 + 2, engine.UnitRed.width, 6))
        interface.draw(win)
        pygame.draw.rect(win, (250, 250, 250), (win_width-75, 0, 5, 15))
        pygame.draw.rect(win, (250, 250, 250), (win_width-75, 10, 75, 5))
        for i in range(engine.unitred1.bullets):
            pygame.draw.circle(win, (250, 250, 0), ((win_height-5)-15*i, 5), win_width//100)
        pygame.display.update()

    def parser():
        data1 = conn.recv(512).decode()
        dataset = data1.split('/')
        for data in dataset:
            if len(data) != 0:
                if data[0] == 'q':
                    engine.unitblue1.orient = data[1::]
                elif data[0] == '2':
                    if data[1::] == 'left' and engine.unitblue1.x>0:
                        engine.unitblue1.move(engine.unitblue1.x-1,engine.unitblue1.y)
                        conn.send((str(engine.unitblue1.x)+str(engine.unitblue1.y)+'/').encode())
                    elif data[1::] == 'right' and engine.unitblue1.x<8:
                        engine.unitblue1.move(engine.unitblue1.x+1, engine.unitblue1.y)
                        conn.send((str(engine.unitblue1.x)+str(engine.unitblue1.y)+'/').encode())
                    elif data[1::] == 'up' and engine.unitblue1.y>0:
                        engine.unitblue1.move(engine.unitblue1.x, engine.unitblue1.y-1)
                        conn.send((str(engine.unitblue1.x)+str(engine.unitblue1.y)+'/').encode())
                    elif data[1::] == 'down' and engine.unitblue1.y<8:
                        engine.unitblue1.move(engine.unitblue1.x,engine.unitblue1.y+1)
                        conn.send((str(engine.unitblue1.x)+str(engine.unitblue1.y)+'/').encode())
                    elif data[1::] == 'fire':
                        a = int(win_height / len(engine.map) * engine.unitblue1.x)
                        b = int(win_height / len(engine.map[0]) * engine.unitblue1.y)
                        if engine.unitblue1.orient == 'up':
                            if engine.unitblue1.y != 0:
                                bullets.append(engine.Bullet(int(a + engine.unitblue1.width//2) + 5, b, engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'down':
                            if engine.unitblue1.y != 8:
                                bullets.append(engine.Bullet(int(a + engine.unitblue1.width//2) + 5, int(b + engine.unitblue1.height + 10), engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'left':
                            if engine.unitblue1.x != 0:
                                bullets.append(engine.Bullet(a, int(b + engine.unitblue1.width//2) + 5, engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'right':
                            if engine.unitblue1.x != 8:
                                bullets.append(engine.Bullet(int(a + engine.unitblue1.width) + 10, int(b + engine.unitblue1.width//2) + 5, engine.unitblue1.orient, (255, 255, 0)))
                elif data == 'r':
                    if engine.unitblue1.reload == 'no':
                        engine.unitblue1.reload = 'yes'
                    else:
                        engine.unitblue1.reload = 'no'
                    reinit()
        conn.send('1/'.encode())

    def mapsender(sendata):
        map1 = ''
        for i in engine.map:
            for j in i:
                map1 += str(j)
        conn.send(('map'+map1+'/'+sendata).encode())

    interface = engine.Interface()
    gen()
    bullets = []
    run = True
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    while run:
        sendata = ''
        parser()
        maindraw()
        #pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if engine.unitred1.helth > 0 :
                    if event.key == pygame.K_w or event.key == 172:
                        engine.unitred1.orient = 'up'
                        #conn.send('qup/'.encode())
                        sendata += 'qup/'
                    if event.key == pygame.K_s or event.key == 161:
                        engine.unitred1.orient = 'down'
                        #conn.send('qdown/'.encode())
                        sendata += 'qdown/'
                    if event.key == pygame.K_a or event.key == 160:
                        engine.unitred1.orient = 'left'
                        #conn.send('qleft/'.encode())
                        sendata += 'qleft/'
                    if event.key == pygame.K_d or event.key == 162:
                        engine.unitred1.orient = 'right'
                        #conn.send('qright/'.encode())
                        sendata += 'qright/'
                    if event.key == pygame.K_SPACE:
                        if engine.unitred1.bullet == 'reload':
                            if engine.unitred1.bullets == 5:
                                engine.unitred1.bullet = ''
                            else:
                                engine.unitred1.bullets += 1
                        if engine.unitred1.bullets >= 0 and engine.unitred1.bullet != 'reload':
                            engine.unitred1.bullets -= 1
                            sendata += '2fire/'
                            if engine.unitred1.orient == 'up':
                                if engine.unitred1.y != 0:
                                    bullets.append(engine.Bullet(int(win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width//2) + 5, int(win_height / len(engine.map[0]) * engine.unitred1.y), engine.unitred1.orient, (255, 255, 0)))
                            elif engine.unitred1.orient == 'down':
                                if engine.unitred1.y !=8:
                                    bullets.append(engine.Bullet(int(win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width//2) + 5, int(win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.height + 10), engine.unitred1.orient, (255, 255, 0)))
                            elif engine.unitred1.orient == 'left':
                                if engine.unitred1.x != 0:
                                    bullets.append(engine.Bullet(int(win_height / len(engine.map) * engine.unitred1.x), int(win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.width//2) + 5, engine.unitred1.orient, (255, 255, 0)))
                            elif engine.unitred1.orient == 'right':
                                if engine.unitred1.x != 8:
                                    bullets.append(engine.Bullet(int(win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width) + 10, int(win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.width//2) + 5, engine.unitred1.orient, (255, 255, 0)))
                        if engine.unitred1.bullets < 1:
                            engine.unitred1.bullet = 'reload'
                    if event.key == pygame.K_LEFT and engine.unitred1.x>0:
                        engine.unitred1.move(engine.unitred1.x-1,engine.unitred1.y)
                        #conn.send((str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/').encode())
                        sendata += (str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/')
                    if event.key == pygame.K_RIGHT and engine.unitred1.x<8:
                        engine.unitred1.move(engine.unitred1.x+1, engine.unitred1.y)
                        #conn.send((str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/').encode())
                        sendata += (str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/')
                    if event.key == pygame.K_UP and engine.unitred1.y>0:
                        engine.unitred1.move(engine.unitred1.x, engine.unitred1.y-1)
                        #conn.send((str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/').encode())
                        sendata += (str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/')
                    if event.key == pygame.K_DOWN and engine.unitred1.y<8:
                        engine.unitred1.move(engine.unitred1.x, engine.unitred1.y+1)
                        #conn.send((str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/').encode())
                        sendata += (str(int(engine.unitred1.x))+str(int(engine.unitred1.y))+'red/')
                if event.key == pygame.K_r or event.key == 174:
                    if engine.unitred1.reload == 'no':
                        engine.unitred1.reload = 'yes'
                    else:
                        engine.unitred1.reload = 'no'
                    conn.send('r/'.encode())
                    reinit()
        mapsender(sendata)

    conn.close()
    pygame.quit()
if __name__ == '__main__':
    init()
