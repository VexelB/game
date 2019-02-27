import pygame
import socket
import engine

rec1 = []
rec2 = []
rec3 = []
rec4 = []
rec5 = []

def init():
    sock = socket.socket()
    pygame.init()
    win_height = win_width = 500
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("StepGame")

    def maindraw():
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

    units=[]
    unitblue1 = engine.UnitBlue()
    unitblue1.init()
    units.append(unitblue1)
    unitred1 = engine.UnitRed()
    unitred1.init()
    units.append(unitred1)
    interface = engine.Interface()
    bullets = []
    run = True
    sock.connect(('localhost', 9090))
    while run:
        def reciever():
            data1 = sock.recv(512).decode()
            #print(data)
            dataset = data1.split('/')
            for data in dataset:
                if len(data) != 0:
                    if data[0:3:] == 'map':
                        q = 3
                        for i in range(len(engine.map)):
                            for j in range(len(engine.map[0])):
                                engine.map[i][j] = int(data[q])
                                q += 1
                    elif 'red' in data:
                        unitred1.move(int(data[0]), int(data[1]))
                    elif len(data) == 2:
                        unitblue1.move(int(data[0]), int(data[1]))
                    elif data[1::] == 'fire':
                        a = int(win_height / len(engine.map) * unitred1.x)
                        b = int(win_height / len(engine.map[0]) * unitred1.y)
                        if unitred1.orient == 'up':
                            bullets.append(engine.Bullet(int(a + unitred1.width//2) + 5, b, unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'down':
                            bullets.append(engine.Bullet(int(a + unitred1.width//2) + 5, int(b + unitred1.height + 10), unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'left':
                            bullets.append(engine.Bullet(a, int(b + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                        elif unitred1.orient == 'right':
                            bullets.append(engine.Bullet(int(a + unitred1.width) + 10, int(b + unitred1.width//2) + 5, unitred1.orient, (255, 255, 0)))
                    elif data[0] == 'q':
                        unitred1.orient = data[1::]

        sock.send('1/'.encode())
        reciever()
        win.fill((0,0,0))
        maindraw()
        interface.draw(win)
        pygame.display.update()
        sendata = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if unitblue1.helth > 0:
                    if event.key == pygame.K_w or event.key == 172:
                        unitblue1.orient = 'up'
                        #sock.send('qup'.encode())
                        sendata += 'qup/'
                    if event.key == pygame.K_s or event.key == 161:
                        unitblue1.orient = 'down'
                        #sock.send('qdown'.encode())
                        sendata += 'qdown/'
                    if event.key == pygame.K_a or event.key == 160:
                        unitblue1.orient = 'left'
                        #sock.send('qleft'.encode())
                        sendata += 'qleft/'
                    if event.key == pygame.K_d or event.key == 162:
                        unitblue1.orient = 'right'
                        #sock.send('qright'.encode())
                        sendata += 'qright/'
                    if event.key == pygame.K_SPACE:
                        if unitblue1.orient == 'up':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitblue1.x + unitblue1.width//2) + 5, int(win_height / len(engine.map[0]) * unitblue1.y), unitblue1.orient, (255, 255, 0)))
                        if unitblue1.orient == 'down':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitblue1.x + unitblue1.width//2) + 5, int(win_height / len(engine.map[0]) * unitblue1.y + unitblue1.height + 10), unitblue1.orient, (255, 255, 0)))
                        if unitblue1.orient == 'left':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitblue1.x), int(win_height / len(engine.map[0]) * unitblue1.y + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                        if unitblue1.orient == 'right':
                            bullets.append(engine.Bullet(int(win_height / len(engine.map) * unitblue1.x + unitblue1.width) + 10, int(win_height / len(engine.map[0]) * unitblue1.y + unitblue1.width//2) + 5, unitblue1.orient, (255, 255, 0)))
                        #sock.send('2fire/'.encode())
                        sendata += '2fire/'
                    if event.key == pygame.K_LEFT:
                        #sock.send('2left'.encode())
                        reciever()
                        sendata += '2left/'
                    if event.key == pygame.K_RIGHT:
                        #sock.send('2right'.encode())
                        reciever()
                        sendata += '2right/'
                    if event.key == pygame.K_UP:
                        #sock.send('2up'.encode())
                        reciever()
                        sendata += '2up/'
                    if event.key == pygame.K_DOWN:
                        #sock.send('2down'.encode())
                        reciever()
                        sendata += '2down/'
        sock.send(sendata.encode())

    #print(rec1)
    sock.close()
    pygame.quit()
if __name__ == '__main__':
    init()
