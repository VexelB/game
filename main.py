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
q = myfont.render('q', False, (250, 250, 250))
w = myfont.render('w', False, (250, 250, 250))
e = myfont.render('e', False, (250, 250, 250))
r = myfont.render('r', False, (250, 250, 250))
t = myfont.render('t', False, (250, 250, 250))
y = myfont.render('y', False, (250, 250, 250))
u = myfont.render('u', False, (250, 250, 250))
iq = myfont.render('i', False, (250, 250, 250))
o = myfont.render('o', False, (250, 250, 250))
p = myfont.render('p', False, (250, 250, 250))
a = myfont.render('a', False, (250, 250, 250))
s = myfont.render('s', False, (250, 250, 250))
d = myfont.render('d', False, (250, 250, 250))
f = myfont.render('f', False, (250, 250, 250))
g = myfont.render('g', False, (250, 250, 250))
h = myfont.render('h', False, (250, 250, 250))
j = myfont.render('j', False, (250, 250, 250))
k = myfont.render('k', False, (250, 250, 250))
l = myfont.render('l', False, (250, 250, 250))
z = myfont.render('z', False, (250, 250, 250))
x = myfont.render('x', False, (250, 250, 250))
c = myfont.render('c', False, (250, 250, 250))
v = myfont.render('v', False, (250, 250, 250))
b = myfont.render('b', False, (250, 250, 250))
n = myfont.render('n', False, (250, 250, 250))
m = myfont.render('m', False, (250, 250, 250))
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if len(blits) < 6:
                    if event.key == pygame.K_q or event.key == 171:
                        name += 'q'
                        blits.append(q)
                    elif event.key == pygame.K_w or event.key == 172:
                        name += 'w'
                        blits.append(w)
                    elif event.key == pygame.K_e or event.key == 173:
                        name += 'e'
                        blits.append(e)
                    elif event.key == pygame.K_r or event.key == 174:
                        name += 'r'
                        blits.append(r)
                    elif event.key == pygame.K_t or event.key == 176:
                        name += 't'
                        blits.append(t)
                    elif event.key == pygame.K_y or event.key == 175:
                        name += 'y'
                        blits.append(y)
                    elif event.key == pygame.K_u or event.key == 179:
                        name += 'u'
                        blits.append(u)
                    elif event.key == pygame.K_i or event.key == 181:
                        name += 'i'
                        blits.append(iq)
                    elif event.key == pygame.K_o or event.key == 178:
                        name += 'o'
                        blits.append(o)
                    elif event.key == pygame.K_p or event.key == 182:
                        name += 'p'
                        blits.append(p)
                    elif event.key == pygame.K_a or event.key == 160:
                        name += 'a'
                        blits.append(a)
                    elif event.key == pygame.K_s or event.key == 161:
                        name += 's'
                        blits.append(s)
                    elif event.key == pygame.K_d or event.key == 162:
                        name += 'd'
                        blits.append(d)
                    elif event.key == pygame.K_f or event.key == 163:
                        name += 'f'
                        blits.append(f)
                    elif event.key == pygame.K_g or event.key == 165:
                        name += 'g'
                        blits.append(g)
                    elif event.key == pygame.K_h or event.key == 164:
                        name += 'h'
                        blits.append(h)
                    elif event.key == pygame.K_j or event.key == 184:
                        name += 'j'
                        blits.append(j)
                    elif event.key == pygame.K_k or event.key == 186:
                        name += 'k'
                        blits.append(k)
                    elif event.key == pygame.K_l or event.key == 183:
                        name += 'l'
                        blits.append(l)
                    elif event.key == pygame.K_z or event.key == 166:
                        name += 'z'
                        blits.append(z)
                    elif event.key == pygame.K_x or event.key == 167:
                        name += 'x'
                        blits.append(x)
                    elif event.key == pygame.K_c or event.key == 168:
                        name += 'c'
                        blits.append(c)
                    elif event.key == pygame.K_v or event.key == 169:
                        name += 'v'
                        blits.append(v)
                    elif event.key == pygame.K_b or event.key == 170:
                        name += 'b'
                        blits.append(b)
                    elif event.key == pygame.K_n or event.key == 190:
                        name += 'n'
                        blits.append(n)
                    elif event.key == pygame.K_m or event.key == 191:
                        name += 'm'
                        blits.append(m)
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
                        run = False
        pygame.display.update()

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
                    blits.append(qq)
                if event.key == pygame.K_1:
                    ip += '1'
                    blits.append(ww)
                if event.key == pygame.K_2:
                    ip += '2'
                    blits.append(ee)
                if event.key == pygame.K_3:
                    ip += '3'
                    blits.append(rr)
                if event.key == pygame.K_4:
                    ip += '4'
                    blits.append(tt)
                if event.key == pygame.K_5:
                    ip += '5'
                    blits.append(yy)
                if event.key == pygame.K_6:
                    ip += '6'
                    blits.append(uu)
                if event.key == pygame.K_7:
                    ip += '7'
                    blits.append(ii)
                if event.key == pygame.K_8:
                    ip += '8'
                    blits.append(oo)
                if event.key == pygame.K_9:
                    ip += '9'
                    blits.append(pp)
                if event.key == 46 or event.key == 192:
                    ip += '.'
                    blits.append(aa)
                if event.key == pygame.K_BACKSPACE:
                    blits.pop()
                    ip = ip[:len(ip)-1:]
                if event.key == pygame.K_RETURN:
                    #nameinput(ip)
                    print('mda')

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
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                nameinput()
            if event.key == pygame.K_2:
                k2()
    win.fill((0,0,0))
    win.blit(create,(10,120))
    win.blit(join,(10,150))
    pygame.display.update()
pygame.quit()
