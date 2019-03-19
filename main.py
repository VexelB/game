import pygame
import socket
import gameclient
win_width = win_height = 300
ip = '94.103.84.146'
name = ''
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
create = myfont.render('1: Играц', False, (250, 250, 250))
join = myfont.render('2: Играть по локалке', False, (250, 250, 250))
inp = myfont.render('Введите ип:', False, (250, 250, 250))
np = myfont.render('Введите name (max 6 символов):', False, (250, 250, 250))
qq = myfont.render('0', False, (250, 250, 250))
ww = myfont.render('1', False, (250, 250, 250))
ee = myfont.render('2', False, (250, 250, 250))
rr = myfont.render('3', False, (250, 250, 250))
tt = myfont.render('4', False, (250, 250, 250))
yy = myfont.render('5', False, (250, 250, 250))
uu = myfont.render('6', False, (250, 250, 250))
ii = myfont.render('7', False, (250, 250, 250))
oo = myfont.render('8', False, (250, 250, 250))
pp = myfont.render('9', False, (250, 250, 250))
aa = myfont.render('.', False, (250, 250, 250))

keys = []
chars = list('qwertyuiopasdfghjklzxcvbnm1234567890.')
for i in chars:
    keys.append([i])
for i in keys:
    i.append(myfont.render(i[0], False, (250, 250, 250)))
keys = dict(keys)
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Танчики")
init = False

def nameinput(ip = ip, host = False):
    run = True
    blits = []
    while run:
        win.fill((0,0,0))
        win.blit(np, (10, 140))
        for bb in blits:
            win.blit(bb, (12*zz, 160))
            zz += 1
        zz = 1
        global name
        if host:
            win.blit(pygame.font.SysFont('Comic Sans MS', 22).render('Поделитесь этим ip со своим другом', False, (250, 250, 250)), (10, win_height - 50))
            try:
                aa = str(socket.gethostbyname(socket.gethostname()))
            except:
                aa = '!не получается получить ваш ip!'
            win.blit(pygame.font.SysFont('Comic Sans MS', 25).render(aa, False, (250, 250, 250)), (10, win_height - 30))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if len(blits) < 6:
                    if event.key == pygame.K_q or event.key == 171:
                        name += 'q'
                        blits.append(keys['q'])
                    elif event.key == pygame.K_w or event.key == 172:
                        name += 'w'
                        blits.append(keys['w'])
                    elif event.key == pygame.K_e or event.key == 173:
                        name += 'e'
                        blits.append(keys['e'])
                    elif event.key == pygame.K_r or event.key == 174:
                        name += 'r'
                        blits.append(keys['r'])
                    elif event.key == pygame.K_t or event.key == 176:
                        name += 't'
                        blits.append(keys['t'])
                    elif event.key == pygame.K_y or event.key == 175:
                        name += 'y'
                        blits.append(keys['y'])
                    elif event.key == pygame.K_u or event.key == 179:
                        name += 'u'
                        blits.append(keys['u'])
                    elif event.key == pygame.K_i or event.key == 181:
                        name += 'i'
                        blits.append(keys['i'])
                    elif event.key == pygame.K_o or event.key == 178:
                        name += 'o'
                        blits.append(keys['o'])
                    elif event.key == pygame.K_p or event.key == 182:
                        name += 'p'
                        blits.append(keys['p'])
                    elif event.key == pygame.K_a or event.key == 160:
                        name += 'a'
                        blits.append(keys['a'])
                    elif event.key == pygame.K_s or event.key == 161:
                        name += 's'
                        blits.append(keys['s'])
                    elif event.key == pygame.K_d or event.key == 162:
                        name += 'd'
                        blits.append(keys['d'])
                    elif event.key == pygame.K_f or event.key == 163:
                        name += 'f'
                        blits.append(keys['f'])
                    elif event.key == pygame.K_g or event.key == 165:
                        name += 'g'
                        blits.append(keys['g'])
                    elif event.key == pygame.K_h or event.key == 164:
                        name += 'h'
                        blits.append(keys['h'])
                    elif event.key == pygame.K_j or event.key == 184:
                        name += 'j'
                        blits.append(keys['j'])
                    elif event.key == pygame.K_k or event.key == 186:
                        name += 'k'
                        blits.append(keys['k'])
                    elif event.key == pygame.K_l or event.key == 183:
                        name += 'l'
                        blits.append(keys['l'])
                    elif event.key == pygame.K_z or event.key == 166:
                        name += 'z'
                        blits.append(keys['z'])
                    elif event.key == pygame.K_x or event.key == 167:
                        name += 'x'
                        blits.append(keys['x'])
                    elif event.key == pygame.K_c or event.key == 168:
                        name += 'c'
                        blits.append(keys['c'])
                    elif event.key == pygame.K_v or event.key == 169:
                        name += 'v'
                        blits.append(keys['v'])
                    elif event.key == pygame.K_b or event.key == 170:
                        name += 'b'
                        blits.append(keys['b'])
                    elif event.key == pygame.K_n or event.key == 190:
                        name += 'n'
                        blits.append(keys['n'])
                    elif event.key == pygame.K_m or event.key == 191:
                        name += 'm'
                        blits.append(keys['m'])
                if event.key == pygame.K_BACKSPACE and len(blits) != 0:
                    blits.pop()
                    name = name[:len(name)-1:]
                if event.key == pygame.K_RETURN:
                    if host:
                        #gameserv.init(name = name)
                        print('mda')
                    else:
                        loop = True
                        i = 0
                        while loop:
                            try:
                                sock = socket.create_connection((ip, 9090))
                                loop = False
                            except ConnectionRefusedError:
                                if i == 0:
                                    print('-------------------------------------------------------------------')
                                    print("server is off, you can wait or CTRL+C and find out what's going on")
                                    print('-------------------------------------------------------------------')
                                    i += 1
                            except Exception as eq:
                                print(eq)
                        sock.send(name.encode())
                        num = sock.recv(512).decode()
                        gameclient.init(name = name, ip = ip, sock = sock, num = num)
                        pygame.display.set_mode((win_width, win_height))
                        name = ''
                        run = False

