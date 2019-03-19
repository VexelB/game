import socket
import engine
import time

def reinit(j):
    j = j//2
    j = j*2
    if engine.units[j].reload == 'yes' and engine.units[j+1].reload == 'yes':
            engine.map = [[0 for i in range(9)] for j in range(9)]
            engine.gen()
            engine.maps[j//2] = engine.map
            bullets[j//2] = []
            engine.units[j].__init__(j//2)
            engine.units[j+1].__init__(j//2)

def parser(data1, j):
    dataset = data1.split('/')
    for data in dataset:
        if engine.units[j].helth != 0:
            if data == 'up' and engine.units[j].y > 0:
                engine.units[j].move(engine.units[j].x, engine.units[j].y-1, j//2)
            elif data == 'down' and engine.units[j].y < 8:
                engine.units[j].move(engine.units[j].x, engine.units[j].y+1, j//2)
            elif data == 'left' and engine.units[j].x > 0:
                engine.units[j].move(engine.units[j].x-1, engine.units[j].y, j//2)
            elif data == 'right' and engine.units[j].x < 8:
                engine.units[j].move(engine.units[j].x+1, engine.units[j].y, j//2)
            elif data == 'w':
                engine.units[j].orient = 'up'
            elif data == 's':
                engine.units[j].orient = 'down'
            elif data == 'a':
                engine.units[j].orient = 'left'
            elif data == 'd':
                engine.units[j].orient = 'right'
            elif data == 'space':
                if engine.units[j].bullet == 'reload':
                    if engine.units[j].bullets == 5:
                        engine.units[j].bullet = 'no'
                    else:
                        engine.units[j].bullets += 1
                if engine.units[j].bullets >= 0 and engine.units[j].bullet != 'reload':
                    engine.units[j].bullets -= 1
                    if engine.units[j].orient == 'up':
                        if engine.units[j].y != 0:
                            bullets[(j)//2].append(engine.Bullet(int(engine.win_height / len(engine.maps[(j)//2]) * engine.units[j].x + engine.units[j].width//2) + 5, int(engine.win_height / len(engine.maps[(j)//2][0]) * engine.units[j].y), engine.units[j].orient, (255, 255, 0)))
                    elif engine.units[j].orient == 'down':
                        if engine.units[j].y !=8:
                            bullets[(j)//2].append(engine.Bullet(int(engine.win_height / len(engine.maps[(j)//2]) * engine.units[j].x + engine.units[j].width//2) + 5, int(engine.win_height / len(engine.maps[(j//2)][0]) * engine.units[j].y + engine.units[j].height + 10), engine.units[j].orient, (255, 255, 0)))
                    elif engine.units[j].orient == 'left':
                        if engine.units[j].x != 0:
                            bullets[j//2].append(engine.Bullet(int(engine.win_height / len(engine.maps[(j)//2]) * engine.units[j].x), int(engine.win_height / len(engine.maps[(j)//2][0]) * engine.units[j].y + engine.units[j].width//2) + 5, engine.units[j].orient, (255, 255, 0)))
                    elif engine.units[j].orient == 'right':
                        if engine.units[j].x != 8:
                            bullets[j//2].append(engine.Bullet(int(engine.win_height / len(engine.maps[(j)//2]) * engine.units[j].x + engine.units[j].width) + 10, int(engine.win_height / len(engine.maps[(j)//2][0]) * engine.units[j].y + engine.units[j].width//2) + 5, engine.units[j].orient, (255, 255, 0)))
                    if engine.units[j].bullets < 1:
                        engine.units[j].bullet = 'reload'
        if data == 'r':
            if engine.units[j].reload == 'no':
                engine.units[j].reload = 'yes'
            else:
                engine.units[j].reload = 'no'
            reinit(j)

def sender(conn, conn1, q):
    ab = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q+1].x)
    bb = int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q+1].y)
    ar = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q].x)
    br = int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q].y)
    sendata = 'map'
    map1 = ''
    for i in engine.maps[q//2]:
        for j in i:
            map1 += str(j)
    sendata += map1 + '/'
    if engine.units[q].helth != 0:
        if engine.units[q].orient == 'up':
            sendata += str(ar + engine.units[q].width//2 + 3)+',' + str(br)+','
            sendata += 'orient red/'
        elif engine.units[q].orient == 'down':
            sendata += str(ar + engine.units[q].width//2 + 3)+',' + str(br + engine.units[q].height + 5)+','
            sendata += 'orient red/'
        elif engine.units[q].orient == 'left':
            sendata += str(ar)+',' + str(br + engine.units[q].width//2 + 3)+','
            sendata += 'orient red/'
        elif engine.units[q].orient == 'right':
            sendata += str(ar + engine.units[q].width + 5)+',' + str(br + engine.units[q].width//2 + 3)+','
            sendata += 'orient red/'
    if engine.units[q+1].helth != 0:
        if engine.units[q+1].orient == 'up':
            sendata += str(ab + engine.units[q+1].width//2 + 3)+',' + str(bb)+','
            sendata += 'orient blue/'
        elif engine.units[q+1].orient == 'down':
            sendata += str(ab + engine.units[q+1].width//2 + 3)+',' + str(bb + engine.units[q+1].height + 5)+','
            sendata += 'orient blue/'
        elif engine.units[q+1].orient == 'left':
            sendata += str(ab)+',' + str(bb + engine.units[q+1].width//2 + 3)+','
            sendata += 'orient blue/'
        elif engine.units[q+1].orient == 'right':
            sendata += str(ab + engine.units[q+1].width + 5)+',' + str(bb + engine.units[q+1].width//2 + 3)+','
            sendata += 'orient blue/'
    for bullet in bullets[q//2]:
        x, y = int(bullet.x*len(engine.maps[q//2])/engine.win_height), int(bullet.y*len(engine.maps[q//2][0])/engine.win_width)
        if x >= 9:
            x -= 1
        if y >= 9:
            y -= 1
        if engine.maps[q//2][x][y] != 0:
            bullets[q//2].pop(bullets[q//2].index(bullet))
            if engine.units[q].x == x and engine.units[q].y == y:
                engine.units[q].destroy(q//2)
            if engine.units[q+1].x == x and engine.units[q+1].y ==y:
                engine.units[q+1].destroy(q//2)
        elif bullet.x < engine.win_height and bullet.x > 0 and bullet.y < engine.win_width and bullet.y > 0:
            bullet.move()
        else:
            bullets[q//2].pop(bullets[q//2].index(bullet))
    for bullet in bullets[q//2]:
        sendata += str(bullet.x) + ',' + str(bullet.y) + ',' + 'bullet/'
    sendata += engine.units[q].reload + ',red re/'
    sendata += engine.units[q+1].reload + ',blue re/'
    sendata += str(engine.score[q//2][0]) + ',' + str(engine.score[q//2][1]) + ',' + 'score/'
    sendata += str(engine.units[q+1].bullets) + ',' + engine.units[q+1].bullet + ',' + 'blue bul1/'
    sendata += str(engine.units[q].bullets) + ',' + engine.units[q].bullet + ',' + 'red bul1/'
    sendata += str(engine.units[q].helth) + ',' + 'red helth/'
    sendata += str(engine.units[q+1].helth) + ',' + 'blue helth/'
    if engine.units[q].helth != 0:
        a, b, c, d = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q].x)+5, int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q].y) + engine.units[q].height // 2, engine.units[q].width, 10
        a1, b1, c1, d1 = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q].x)+5, int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q].y) + engine.units[q].height // 2 + 2, engine.UnitRed.width * engine.units[q].helth // 5, 6
        sendata += str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + ',' + str(a1) + ',' + str(b1) + ',' + str(c1) + ',' + str(d1) + ',' + engine.units[q].name + ',hp/'
    if engine.units[q+1].helth != 0:
        a, b, c, d = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q+1].x)+5, int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q+1].y) + engine.units[q+1].height // 2, engine.units[q+1].width, 10
        a1, b1, c1, d1 = int(engine.win_height / len(engine.maps[q//2]) * engine.units[q+1].x)+5, int(engine.win_height / len(engine.maps[q//2][0]) * engine.units[q+1].y) + engine.units[q+1].height // 2 + 2, engine.UnitBlue.width * engine.units[q+1].helth // 5, 6
        sendata += str(a) + ',' + str(b) + ',' + str(c) + ',' + str(d) + ',' + str(a1) + ',' + str(b1) + ',' + str(c1) + ',' + str(d1) + ',' + engine.units[q+1].name + ',hp/'
    conn.send(sendata.encode())
    conn1.send(sendata.encode())

i = 0
conns = []
addrs = []
bullets = []
sock = socket.socket()
sock.bind(('', 9090))
sock.settimeout(0.0000001)
sock.listen(2)
while True:
    log = open("log.txt", "a")
    try:
        conn, addr = sock.accept()
        if i%2 == 0:
            bullets.append([])
            engine.score.append([0, 0])
            engine.map = [[0 for i in range(9)] for j in range(9)]
            engine.gen()
            engine.maps.append(engine.map)
            engine.units.append(engine.UnitRed(i//2))
            try:
                engine.units[i].name = conn.recv(512).decode()
                if len(engine.units[i].name) > 6:
                    conn.close()
                    engine.maps.pop(i//2)
                    engine.units.pop(i)
                    engine.score.pop(j//2)
                    bullets.pop(j//2)
                    i -= 1
            except:
                conn.close()
                engine.maps.pop(i//2)
                engine.units.pop(i)
                engine.score.pop(j//2)
                bullets.pop(j//2)
                i -= 1
            if engine.units[i].name == '|bot':
                conns.append(conn)
                addrs.append(addr)
                i += 1
                engine.units.append(engine.UnitBlue(i//2))
                engine.units[i].name = '|bot'
                log.write(time.ctime(time.time())+ " Bot Conn:"+conns[i]+'\n')
            conns.append(conn)
            addrs.append(addr)
        elif i%2 == 1:
            engine.units.append(engine.UnitBlue(i//2))
            engine.units[i].name = conn.recv(512).decode()
            conns.append(conn)
            addrs.append(addr)
            conns[i].send(str(i%2).encode())
            conns[i-1].send(str((i-1)%2).encode())
            log.write(f"{time.ctime(time.time())} Conns: i = {i} units = {len(engine.units)}\n")
            j = 0
            while j < len(conns) - 1:
                log.write(f"                              {j//2}: {addrs[j]} {str(engine.units[j])[8:13:]} |{j}| name = '{engine.units[j].name}'  {addrs[j+1]} {str(engine.units[j+1])[8:13:]} |{j+1}| name = '{engine.units[j+1].name}'\n")
                j += 2
        i += 1
    except Exception as e:
        if type(e) != socket.timeout:
            log.write(f"{time.ctime(time.time())} There is an error with conectiong: {str(e)} \n")
    if len(conns) > 1:
        j = 0
        m = 0
        while j < len(conns) - 1:
            try:
                if addrs[j] != addrs[j+1]:
                    parser(conns[j+1].recv(512).decode(), j+1)
                parser(conns[j].recv(512).decode(), j)
                sender(conns[j], conns[j+1], j)
            except Exception as e:
                log.write(f"{time.ctime(time.time())} Closed Conn: {str(e)}\n")
                log.write(f"                              {j//2}: score: {engine.score[j//2]}\n")
                log.write(f"                              users: {engine.units[j].name} {addrs[j]} {engine.units[j+1].name} {addrs[j+1]} \n")
                conns[j].close()
                conns.pop(j)
                conns[j].close()
                conns.pop(j)
                addrs.pop(j)
                addrs.pop(j)
                engine.maps.pop(j//2)
                engine.units.pop(j)
                engine.units.pop(j)
                engine.score.pop(j//2)
                bullets.pop(j//2)
                i -= 2
            j += 2
    log.close()
