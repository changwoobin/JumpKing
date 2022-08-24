from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
import pygame

pygame.init()

scrWidth = 960
scrHeight = 540
screen = pygame.display.set_mode((scrWidth, scrHeight))

pygame.display.set_caption("Jump King")
background = pygame.image.load("./img/background.png")
block_center = pygame.image.load("./img/block2.png")
block_s = pygame.image.load("./img/block4.png")
block_end = pygame.image.load("./img/block5.png")
end = pygame.image.load("./img/end.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(block_s, (200, 212))
    screen.blit(block_s, (100, 400))
    screen.blit(block_s, (500, 350))
    screen.blit(block_s, (850, 200))
    screen.blit(block_end, (825, 50))
    screen.blit(end, (840, 35))

    pygame.display.update()


pygame.quit()