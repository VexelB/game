import socket
import engine

def reinit():
    if engine.unitblue1.reload == 'yes' and engine.unitred1.reload == 'yes':
            engine.map = [[0 for i in range(9)] for j in range(9)]
            engine.gen()
            bullets = []
            engine.unitblue1.init()
            engine.unitred1.init()

def parser(data1):
    dataset = data1.split('/')
    for data in dataset:
        if dataset[0] == 'red':
            if engine.unitred1.helth != 0:
                if data == 'up' and engine.unitred1.y > 0:
                    engine.unitred1.move(engine.unitred1.x, engine.unitred1.y-1)
                elif data == 'down' and engine.unitred1.y < 8:
                    engine.unitred1.move(engine.unitred1.x, engine.unitred1.y+1)
                elif data == 'left' and engine.unitred1.x > 0:
                    engine.unitred1.move(engine.unitred1.x-1, engine.unitred1.y)
                elif data == 'right' and engine.unitred1.x < 8:
                    engine.unitred1.move(engine.unitred1.x+1, engine.unitred1.y)
                elif data == 'w':
                    engine.unitred1.orient = 'up'
                elif data == 's':
                    engine.unitred1.orient = 'down'
                elif data == 'a':
                    engine.unitred1.orient = 'left'
                elif data == 'd':
                    engine.unitred1.orient = 'right'
                elif data == 'space':
                    if engine.unitred1.bullet == 'reload':
                        if engine.unitred1.bullets == 5:
                            engine.unitred1.bullet = 'no'
                        else:
                            engine.unitred1.bullets += 1
                    if engine.unitred1.bullets >= 0 and engine.unitred1.bullet != 'reload':
                        engine.unitred1.bullets -= 1
                        if engine.unitred1.orient == 'up':
                            if engine.unitred1.y != 0:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width//2) + 5, int(engine.win_height / len(engine.map[0]) * engine.unitred1.y), engine.unitred1.orient, (255, 255, 0)))
                        elif engine.unitred1.orient == 'down':
                            if engine.unitred1.y !=8:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width//2) + 5, int(engine.win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.height + 10), engine.unitred1.orient, (255, 255, 0)))
                        elif engine.unitred1.orient == 'left':
                            if engine.unitred1.x != 0:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitred1.x), int(engine.win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.width//2) + 5, engine.unitred1.orient, (255, 255, 0)))
                        elif engine.unitred1.orient == 'right':
                            if engine.unitred1.x != 8:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitred1.x + engine.unitred1.width) + 10, int(engine.win_height / len(engine.map[0]) * engine.unitred1.y + engine.unitred1.width//2) + 5, engine.unitred1.orient, (255, 255, 0)))
                        if engine.unitred1.bullets < 1:
                            engine.unitred1.bullet = 'reload'
            if data == 'r':
                if engine.unitred1.reload == 'no':
                    engine.unitred1.reload = 'yes'
                else:
                    engine.unitred1.reload = 'no'
                reinit()
        elif dataset[0] == 'blue':
            if engine.unitblue1.helth != 0:
                if data == 'up' and engine.unitblue1.y > 0:
                    engine.unitblue1.move(engine.unitblue1.x, engine.unitblue1.y-1)
                elif data == 'down' and engine.unitblue1.y < 8:
                    engine.unitblue1.move(engine.unitblue1.x, engine.unitblue1.y+1)
                elif data == 'left' and engine.unitblue1.x > 0:
                    engine.unitblue1.move(engine.unitblue1.x-1, engine.unitblue1.y)
                elif data == 'right' and engine.unitblue1.x < 8:
                    engine.unitblue1.move(engine.unitblue1.x+1, engine.unitblue1.y)
                elif data == 'w':
                    engine.unitblue1.orient = 'up'
                elif data == 's':
                    engine.unitblue1.orient = 'down'
                elif data == 'a':
                    engine.unitblue1.orient = 'left'
                elif data == 'd':
                    engine.unitblue1.orient = 'right'
                elif data == 'space':
                    if engine.unitblue1.bullet == 'reload':
                        if engine.unitblue1.bullets == 5:
                            engine.unitblue1.bullet = 'no'
                        else:
                            engine.unitblue1.bullets += 1
                    if engine.unitblue1.bullets >= 0 and engine.unitblue1.bullet != 'reload':
                        engine.unitblue1.bullets -= 1
                        if engine.unitblue1.orient == 'up':
                            if engine.unitblue1.y != 0:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitblue1.x + engine.unitblue1.width//2) + 5, int(engine.win_height / len(engine.map[0]) * engine.unitblue1.y), engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'down':
                            if engine.unitblue1.y !=8:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitblue1.x + engine.unitblue1.width//2) + 5, int(engine.win_height / len(engine.map[0]) * engine.unitblue1.y + engine.unitblue1.height + 10), engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'left':
                            if engine.unitblue1.x != 0:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitblue1.x), int(engine.win_height / len(engine.map[0]) * engine.unitblue1.y + engine.unitblue1.width//2) + 5, engine.unitblue1.orient, (255, 255, 0)))
                        elif engine.unitblue1.orient == 'right':
                            if engine.unitblue1.x != 8:
                                bullets.append(engine.Bullet(int(engine.win_height / len(engine.map) * engine.unitblue1.x + engine.unitblue1.width) + 10, int(engine.win_height / len(engine.map[0]) * engine.unitblue1.y + engine.unitblue1.width//2) + 5, engine.unitblue1.orient, (255, 255, 0)))
                        if engine.unitblue1.bullets < 1:
                            engine.unitblue1.bullet = 'reload'
            if data == 'r':
                if engine.unitblue1.reload == 'no':
                    engine.unitblue1.reload = 'yes'
                else:
                    engine.unitblue1.reload = 'no'
                reinit()

def sender(conn):
    ab = int(engine.win_height / len(engine.map) * engine.unitblue1.x)
    bb = int(engine.win_height / len(engine.map[0]) * engine.unitblue1.y)
    ar = int(engine.win_height / len(engine.map) * engine.unitred1.x)
    br = int(engine.win_height / len(engine.map[0]) * engine.unitred1.y)
    sendata = 'map'
    map1 = ''
    for i in engine.map:
        for j in i:
            map1 += str(j)
    sendata += map1 + '/'
    if engine.unitred1.helth != 0:
        if engine.unitred1.orient == 'up':
            sendata += str(ar + engine.unitblue1.width//2 + 3)+',' + str(br)+','
            sendata += 'orient red/'
        elif engine.unitred1.orient == 'down':
            sendata += str(ar + engine.unitblue1.width//2 + 3)+',' + str(br + engine.unitred1.height + 5)+','
            sendata += 'orient red/'
        elif engine.unitred1.orient == 'left':
            sendata += str(ar)+',' + str(br + engine.unitblue1.width//2 + 3)+','
            sendata += 'orient red/'
        elif engine.unitred1.orient == 'right':
            sendata += str(ar + engine.unitblue1.width + 5)+',' + str(br + engine.unitblue1.width//2 + 3)+','
            sendata += 'orient red/'
    if engine.unitblue1.helth != 0:
        if engine.unitblue1.orient == 'up':
            sendata += str(ab + engine.unitblue1.width//2 + 3)+',' + str(bb)+','
            sendata += 'orient blue/'
        elif engine.unitblue1.orient == 'down':
            sendata += str(ab + engine.unitblue1.width//2 + 3)+',' + str(bb + engine.unitred1.height + 5)+','
            sendata += 'orient blue/'
        elif engine.unitblue1.orient == 'left':
            sendata += str(ab)+',' + str(bb + engine.unitblue1.width//2 + 3)+','
            sendata += 'orient blue/'
        elif engine.unitblue1.orient == 'right':
            sendata += str(ab + engine.unitblue1.width + 5)+',' + str(bb + engine.unitblue1.width//2 + 3)+','
            sendata += 'orient blue/'
    for bullet in bullets:
        x, y = int(bullet.x*len(engine.map)/engine.win_height), int(bullet.y*len(engine.map[0])/engine.win_width)
        if x >= 9:
            x -= 1
        if y >= 9:
            y -= 1
        if engine.map[x][y] != 0:
            bullets.pop(bullets.index(bullet))
            for unit in engine.units:
                if unit.x == x and unit.y == y:
                    unit.destroy()
        elif bullet.x < engine.win_height and bullet.x > 0 and bullet.y < engine.win_width and bullet.y > 0:
            bullet.move()
        else:
            bullets.pop(bullets.index(bullet))
    for bullet in bullets:
        sendata += str(bullet.x) + ',' + str(bullet.y) + ',' + 'bullet/'
    sendata += engine.unitred1.reload + ',red re/'
    sendata += engine.unitblue1.reload + ',blue re/'
    sendata += str(engine.score[0]) + ',' + str(engine.score[1]) + ',' + 'score/'
    sendata += str(engine.unitblue1.bullets) + ',' + engine.unitblue1.bullet + ',' + 'blue bul1/'
    sendata += str(engine.unitred1.bullets) + ',' + engine.unitred1.bullet + ',' + 'red bul1/'
    sendata += str(engine.unitred1.helth) + ',' + 'red helth/'
    sendata += str(engine.unitblue1.helth) + ',' + 'blue helth/'
    for unit in engine.units:
        if unit.helth != 0:
            a, b, c, d = int(engine.win_height / len(engine.map) * unit.x)+5, int(engine.win_height / len(engine.map[0]) * unit.y) + unit.height // 2, engine.unitred1.width, 10
            a1, b1, c1, d1 = int(engine.win_height / len(engine.map) * unit.x)+5, int(engine.win_height / len(engine.map[0]) * unit.y) + unit.height // 2 + 2, engine.UnitRed.width * unit.helth // 5, 6
            sendata += str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + ',' + str(a1) + ',' + str(b1) + ',' + str(c1) + ',' + str(d1) + ',' + unit.name + ',hp/'
    conn.send(sendata.encode())
bullets = []
engine.gen()
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)
conn1, addr1 = sock.accept()
engine.unitred1.name = conn1.recv(512).decode()
conn1.send('1'.encode())
conn2, addr2 = sock.accept()
engine.unitblue1.name = conn2.recv(512).decode()
conn2.send('2'.encode())
while True:
    parser(conn2.recv(512).decode())
    parser(conn1.recv(512).decode())
    sender(conn2)
    sender(conn1)
