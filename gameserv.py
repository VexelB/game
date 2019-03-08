import pygame
import socket
import engine

def init(local = False, ip = 'localhost', sock = None):

    def pasrer():
        data1 = sock.recv(512).decode()
        dataset = data1.split('/')
        for data in dataset:
            if 'map' in data:
                q = 3
                for i in range(len(map)):
                    for j in range(len(map[0])):
                        map[i][j] = int(data[q])
                        q += 1
            elif 'orient' in data:
                if 'red' in data:
                    data1 = data.split(',')
                    pygame.draw.rect(win, (250, 0, 0), (int(data1[0]), int(data1[1]), win_height//100, win_height//100))
                elif 'blue' in data:
                    data1 = data.split(',')
                    pygame.draw.rect(win, (0, 0, 250), (int(data1[0]), int(data1[1]), win_height//100, win_height//100))
            elif 'bullet' in data:
                data1 = data.split(',')
                pygame.draw.circle(win, (250, 250, 0), (data1[0], data1[1]), win_width//100)

    def draw():
        for i in range(len(map)):
            for j in range(len(map)):
                x = win_height / len(engine.map) * i
                y = win_width / len(engine.map[0]) * j
                if j == 1:
                    pygame.draw.rect(win, (250, 0, 0), (x+5, y+5, win_height//10, win_height//10))
                if j == 2:
                    pygame.draw.rect(win, (0, 0, 250), (x+5, y+5, win_height//10, win_height//10))
                if j == 3:
                    pygame.draw.rect(win, (250, 250, 250), (x+5, y+5, win_height/10, win_height/10))

    bullets = []
    map = [[0 for i in range(9)] for j in range(9)]
    pygame.init()
    win_height = win_width = 500
    win = pygame.display.set_mode((win_width,win_height+win_height//5),0)
    pygame.display.set_caption("Танчики")
    interface = engine.Interface()
    bullets = []
    win.fill((0, 0, 0))
    while True:
        sock.send('1/'.encode())
        parser()
        draw()
        sendata = 'red/'
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
        sock.send((sendata).encode())
