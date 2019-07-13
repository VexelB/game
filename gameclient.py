import pygame
import socket
import time

pygame.init()
win_height = win_width = 500
score = [0, 0]

class Interface:
    myfont = pygame.font.SysFont('Comic Sans MS', win_height//23)
    info = myfont.render('Переключение:', False, (250, 250, 250))
    atck = myfont.render('1нету: Атаковать (СПАСЕ)', False, (250, 250, 250))
    heal = myfont.render('2еще: Хилить (СПАСЕ)', False, (250, 250, 250))
    deff = myfont.render('3нету: Поддержка (КОНСТ)', False, (250, 250, 250))
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
        win.blit(self.rrrr, (win_height//20*19, win_height+win_height//5//2-15))
        win.blit(self.myfont.render(f'Красных очков: {score[0]}', False, (250, 250, 250)), (win_width//50, win_height//100))
        win.blit(self.myfont.render(f'Синих очков: {score[1]}', False, (250, 250, 250)), (win_width//50, (win_height//100+win_height//20)))

def init(ip = 'localhost', name = 'Jendos', sock = None, num = 0):

    def parser(data1):
        win.fill((0, 0, 0))
        global score
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
                        data1[0] = 0
                    for i in range(int(data1[0])):
                        pygame.draw.circle(win, (250, 250, 0), ((win_height-5)-15*i, 5), win_width//100)
                        if data1[1] == 'reload':
                            pygame.draw.rect(win, (0, 250, 0), ((win_height-10)-15*i, 0, win_width//25, win_height//50))
            elif 'map' in data:
                q = 3
                for i in range(len(map)):
                    for j in range(len(map[0])):
                        if num == '0':
                            map[i][j] = int(data[q])
                        elif num == '1':
                            map[len(map)-1-i][len(map[0])-1-j] = int(data[q])
                        q += 1
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
            elif 'hp' in data:
                data1 = data.split(',')
                if num == '0':
                    try:
                        pygame.draw.rect(win, (0, 0, 0), (int(float(data1[0])), int(float(data1[1])), int(float(data1[2])), int(float(data1[3]))))
                    except Exception as e:
                        print(e)
                    try:
                        pygame.draw.rect(win, (250, 250, 250), (int(float(data1[4])), int(float(data1[5])), int(float(data1[6])), int(float(data1[7]))))
                    except Exception as e:
                        print(e)
                    try:
                        if data1[8] != '|bot':
                            win.blit(pygame.font.SysFont('Comic Sans MS', win_height//23).render(data1[8], False, (250, 250, 250)), (int(float(data1[4])), int(float(data1[5])-win_height//10//2+3)))
                    except Exception as e:
                        print(e)
                elif num == '1':
                    try:
                        pygame.draw.rect(win, (0, 0, 0), (int(win_width - float(data1[0]) - win_width//10+4), int(win_height - float(data1[1])), int(float(data1[2])), int(float(data1[3]))))
                    except Exception as e:
                        print(e)
                    try:
                        pygame.draw.rect(win, (250, 250, 250), (int(win_width - float(data1[4]) - win_width//10+4), int(win_height - float(data1[5])+3), int(float(data1[6])), int(float(data1[7]))))
                    except Exception as e:
                        print(e)
                    try:
                        if data1[8] != '|bot':
                            win.blit(pygame.font.SysFont('Comic Sans MS', win_height//23).render(data1[8], False, (250, 250, 250)), (int(win_width - float(data1[4]) - win_width//10+5), int( win_height - float(data1[5])-win_height//10//2+3)))
                    except Exception as e:
                        print(e)
            elif 'orient' in data:
                if num == '0':
                    if 'red' in data:
                        data1 = data.split(',')
                        pygame.draw.rect(win, (250, 0, 0), (int(float(data1[0])), int(float(data1[1])), win_height//100, win_height//100))
                    elif 'blue' in data:
                        data1 = data.split(',')
                        if len(data1) > 1:
                            pygame.draw.rect(win, (0, 0, 250), (int(float(data1[0])), int(float(data1[1])), win_height//100, win_height//100))
                elif num == '1':
                    if 'red' in data:
                        data1 = data.split(',')
                        pygame.draw.rect(win, (250, 0, 0), (int(win_width - float(data1[0])), int(win_height - float(data1[1])), win_height//100, win_height//100))
                    elif 'blue' in data:
                        data1 = data.split(',')
                        if len(data1) > 1:
                            pygame.draw.rect(win, (0, 0, 250), (int(win_width - float(data1[0])), int(win_height - float(data1[1])), win_height//100, win_height//100))
            elif 'bullet' in data:
                data1 = data.split(',')
                if num == '0':
                    pygame.draw.circle(win, (250, 250, 0), (int(data1[0]), int(data1[1])), win_width//100)
                elif num == '1':
                    pygame.draw.circle(win, (250, 250, 0), (win_width - int(data1[0]) + win_width//100, win_height - int(data1[1]) + win_width//100), win_width//100)
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
                        pygame.draw.rect(win, (250, 0, 0), (win_height//20*19, win_height+win_height//5//2+5, 15, 15))
                if 'blue' in data:
                    data1 = data.split(',')
                    if data1[0] == 'yes':
                        pygame.draw.rect(win, (0, 0, 250), (win_height//20*19, win_height+win_height//5//2-35, 15, 15))

    global score
    map = [[0 for i in range(9)] for j in range(9)]
    interface = Interface()
    pygame.display.set_caption("Танчики")
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    if sock == None:
        loop = True
        i = 0
        while loop:
            try:
                sock = socket.create_connection((ip, 9090))
                loop = False
                sock.send(name.encode())
                num = sock.recv(512).decode()
            except ConnectionRefusedError:
                if i == 0:
                    print('--------------------------------------------------------------------------')
                    print("server is anavailable, you can wait or CTRL+C and find out what's going on")
                    print('--------------------------------------------------------------------------')
                    i += 1
            except Exception as e:
                print(e)
    run = True
    i = 0
    data = ''
    sock.settimeout(0.0000001)
    delay = time.time()
    while run:
        #start_time=time.time()
        try:
            sock.send('1/'.encode())
        except BrokenPipeError:
            if i == 0:
                print('----------------------------')
                print('Your opponent leave the game')
                print('----------------------------')
                run = False
                i += 1
        except Exception as e:
            print(e)
        try:
            data = sock.recv(512).decode()
        except ConnectionResetError:
            if i == 0:
                print('----------------------------')
                print('Your opponent leave the game')
                print('----------------------------')
                run = False
                i += 1
        except Exception as e:
            if type(e) != socket.timeout:
                print(e)
        parser(data)
        try:
            delay = time.time()-delay
            if delay < 0.2:
                color = (0, 255, 0)
            elif delay > 0.2:
                color = (255, 255, 0)
                if delay > 1:
                    color = (255, 0, 0)
            win.blit(interface.myfont.render("delay", False, color), (win_height//20*18, win_height+win_height//5//2+25))
        except:
            pass
        pygame.display.update()
        if num == '0':
            sendata = 'red/'
        if num == '1':
            sendata = 'blue/'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if num == '1':
                    if event.key == pygame.K_w or event.key == 172:
                        sendata += 's/'
                    if event.key == pygame.K_s or event.key == 161:
                        sendata += 'w/'
                    if event.key == pygame.K_a or event.key == 160:
                        sendata += 'd/'
                    if event.key == pygame.K_d or event.key == 162:
                        sendata += 'a/'
                    if event.key == pygame.K_LEFT:
                        sendata += 'right/'
                    if event.key == pygame.K_RIGHT:
                        sendata += 'left/'
                    if event.key == pygame.K_UP:
                        sendata += 'down/'
                    if event.key == pygame.K_DOWN:
                        sendata += 'up/'
                elif num == '0':
                    if event.key == pygame.K_w or event.key == 172:
                        sendata += 'w/'
                    if event.key == pygame.K_s or event.key == 161:
                        sendata += 's/'
                    if event.key == pygame.K_a or event.key == 160:
                        sendata += 'a/'
                    if event.key == pygame.K_d or event.key == 162:
                        sendata += 'd/'
                    if event.key == pygame.K_LEFT:
                        sendata += 'left/'
                    if event.key == pygame.K_RIGHT:
                        sendata += 'right/'
                    if event.key == pygame.K_UP:
                        sendata += 'up/'
                    if event.key == pygame.K_DOWN:
                        sendata += 'down/'
                if event.key == pygame.K_SPACE:
                    sendata += 'space/'
                if event.key == pygame.K_r or event.key == 174:
                    sendata += 'r/'
                if event.key == pygame.K_ESCAPE:
                    run = False
        try:
            sock.send((sendata).encode())
            delay = time.time()
        except BrokenPipeError:
            if i == 0:
                print('----------------------------')
                print('Your opponent leave the game')
                print('----------------------------')
                run = False
                i += 1
        except Exception as e:
            print(e)
    sock.close()
if __name__ == '__main__':
    init()
