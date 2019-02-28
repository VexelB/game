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
        if r % 2 == 0 and r != 0:
            engine.map = [[0 for i in range(9)] for j in range(9)]
            gen()
            bullets = []
            unitblue1.init()
            unitred1.init()
            conn.send('reinit/'.encode())
            print(engine.score)
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
            if x > 8:
                x -= 1
            if y > 8:
                y -= 1
            if engine.map[x][y] != 0:
                bullets.pop(bullets.index(bullet))
                for unit in units:
                    if unit.x == x and unit.y == y:
                        unit.destroy()
                        print(unit, unit.helth)
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
                    if unitred1.orient == 'up':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+unitred1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if unitred1.orient == 'down':
                        pygame.draw.rect(win, (250, 0, 0), ((x+5+unitred1.width//2)-win_height//200, y+5+unitred1.height, win_height//100, win_height//100))
                    if unitred1.orient == 'left':
                        pygame.draw.rect(win, (250, 0, 0), (x+5-win_height//100, (y+5+unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                    if unitred1.orient == 'right':
                        pygame.draw.rect(win, (250, 0, 0), (x+unitred1.width+5, (y+5+unitred1.height//2)-win_height//200, win_height//100, win_height//100))
                if engine.map[i][j] == 2:
                    pygame.draw.rect(win, (0, 0, 250), (x+5, y+5, engine.UnitBlue.width, engine.UnitBlue.height))
                    if unitblue1.orient == 'up':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+unitblue1.width//2)-win_height//200, y+5-win_height//100, win_height//100, win_height//100))
                    if unitblue1.orient == 'down':
                        pygame.draw.rect(win, (0, 0, 250), ((x+5+unitblue1.width//2)-win_height//200, y+5+unitblue1.height, win_height//100, win_height//100))
                    if unitblue1.orient == 'left':
                        pygame.draw.rect(win, (0, 0, 250), (x+5-win_height//100, (y+5+unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                    if unitblue1.orient == 'right':
                        pygame.draw.rect(win, (0, 0, 250), (x+unitblue1.width+5, (y+5+unitblue1.height//2)-win_height//200, win_height//100, win_height//100))
                if engine.map[i][j] == 3:
                    pygame.draw.rect(win, (250, 250, 250), (x+5, y+5, engine.UnitRed.width, engine.UnitRed.height))
        for unit in units:
            if unit.helth != 0:
                pygame.draw.rect(win, (0, 0, 0), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 , engine.UnitRed.width, 10))
                pygame.draw.rect(win, (250, 250, 250), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 + 2 , engine.UnitRed.width * unit.helth // 3, 6))
                #pygame.draw.rect(win, (250, 250, 250), ((int(win_height / len(engine.map) * unit.x)+5), int(win_height / len(engine.map[0]) * unit.y) + unit.height // 2 + 2, engine.UnitRed.width, 6))

    def parser():
        data1 = conn.recv(512).decode()
        #if data1 != '':
            #print('Прием:', data1)
        dataset = data1.split('/')
        for data in dataset:
            if len(data) != 0:
                if data[0] == 'q':
                    unitblue1.orient = data[1::]
                elif data[0] == '2':
                    if data[1::] == 'left' and unitblue1.x>0:
                        unitblue1.move(unitblue1.x-1,unitblue1.y)
                        conn.send((str(unitblue1.x)+str(unitblue1.y)+'/').encode())
                    elif data[1::] == 'right' and unitblue1.x<8:
                        unitblue1.move(unitblue1.x+1, unitblue1.y)
                        conn.send((str(unitblue1.x)+str(unitblue1.y)+'/').encode())
                    elif data[1::] == 'up' and unitblue1.y>0:
                        unitblue1.move(unitblue1.x, unitblue1.y-1)
                        conn.send((str(unitblue1.x)+str(unitblue1.y)+'/').encode())
                    elif data[1::] == 'down' and unitblue1.y<8:
                        unitblue1.move(unitblue1.x,unitblue1.y+1)
                        conn.send((str(unitblue1.x)+str(unitblue1.y)+'/').encode())
                    elif data[1::] == 'fire':
                        a = int(win_height / len(engine.map) * unitblue1.x)
                        b = int(win_height / len(engine.map[0]) * unitblue1.y)
                        if unitblue1.orient == 'up':
                            bullets.append(engine.Bullet(int(a + unitblue1.width//2) + 5, b, unitblue1.orient, (255, 255, 0)))
                        elif unitblue1.orient == 'down':
                            bullets.append(engine.Bullet(int(a + unitblue1.width//2) + 5, int(b + unitblue1.height + 10), unitblue1.orient, (255, 255, 0)))
                            a += unitblue1.width//2 + 5
                            b += unitblue1.height + 10
                        elif unitblue1.orient == 'left':
                            bullets.append(engine.Bullet(a, int(b + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                            b += unitblue1.width//2 + 5
                        elif unitblue1.orient == 'right':
                            bullets.append(engine.Bullet(int(a + unitblue1.width) + 10, int(b + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                            a += unitblue1.width + 10
                            b += unitblue1.width//2 + 5
                        #conn.send(('5'+str(int(a))+'/'+str(int(b))+'/'+unitblue1.orient).encode())
                elif data == 'r':
                    print(r)
                    reinit()
        conn.send('1/'.encode())

    def mapsender(sendata):
        map1 = ''
        for i in engine.map:
            for j in i:
                map1 += str(j)
        conn.send(('map'+map1+'/'+sendata).encode())

    units=[]
    unitblue1 = engine.UnitBlue()
    unitblue1.init()
    units.append(unitblue1)
    unitred1 = engine.UnitRed()
    unitred1.init()
    units.append(unitred1)
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
        interface.draw(win)
        pygame.display.update()
        #pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if unitred1.helth > 0 :
                    if event.key == pygame.K_w or event.key == 172:
                        unitred1.orient = 'up'
                        #conn.send('qup/'.encode())
                        sendata += 'qup/'
                    if event.key == pygame.K_s or event.key == 161:
                        unitred1.orient = 'down'
                        #conn.send('qdown/'.encode())
                        sendata += 'qdown/'
                    if event.key == pygame.K_a or event.key == 160:
                        unitred1.orient = 'left'
                        #conn.send('qleft/'.encode())
                        sendata += 'qleft/'
                    if event.key == pygame.K_d or event.key == 162:
                        unitred1.orient = 'right'
                        #conn.send('qright/'.encode())
                        sendata += 'qright/'
                    if event.key == pygame.K_SPACE:
                        conn.send('2fire/'.encode())
                        if unitred1.orient == 'up':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitred1.x + unitred1.width//2) + 5, int(win_height / len(engine.map[0]) * unitred1.y), unitred1.orient, (255, 255, 0)))
                        if unitred1.orient == 'down':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitred1.x + unitred1.width//2) + 5, int(win_height / len(engine.map[0]) * unitred1.y + unitred1.height + 10), unitred1.orient, (255, 255, 0)))
                        if unitred1.orient == 'left':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitred1.x), int(win_height / len(engine.map[0]) * unitred1.y + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                        if unitred1.orient == 'right':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitred1.x + unitred1.width) + 10, int(win_height / len(engine.map[0]) * unitred1.y + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                    if event.key == pygame.K_LEFT and unitred1.x>0:
                        unitred1.move(unitred1.x-1,unitred1.y)
                        #conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red/').encode())
                        sendata += (str(int(unitred1.x))+str(int(unitred1.y))+'red/')
                    if event.key == pygame.K_RIGHT and unitred1.x<8:
                        unitred1.move(unitred1.x+1, unitred1.y)
                        #conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red/').encode())
                        sendata += (str(int(unitred1.x))+str(int(unitred1.y))+'red/')
                    if event.key == pygame.K_UP and unitred1.y>0:
                        unitred1.move(unitred1.x, unitred1.y-1)
                        #conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red/').encode())
                        sendata += (str(int(unitred1.x))+str(int(unitred1.y))+'red/')
                    if event.key == pygame.K_DOWN and unitred1.y<8:
                        unitred1.move(unitred1.x, unitred1.y+1)
                        #conn.send((str(int(unitred1.x))+str(int(unitred1.y))+'red/').encode())
                        sendata += (str(int(unitred1.x))+str(int(unitred1.y))+'red/')
                if event.key == pygame.K_r or event.key == 174:
                    r += 1
                    print(r)
                    reinit()
                print(event.key)
        #if sendata != '':
            #print('Отправка:',sendata)
        mapsender(sendata)

    conn.close()
    pygame.quit()
if __name__ == '__main__':
    init()
