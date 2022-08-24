import pygame

pygame.init()

scrWidth = 960
scrHeight = 540
screen = pygame.display.set_mode((scrWidth, scrHeight))

pygame.display.set_caption("Jump King")
background = pygame.image.load("./img/background.png")
block_side = pygame.image.load("./img/block.png")
block_center = pygame.image.load("./img/block2.png")
block_center2 = pygame.image.load("./img/block3.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    screen.blit(block_side, (0,340))
    screen.blit(block_side, (660, 340))
    screen.blit(block_center, (300, 530))
    screen.blit(block_center2, (300, 100))

    pygame.display.update()


pygame.quit()