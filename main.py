import pygame
import gameserv
import gameclient

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
create = myfont.render('1: Создат игру', False, (250, 250, 250))
join = myfont.render('2: Присоединица', False, (250, 250, 250))
win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("StepGame")
init = False
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                gameserv.init()
            if event.key == pygame.K_2:
                gameclient.init()
    win.fill((0,0,0))
    win.blit(create,(10,120))
    win.blit(join,(10,150))
    pygame.display.update()
pygame.quit()