def ipinput():
    run = True
    blits = []
    while run:
        z = 1
        global ip
        ip = ''
        win.fill((0,0,0))
        win.blit(inp, (10, 140))
        for b in blits:
            win.blit(b, (10*z, 160))
            z += 1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_0:
                    ip += '0'
                    blits.append(keys['0'])
                if event.key == pygame.K_1:
                    ip += '1'
                    blits.append(keys['1'])
                if event.key == pygame.K_2:
                    ip += '2'
                    blits.append(keys['2'])
                if event.key == pygame.K_3:
                    ip += '3'
                    blits.append(keys['3'])
                if event.key == pygame.K_4:
                    ip += '4'
                    blits.append(keys['4'])
                if event.key == pygame.K_5:
                    ip += '5'
                    blits.append(keys['5'])
                if event.key == pygame.K_6:
                    ip += '6'
                    blits.append(keys['6'])
                if event.key == pygame.K_7:
                    ip += '7'
                    blits.append(keys['7'])
                if event.key == pygame.K_8:
                    ip += '8'
                    blits.append(keys['8'])
                if event.key == pygame.K_9:
                    ip += '9'
                    blits.append(keys['9'])
                if event.key == 46 or event.key == 192:
                    ip += '.'
                    blits.append(keys['.'])
                if event.key == pygame.K_BACKSPACE:
                    blits.pop()
                    ip = ip[:len(ip)-1:]
                if event.key == pygame.K_RETURN:
                    #nameinput(ip)
                    print('mda')
                    run = False

def bot():
    pass

def k2():
    run = True
    while run:
        win.fill((0,0,0))
        win.blit(myfont.render('1. Хостить:', False, (250, 250, 250)),(10,120))
        win.blit(myfont.render('2. ПРисоединица:', False, (250, 250, 250)),(10,150))
        win.blit(pygame.font.SysFont('Comic Sans MS', 22).render('Поделитесь этим ip со своим другом', False, (250, 250, 250)), (10, win_height - 50))
        try:
            a = str(socket.gethostbyname(socket.gethostname()))
        except:
            a = '!не получается получить ваш ip!'
        win.blit(pygame.font.SysFont('Comic Sans MS', 25).render(a, False, (250, 250, 250)), (10, win_height - 30))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_1:
                    nameinput(host = True)
                if event.key == pygame.K_2:
                    ipinput()

run = True
while run:
    try:
        win.fill((0,0,0))
        win.blit(create,(10,120))
        win.blit(join,(10,150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nameinput()
                if event.key == pygame.K_2:
                    k2()
                #if event.key == pygame.K_3:
                #    loop = True
                #    i = 0
                #    while loop:
                #        try:
                #            sock = socket.create_connection((ip, 9090))
                #            loop = False
                #        except ConnectionRefusedError:
                #            if i == 0:
                #                print('-------------------------------------------------------------------')
                #                print("server is off, you can wait or CTRL+C and find out what's going on")
                #                print('-------------------------------------------------------------------')
                #                i += 1
                #        except Exception as eq:
                #            print(eq)
                #    sock.send('|bot'.encode())
                #    num = sock.recv(512).decode()
                #    print(num)
                #    gameclient.init(name = name, ip = ip, sock = sock, num = num)
                #    run = False
    except:
        run = False
pygame.quit()
