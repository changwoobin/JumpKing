import pygame
import time

pygame.init()

scrWidth = 960
scrHeight = 540
screen = pygame.display.set_mode((scrWidth, scrHeight))

pygame.display.set_caption("Jump King")
background = pygame.image.load("./img/background.png")
block_side = pygame.image.load("./img/block.png")  # 300 X 200
block_center = pygame.image.load("./img/block2.png")  # 360 X 10
block_center2 = pygame.image.load("./img/block3.png")  # 360 X 100
block_s = pygame.image.load("./img/block4.png")  # 25 x 25
block_end = pygame.image.load("./img/block5.png")
end = pygame.image.load("./img/end.png")
surface = pygame.display.set_mode((960, 540))
fpsclook = pygame.time.Clock
black = (0, 0, 0)

# 캐릭터
character = pygame.image.load("./img/end.png")  # 10X10
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

# 테스트 용
# x_pos = 300
# y_pos = 5

time_jump = 0
end_time_jump = 0
mappage = 1

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

    if x_pos < 0:
        to_x *= -1

    if x_pos > scrWidth - 10:
        to_x *= -1

    if mappage == 2:
        if y_pos < 90 and y_pos > 54 and x_pos > 64 and before_x < 64:
            to_x *= -1
        elif y_pos < 90 and y_pos > 54 and x_pos < 172 and before_x > 172:
            to_x *= -1

        if y_pos < 90 and before_y > 90 and x_pos > 64 and x_pos < 172:  # 여기 확인 요함
            to_y *= -1
        elif y_pos > 54 and before_y < 54 and x_pos > 64 and x_pos < 172:
            y_pos = 44
            to_x = 0
    ######
        if y_pos < 104 and y_pos > 68 and x_pos > 292 and before_x < 292:
            to_x = -1
        elif y_pos < 104 and y_pos > 68 and x_pos < 361 and before_x > 361:
            to_x *= -1

        if y_pos < 104 and before_y > 104 and x_pos > 292 and x_pos < 361:
            to_y *= -1
        elif y_pos > 68 and before_y < 68 and x_pos > 292 and x_pos < 361:
            y_pos = 58
            to_x = 0

        if y_pos < 147 and y_pos > 111 and x_pos > 472 and before_x < 472:
            to_x *= -1
        elif y_pos < 147 and y_pos > 111 and x_pos < 690 and before_x > 690:
            to_x *= -1

        if y_pos < 147 and before_y > 147 and x_pos > 472 and x_pos < 690:
            to_y *= -1
        elif y_pos > 111 and before_y < 111 and x_pos > 472 and x_pos < 690:
            y_pos = 101
            to_x = 0

     ##########
        if y_pos < 270 and y_pos > 234 and x_pos > 753 and before_x < 753:
            to_x *= -1
        elif y_pos < 270 and y_pos > 254 and x_pos < 921 and before_x > 921:
            to_x *= -1

        if y_pos < 270 and before_y > 270 and x_pos > 753 and x_pos < 921:
            to_y *= -1
        elif y_pos > 234 and before_y < 234 and x_pos > 753 and x_pos < 921:
            y_pos = 224
            to_x = 0
    ##########
        if y_pos < 362 and y_pos > 326 and x_pos > 472 and before_x < 472:
            to_x *= -1
        elif y_pos < 362 and y_pos > 326 and x_pos < 640 and before_x > 640:
            to_x *= -1

        if y_pos < 362 and before_y > 362 and x_pos > 472 and x_pos < 640:
            to_y *= -1
        elif y_pos > 326 and before_y < 326 and x_pos > 472 and x_pos < 640:
            y_pos = 316
            to_x = 0

    #########
        if y_pos < 417 and y_pos > 381 and x_pos > 257 and before_x < 257:
            to_x *= -1
        elif y_pos < 417 and y_pos > 417 and x_pos < 326 and before_x > 326:
            to_x *= -1

        if y_pos < 417 and before_y > 417 and x_pos > 257 and x_pos < 326:
            to_y *= -1
        elif y_pos > 381 and before_y < 381 and x_pos > 257 and x_pos < 326:
            y_pos = 371
            to_x = 0

    ############
        if y_pos < 459 and y_pos > 423 and x_pos > 26 and before_x < 26:
            to_x *= -1
        elif y_pos < 459 and y_pos > 423 and x_pos < 121 and before_x > 121:
            to_x *= -1

        if y_pos < 459 and before_y > 459 and x_pos > 26 and x_pos < 121:
            to_y *= -1
        elif y_pos > 423 and before_y < 423 and x_pos > 26 and x_pos < 121:
            y_pos = 413
            to_x = 0
        surface.fill((255, 255, 255))  # R,G,B

        # draw Rectangle
        rect1 = (64, 54, 108, 36)
        rect2 = (292, 68, 69, 36)
        rect3 = (472, 111, 218, 36)
        rect4 = (753, 234, 168, 36)
        rect5 = (472, 326, 168, 36)
        rect6 = (257, 381, 69, 36)
        rect7 = (26, 423, 95, 36)

        pygame.draw.rect(surface, black, rect1)
        pygame.draw.rect(surface, black, rect2)
        pygame.draw.rect(surface, black, rect3)
        pygame.draw.rect(surface, black, rect4)
        pygame.draw.rect(surface, black, rect5)
        pygame.draw.rect(surface, black, rect6)
        pygame.draw.rect(surface, black, rect7)
        screen.blit(character, (x_pos, y_pos))

        if y_pos > 540:
            mappage = 1
            y_pos = 0

        if y_pos < -10:
            mappage = 3
            y_pos = 540

    elif mappage == 5:
        if y_pos < 836 and y_pos > 54 and x_pos > 800 and before_x < 800:
            to_x *= -1
        elif y_pos < 836 and y_pos > 54 and x_pos < 908 and before_x > 908:
            to_x *= -1

        if y_pos < 800 and before_y > 836 and x_pos > 800 and x_pos < 908:
            to_y *= -1
        elif y_pos > 54 and before_y < 54 and x_pos > 836 and x_pos < 908:
            y_pos = 44
            to_x = 0
        if y_pos < 328 and y_pos > 68 and x_pos > 292 and before_x < 292:
            to_x *= -1
        elif y_pos < 328 and y_pos > 68 and x_pos < 361 and before_x > 361:
            to_x *= -1

        if y_pos < 292 and before_y > 328 and x_pos > 292 and x_pos < 361:
            to_y *= -1
        elif y_pos > 68 and before_y < 68 and x_pos > 292 and x_pos < 361:
            y_pos = 58
            to_x = 0
        if y_pos < 636 and y_pos > 180 and x_pos > 600 and before_x < 600:
            to_x *= -1
        elif y_pos < 636 and y_pos > 180 and x_pos < 750 and before_x > 750:
            to_x *= -1

        if y_pos < 600 and before_y > 636 and x_pos > 600 and x_pos < 750:
            to_y *= -1
        elif y_pos > 180 and before_y < 180 and x_pos > 600 and x_pos < 750:
            y_pos = 170
            to_x = 0
        if y_pos < 216 and y_pos > 234 and x_pos > 180 and before_x < 180:
            to_x *= -1
        elif y_pos < 216 and y_pos > 234 and x_pos < 348 and before_x > 348:
            to_x *= -1

        if y_pos < 180 and before_y > 216 and x_pos > 180 and x_pos < 348:
            to_y *= -1
        elif y_pos > 234 and before_y < 234 and x_pos > 180 and x_pos < 348:
            y_pos = 224
            to_x = 0
        if y_pos < 508 and y_pos > 326 and x_pos > 472 and before_x < 472:
            to_x *= -1
        elif y_pos < 508 and y_pos > 326 and x_pos < 508 and before_x > 508:
            to_x *= -1

        if y_pos < 472 and before_y > 508 and x_pos > 472 and x_pos < 640:
            to_y *= -1
        elif y_pos > 326 and before_y < 326 and x_pos > 472 and x_pos < 640:
            y_pos = 316
            to_x = 0
        if y_pos < 293 and y_pos > 420 and x_pos > 257 and before_x < 257:
            to_x *= -1
        elif y_pos < 257 and y_pos > 420 and x_pos < 293 and before_x > 293:
            to_x *= -1

        if y_pos < 257 and before_y > 293 and x_pos > 257 and x_pos < 326:
            to_y *= -1
        elif y_pos > 420 and before_y < 420 and x_pos > 257 and x_pos < 326:
            y_pos = 410
            to_x = 0
        if y_pos < 62 and y_pos > 500 and x_pos > 26 and before_x < 26:
            to_x *= -1
        elif y_pos < 62 and y_pos > 500 and x_pos < 62 and before_x > 62:
            to_x *= -1

        if y_pos < 26 and before_y > 62 and x_pos > 26 and x_pos < 121:
            to_y *= -1
        elif y_pos > 500 and before_y < 500 and x_pos > 26 and x_pos < 121:
            y_pos = 490
            to_x = 0

        surface.fill((255, 255, 255))  # R,G,B

        # draw Rectangle
        rect1 = (800, 54, 108, 36)
        rect2 = (292, 68, 69, 36)
        rect3 = (600, 180, 150, 36)
        rect4 = (180, 234, 168, 36)
        rect5 = (472, 326, 168, 36)
        rect6 = (257, 420, 69, 36)
        rect7 = (26, 500, 95, 36)

        pygame.draw.rect(surface, black, rect1)
        pygame.draw.rect(surface, black, rect2)
        pygame.draw.rect(surface, black, rect3)
        pygame.draw.rect(surface, black, rect4)
        pygame.draw.rect(surface, black, rect5)
        pygame.draw.rect(surface, black, rect6)
        pygame.draw.rect(surface, black, rect7)
        screen.blit(character, (x_pos, y_pos))

        if y_pos > 540:
            mappage = 4
            y_pos = 0

        if y_pos < -10:
            mappage = 6
            y_pos = 540
    elif mappage == 4:

        if y_pos < 164 and y_pos > 150 and x_pos > 128 and before_x < 128:
            to_x *= -1
        elif y_pos < 164 and y_pos > 150 and x_pos < 164 and before_x > 164:
            to_x *= -1

        if y_pos < 128 and before_y > 164 and x_pos > 128 and x_pos < 628:
            to_y *= -1
        elif y_pos > 150 and before_y < 150 and x_pos > 128 and x_pos < 628:
            y_pos = 140
            to_x = 0
        if y_pos < 718 and y_pos > 68 and x_pos > 600 and before_x < 600:
            to_x *= -1
        elif y_pos < 718 and y_pos > 68 and x_pos < 718 and before_x > 718:
            to_x *= -1

        if y_pos < 600 and before_y > 718 and x_pos > 600 and x_pos < 669:
            to_y *= -1
        elif y_pos > 68 and before_y < 68 and x_pos > 600 and x_pos < 669:
            y_pos = 58
            to_x = 0
        if y_pos < 816 and y_pos > 200 and x_pos > 780 and before_x < 780:
            to_x *= -1
        elif y_pos < 816 and y_pos > 200 and x_pos < 816 and before_x > 816:
            to_x *= -1

        if y_pos < 780 and before_y > 816 and x_pos > 780 and x_pos < 916:
            to_y *= -1
        elif y_pos > 200 and before_y < 200 and x_pos > 780 and x_pos < 916:
            y_pos = 190
            to_x = 0
        if y_pos < 216 and y_pos > 350 and x_pos > 180 and before_x < 180:
            to_x *= -1
        elif y_pos < 216 and y_pos > 350 and x_pos < 216 and before_x > 216:
            to_x *= -1

        if y_pos < 180 and before_y > 216 and x_pos > 180 and x_pos < 264:
            to_y *= -1
        elif y_pos > 350 and before_y < 350 and x_pos > 180 and x_pos < 264:
            y_pos = 340
            to_x = 0
        if y_pos < 580 and y_pos > 326 and x_pos > 472 and before_x < 472:
            to_x *= -1
        elif y_pos < 472 and y_pos > 326 and x_pos < 580 and before_x > 580:
            to_x *= -1

        if y_pos < 472 and before_y > 580 and x_pos > 472 and x_pos < 640:
            to_y *= -1
        elif y_pos > 326 and before_y < 326 and x_pos > 472 and x_pos < 640:
            y_pos = 316
            to_x = 0
        if y_pos < 465 and y_pos > 280 and x_pos > 257 and before_x < 257:
            to_x *= -1
        elif y_pos < 465 and y_pos > 280 and x_pos < 465 and before_x > 465:
            to_x *= -1

        if y_pos < 257 and before_y > 465 and x_pos > 257 and x_pos < 326:
            to_y *= -1
        elif y_pos > 280 and before_y < 280 and x_pos > 257 and x_pos < 326:
            y_pos = 270
            to_x = 0

        if y_pos < 66 and y_pos > 450 and x_pos > 30 and before_x < 30:
            to_x *= -1
        elif y_pos < 66 and y_pos > 450 and x_pos < 66 and before_x > 66:
            to_x *= -1

        if y_pos < 30 and before_y > 66 and x_pos > 30 and x_pos < 75:
            to_y *= -1
        elif y_pos > 450 and before_y < 450 and x_pos > 30 and x_pos < 75:
            y_pos = 440
            to_x = 0  # 5번맵
        surface.fill((255, 255, 255))  # R,G,B

        # draw Rectangle
        rect1 = (128, 150, 500, 36)
        rect2 = (600, 68, 69, 118)
        rect3 = (780, 200, 150, 36)
        rect4 = (180, 350, 84, 36)
        rect5 = (472, 326, 168, 108)
        rect6 = (257, 280, 69, 208)
        rect7 = (30, 450, 45, 36)

        pygame.draw.rect(surface, black, rect1)
        pygame.draw.rect(surface, black, rect2)
        pygame.draw.rect(surface, black, rect3)
        pygame.draw.rect(surface, black, rect4)
        pygame.draw.rect(surface, black, rect5)
        pygame.draw.rect(surface, black, rect6)
        pygame.draw.rect(surface, black, rect7)
        screen.blit(character, (x_pos, y_pos))

        if y_pos > 540:
            mappage = 3
            y_pos = 0

        if y_pos < -10:
            mappage = 5
            y_pos = 540

    elif mappage == 3:
        if y_pos < 92 and y_pos > 56 and x_pos > 199 and before_x < 199:
            to_x *= -1
        elif y_pos < 92 and y_pos > 56 and x_pos < 329 and before_x > 329:
            to_x *= -1

        if y_pos < 92 and before_y > 92 and x_pos > 199 and x_pos < 329:
            to_y *= -1
        elif y_pos > 56 and before_y < 56 and x_pos > 199 and x_pos < 329:
            y_pos = 46
            to_x = 0
        if y_pos < 146 and y_pos > 110 and x_pos > 464 and before_x < 464:
            to_x *= -1
        elif y_pos < 146 and y_pos > 110 and x_pos < 594 and before_x > 594:
            to_x *= -1

        if y_pos < 146 and before_y > 146 and x_pos > 464 and x_pos < 594:
            to_y *= -1
        elif y_pos > 110 and before_y < 110 and x_pos > 464 and x_pos < 594:
            y_pos = 100
            to_x *= 0
        if y_pos < 237 and y_pos > 201 and x_pos > 690 and before_x < 690:
            to_x *= -1
        elif y_pos < 237 and y_pos > 201 and x_pos < 812 and before_x > 812:
            to_x = -1

        if y_pos < 237 and before_y > 237 and x_pos > 690 and x_pos < 812:
            to_y *= -1
        elif y_pos > 201 and before_y < 201 and x_pos > 690 and x_pos < 812:
            y_pos = 191
            to_x = 0
        if y_pos < 325 and y_pos > 289 and x_pos > 480 and before_x < 480:
            to_x *= -1
        elif y_pos < 325 and y_pos > 325 and x_pos < 610 and before_x > 610:
            to_x *= -1
        if y_pos < 325 and before_y > 325 and x_pos > 480 and x_pos < 610:
            to_y *= -1
        elif y_pos > 289 and before_y < 289 and x_pos > 480 and x_pos < 610:
            y_pos = 279
            to_x = 0
        if y_pos < 432 and y_pos > 396 and x_pos > 287 and before_x < 287:
            to_x *= -1
        elif y_pos < 432 and y_pos > 396 and x_pos < 408 and before_x > 408:
            to_x *= -1

        if y_pos < 432 and before_y > 432 and x_pos > 287 and x_pos < 408:
            to_y *= -1
        elif y_pos > 396 and before_y < 396 and x_pos > 287 and x_pos < 408:
            y_pos = 386
            to_x = 0
        if y_pos < 498 and y_pos > 462 and x_pos > 62 and before_x < 62:
            to_x *= -1
        elif y_pos < 498 and y_pos > 462 and x_pos < 213 and before_x > 213:
            to_x *= -1

        if y_pos < 498 and before_y > 498 and x_pos > 62 and x_pos < 213:
            to_y *= -1
        elif y_pos > 462 and before_y < 462 and x_pos > 62 and x_pos < 213:
            y_pos = 452
            to_x = 0

        surface.fill((255, 255, 255))  # R,G,B

        # draw Rectangle
        rect1 = (199, 56, 130, 36)
        rect2 = (464, 110, 130, 36)
        rect3 = (464, 110, 130, 36)
        rect4 = (690, 201, 122, 36)
        rect5 = (480, 289, 130, 36)
        rect6 = (287, 396, 121, 36)
        rect7 = (62, 462, 151, 36)

        pygame.draw.rect(surface, black, rect1)
        pygame.draw.rect(surface, black, rect2)
        pygame.draw.rect(surface, black, rect3)
        pygame.draw.rect(surface, black, rect4)
        pygame.draw.rect(surface, black, rect5)
        pygame.draw.rect(surface, black, rect6)
        pygame.draw.rect(surface, black, rect7)
        screen.blit(character, (x_pos, y_pos))
        if y_pos > 540:
            mappage = 2
            y_pos = 0

        if y_pos < -10:
            mappage = 4
            y_pos = 540

    elif mappage == 6:
        if y_pos < 425 and y_pos > 400 and x_pos > 90 and before_x < 90:
            to_x *= -1
        elif y_pos < 425 and y_pos > 400 and x_pos < 125 and before_x > 125:
            to_x *= -1

        if y_pos < 425 and before_y > 425 and x_pos > 90 and x_pos < 125:
            to_y *= -1
        elif y_pos > 400 and before_y < 400 and x_pos > 90 and x_pos < 125:
            y_pos = 390
            to_x = 0

        if y_pos < 237 and y_pos > 212 and x_pos > 190 and before_x < 190:
            to_x *= -1
        elif y_pos < 237 and y_pos > 212 and x_pos < 225 and before_x > 225:
            to_x *= -1

        if y_pos < 237 and before_y > 237 and x_pos > 190 and x_pos < 225:
            to_y *= -1
        elif y_pos > 212 and before_y < 212 and x_pos > 190 and x_pos < 225:
            y_pos = 202
            to_x = 0

        if y_pos < 375 and y_pos > 350 and x_pos > 490 and before_x < 490:
            to_x *= -1
        elif y_pos < 375 and y_pos > 350 and x_pos < 525 and before_x > 525:
            to_x *= -1

        if y_pos < 375 and before_y > 375 and x_pos > 490 and x_pos < 525:
            to_y *= -1
        elif y_pos > 350 and before_y < 350 and x_pos > 490 and x_pos < 525:
            y_pos = 340
            to_x = 0

        if y_pos < 225 and y_pos > 200 and x_pos > 840 and before_x < 840:
            to_x *= -1
        elif y_pos < 225 and y_pos > 200 and x_pos < 875 and before_x > 875:
            to_x *= -1

        if y_pos < 225 and before_y > 225 and x_pos > 840 and x_pos < 875:
            to_y *= -1
        elif y_pos > 200 and before_y < 200 and x_pos > 840 and x_pos < 875:
            y_pos = 190
            to_x = 0

        if y_pos < 75 and y_pos > 50 and x_pos > 815 and before_x < 815:
            to_x *= -1
        elif y_pos < 75 and y_pos > 50 and x_pos < 875 and before_x > 875:
            to_x *= -1

        if y_pos < 75 and before_y > 75 and x_pos > 815 and x_pos < 875:
            to_y *= -1
        elif y_pos > 50 and before_y < 50 and x_pos > 815 and x_pos < 875:
            y_pos = 40
            to_x = 0

        screen.blit(background, (0, 0))
        screen.blit(block_s, (200, 212))  # 완료 2
        screen.blit(block_s, (100, 400))  # 완료 1
        screen.blit(block_s, (500, 350))  # 완료 3
        screen.blit(block_s, (850, 200))  # 완료 4
        screen.blit(block_end, (825, 50))  # 완료 5
        screen.blit(end, (840, 35))
        screen.blit(character, (x_pos, y_pos))
        if y_pos > 540:
            mappage = 5
            y_pos = 0

    elif mappage == 1:
        if y_pos > 520:
            y_pos = 520
            to_x = 0

        if y_pos >= 330 and before_y <= 330 and x_pos > 0 and x_pos < 300:
            y_pos = 330
            to_x = 0

        if y_pos <= 520 and y_pos > 330 and x_pos < 300 and before_x > 300:
            to_x *= -1

        if y_pos >= 330 and before_y <= 330 and x_pos > 650 and x_pos < 960:
            y_pos = 330
            to_x = 0

        if y_pos <= 520 and y_pos > 330 and x_pos > 650 and before_x < 650:
            to_x *= -1

        if y_pos < 200 and before_y > 200 and x_pos > 300 and x_pos < 650:
            to_y *= -1
        elif y_pos > 100 and before_y < 100 and x_pos > 300 and x_pos < 650:
            y_pos = 90
            to_x = 0

        if y_pos < 200 and y_pos > 100 and x_pos > 300 and before_x < 300:
            to_x *= -1
        elif y_pos < 200 and y_pos > 100 and x_pos < 660 and before_x > 660:
            to_x *= -1

        if y_pos < -10:
            mappage = 2
            y_pos = 540

        screen.blit(background, (0, 0))
        screen.blit(block_side, (0, 340))
        screen.blit(block_side, (660, 340))
        screen.blit(block_center, (300, 530))
        screen.blit(block_center2, (300, 100))
        screen.blit(character, (x_pos, y_pos))

    print(mappage)
    pygame.display.update()
    before_x = x_pos
    before_y = y_pos
    time.sleep(0.01)


pygame.quit()
