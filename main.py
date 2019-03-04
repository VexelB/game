import socket
import pygame
import gameserv
import gameclient
win_width = win_height = 300
ip = ''
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
create = myfont.render('1: Играц', False, (250, 250, 250))
join = myfont.render('2: Играть по локалке', False, (250, 250, 250))
inp = myfont.render('Введите ип:', False, (250, 250, 250))
q = myfont.render('0', False, (250, 250, 250))
w = myfont.render('1', False, (250, 250, 250))
e = myfont.render('2', False, (250, 250, 250))
r = myfont.render('3', False, (250, 250, 250))
t = myfont.render('4', False, (250, 250, 250))
y = myfont.render('5', False, (250, 250, 250))
u = myfont.render('6', False, (250, 250, 250))
i = myfont.render('7', False, (250, 250, 250))
o = myfont.render('8', False, (250, 250, 250))
p = myfont.render('9', False, (250, 250, 250))
a = myfont.render('.', False, (250, 250, 250))
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("StepGame")
init = False
def ipinput():

    run = True
    blits = []
    while run:
        z = 1
        global ip
        win.fill((0,0,0))
        win.blit(inp, (10, 140))
        for b in blits:
            win.blit(b, (10*z, 160))
            z += 1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ip += '0'
                    blits.append(q)
                if event.key == pygame.K_1:
                    ip += '1'
                    blits.append(w)
                if event.key == pygame.K_2:
                    ip += '2'
                    blits.append(e)
                if event.key == pygame.K_3:
                    ip += '3'
                    blits.append(r)
                if event.key == pygame.K_4:
                    ip += '4'
                    blits.append(t)
                if event.key == pygame.K_5:
                    ip += '5'
                    blits.append(y)
                if event.key == pygame.K_6:
                    ip += '6'
                    blits.append(u)
                if event.key == pygame.K_7:
                    ip += '7'
                    blits.append(i)
                if event.key == pygame.K_8:
                    ip += '8'
                    blits.append(o)
                if event.key == pygame.K_9:
                    ip += '9'
                    blits.append(p)
                if event.key == 46:
                    ip += '.'
                    blits.append(a)
                if event.key == pygame.K_BACKSPACE:
                    blits.pop()
                    ip = ip[:len(ip)-1:]
                if event.key == pygame.K_RETURN:
                    gameclient.init(ip)

def k2():
    while True:
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
                if event.key == pygame.K_1:
                    gameserv.init(local = True)
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
                #sock = socket.create_connection(('localhost', 9090))
                #data = sock.recv(512).decode()
                gameclient.init()
            if event.key == pygame.K_2:
                k2()
    win.fill((0,0,0))
    win.blit(create,(10,120))
    win.blit(join,(10,150))
    pygame.display.update()
pygame.quit()
