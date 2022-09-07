import pygame
import time

pygame.init()

scrWidth = 960
scrHeight = 540
screen = pygame.display.set_mode((scrWidth, scrHeight))

pygame.display.set_caption("Jump King")
background = pygame.image.load("./img/background.png")
block_side = pygame.image.load("./img/block.png") # 300 X 200
block_center = pygame.image.load("./img/block2.png") # 360 X 10
block_center2 = pygame.image.load("./img/block3.png") # 360 X 100

#캐릭터
character = pygame.image.load("./img/end.png") # 10X10
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
x_pos = scrWidth/2 - 5
y_pos = 540 - character_height - 10

to_x = 0
to_y = 0

a_x = 0
u = 0

before_x = scrWidth/2 - 5
before_y = 540 - character_height - 10


time_jump = 0
end_time_jump = 0


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
                a_x = 0.4
            elif event.key == pygame.K_RIGHT:
                to_x += 1
                a_x = -0.4
            elif event.key == pygame.K_SPACE:
                time_jump = time.time()/1.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                end_time_jump = time.time()/1.1
                u = (end_time_jump - time_jump)*20*(-1)
                if u < -24:
                    u = -24
                
                to_x = u*a_x
                to_y = 0.9*u
                a_x = 0


    x_pos += to_x
    y_pos += to_y

    to_y += 1

    if y_pos > 520:
        y_pos = 520
        to_x = 0

    if x_pos < 0:
        x_pos = 0

    if x_pos > scrWidth - 10:
        x_pos = scrWidth - 10

    if y_pos > 330:
        if x_pos < 300:
            if before_x > 300:
                to_x *= -1
            elif before_x < 300:
                y_pos = 330
                to_x = 0
        elif x_pos > 650:
            if before_x < 650:
                to_x *= -1
            elif before_x > 650:
                y_pos = 330
                to_x = 0

    if y_pos < 200 and before_y > 200 and x_pos > 300 and x_pos < 650:
        to_y *= -1
    elif y_pos > 100 and before_y < 100 and x_pos > 300 and x_pos < 650:
        y_pos = 90
        to_x = 0
    
    if y_pos < 200 and y_pos > 100 and  x_pos > 300 and before_x < 300:
        to_x *= -1
    elif y_pos < 200 and y_pos > 100 and  x_pos < 660 and before_x > 660:
        to_x *= -1


    screen.blit(background, (0, 0))
    screen.blit(block_side, (0,340))
    screen.blit(block_side, (660, 340))
    screen.blit(block_center, (300, 530))
    screen.blit(block_center2, (300, 100))
    screen.blit(character, (x_pos, y_pos))

    pygame.display.update()
    before_x = x_pos
    before_y = y_pos
    time.sleep(0.01)


pygame.quit()