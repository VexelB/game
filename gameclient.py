import pygame
import socket

pygame.init()
win_height = win_width = 500
score = [0, 0]

class Interface:
    myfont = pygame.font.SysFont('Comic Sans MS', win_height//23)
    info = myfont.render('Переключение:', False, (250, 250, 250))
    atck = myfont.render('1: Атаковать (СПАСЕ)', False, (250, 250, 250))
    heal = myfont.render('2: Хилить (СПАСЕ)', False, (250, 250, 250))
    deff = myfont.render('3: Поддержка (КОНСТ)', False, (250, 250, 250))
    opts = myfont.render('Управление:', False, (250, 250, 250))
    wsad = myfont.render('Целиться: WSAD', False, (250, 250, 250))
    udrl = myfont.render('ЕЗДЕТЬ: стрелочки', False, (250, 250, 250))
    spce = myfont.render('Стрилять: SPACE', False, (250, 250, 250))
    rrrr = myfont.render('R', False, (250, 250, 250))
    def draw(self, win):
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
        win.blit(pygame.font.SysFont('Comic Sans MS', win_height//23).render(f'Красных очков: {score[0]}', False, (250, 250, 250)), (win_width//50, win_height//100))
        win.blit(pygame.font.SysFont('Comic Sans MS', win_height//23).render(f'Синих очков: {score[1]}', False, (250, 250, 250)), (win_width//50, (win_height//100+win_height//20)))

def init(ip = 'localhost', name = 'Jendos'):

    def parser():
        global score
        data1 = sock.recv(512).decode()
        dataset = data1.split('/')
        for data in dataset:
            if 'bul1' in data:
                pygame.draw.rect(win, (250, 250, 250), (win_width-75, 0, 5, 15))
                pygame.draw.rect(win, (250, 250, 250), (win_width-75, 10, 75, 5))
                if num == '0' and 'red' in data:
                    data1 = data.split(',')
                    try:
                        int(data1[0])
                    except:
                        data1[0] = 0
                    for i in range(int(data1[0])):
                        pygame.draw.circle(win, (250, 250, 0), ((win_height-5)-15*i, 5), win_width//100)
                        if data1[1] == 'reload':
                            pygame.draw.rect(win, (0, 250, 0), ((win_height-10)-15*i, 0, win_width//25, win_height//50))
                elif num == '1' and 'blue' in data:
                    data1 = data.split(',')
                    try:
                        int(data1[0])
                    except:
                        print(data)
                    for i in range(int(data1[0])):
                        pygame.draw.circle(win, (250, 250, 0), ((win_height-5)-15*i, 5), win_width//100)
                        if data1[1] == 'reload':
                            pygame.draw.rect(win, (0, 250, 0), ((win_height-10)-15*i, 0, win_width//25, win_height//50))
            elif 'map' in data:
                q = 3
                for i in range(len(map)):
                    for j in range(len(map[0])):
                        map[i][j] = int(data[q])
                        q += 1
            elif 'hp' in data:
                data1 = data.split(',')
                try:
                    pygame.draw.rect(win, (0, 0, 0), (int(float(data1[0])), int(float(data1[1])), int(float(data1[2])), int(float(data1[3]))))
                except:
                    pass
                try:
                    pygame.draw.rect(win, (250, 250, 250), (int(float(data1[4])), int(float(data1[5])), int(float(data1[6])), int(float(data1[7]))))
                except:
                    #pygame.draw.rect(win, (250, 250, 250), (5, int(float(data1[4])), int(float(data1[5])), int(float(data1[6]))))
                    pass
                try:
                    win.blit(pygame.font.SysFont('Comic Sans MS', win_height//23).render(data1[8], False, (250, 250, 250)), (int(float(data1[4])), int(float(data1[5])-win_height//10//2+3)))
                except:
                    pass
            elif 'orient' in data:
                if 'red' in data:
                    data1 = data.split(',')
                    pygame.draw.rect(win, (250, 0, 0), (int(float(data1[0])), int(float(data1[1])), win_height//100, win_height//100))
                elif 'blue' in data:
                    data1 = data.split(',')
                    if len(data1) > 1:
                        pygame.draw.rect(win, (0, 0, 250), (int(float(data1[0])), int(float(data1[1])), win_height//100, win_height//100))
            elif 'bullet' in data:
                data1 = data.split(',')
                pygame.draw.circle(win, (250, 250, 0), (int(data1[0]), int(data1[1])), win_width//100)
            elif 'score' in data:
                data1 = data.split(',')
                try:
                    int(data1[0])
                    int(data1[1])
                except:
                    print(data)
                try:
                    score[0], score[1] = int(data1[0]), int(data1[1])
                except:
                    pass
            elif 're' in data:
                if 'red' in data:
                    data1 = data.split(',')
                    if data1[0] == 'yes':
                        pygame.draw.rect(win, (250, 0, 0), (win_height//20*19, win_height+win_height//5//2+20, 15, 15))
                if 'blue' in data:
                    data1 = data.split(',')
                    if data1[0] == 'yes':
                        pygame.draw.rect(win, (0, 0, 250), (win_height//20*19, win_height+win_height//5//2-20, 15, 15))
        pygame.display.update()

    def draw():
        win.fill((0, 0, 0))
        for i in range(len(map)):
            for j in range(len(map[0])):
                x = win_height / 9 * i
                y = win_width / 9 * j
                if map[i][j] == 1:
                    pygame.draw.rect(win, (250, 0, 0), (x+5, y+5, win_height/10, win_height/10))
                if map[i][j] == 2:
                    pygame.draw.rect(win, (0, 0, 250), (x+5, y+5, win_height/10, win_height/10))
                if map[i][j] == 3:
                    pygame.draw.rect(win, (250, 250, 250), (x+5, y+5, win_height/10, win_height/10))
        interface.draw(win)

    global score
    interface = Interface()
    sock = socket.create_connection((ip, 9090))
    sock.send(name.encode())
    num = sock.recv(512).decode()
    map = [[0 for i in range(9)] for j in range(9)]
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("Танчики")
    while True:
        sock.send('1/'.encode())
        draw()
        parser()
        if num == '0':
            sendata = 'red/'
        if num == '1':
            sendata = 'blue/'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == 172:
                    sendata += 'w/'
                if event.key == pygame.K_s or event.key == 161:
                    sendata += 's/'
                if event.key == pygame.K_a or event.key == 160:
                    sendata += 'a/'
                if event.key == pygame.K_d or event.key == 162:
                    sendata += 'd/'
                if event.key == pygame.K_SPACE:
                    sendata += 'space/'
                if event.key == pygame.K_LEFT:
                    sendata += 'left/'
                if event.key == pygame.K_RIGHT:
                    sendata += 'right/'
                if event.key == pygame.K_UP:
                    sendata += 'up/'
                if event.key == pygame.K_DOWN:
                    sendata += 'down/'
                if event.key == pygame.K_r or event.key == 174:
                    sendata += 'r/'
        if sendata != 'blue/' and sendata != 'red/':
            sock.send((sendata).encode())
if __name__ == '__main__':
    init()
