import pygame
import time


# 4번맵

pygame.init()
surface = pygame.display.set_mode((960, 540))
fpsclook = pygame.time.Clock
black = (0, 0, 0)


def main():
    """"main routine"""
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        surface.fill((255, 255, 255))  # R,G,B

        # draw Rectangle
        rect1 = (128, 150, 450, 36)
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

        pygame.display.update()

    fpsclock.tick(3)


main()
if y_pos < 54 and y_pos > 90 and x_pos < 800 and before_x > 800:
    to_x *= -1
elif y_pos < 54 and y_pos > 90 and x_pos > 908 and before_x < 908:
    to_x *= -1

if y_pos > 54 and before_y < 54 and x_pos > 800 and x_pos < 908:
    to_y *= -1
elif y_pos < 90 and before_y > 90 and x_pos > 908 and x_pos < 800:
    y_pos = 44
    to_x = 0
if y_pos < 104 and y_pos > 68 and x_pos > 292 and before_x < 292:
    to_x *= -1
elif y_pos < 104 and y_pos > 68 and x_pos < 361 and before_x > 361:
    to_x *= -1

if y_pos < 68 and before_y > 68 and x_pos > 292 and x_pos < 361:
    to_y *= -1
elif y_pos > 104 and before_y < 104 and x_pos > 292 and x_pos < 361:
    y_pos = 58
    to_x = 0
if y_pos < 216 and y_pos > 180 and x_pos > 600 and before_x < 600:
    to_x *= -1
elif y_pos < 216 and y_pos > 180 and x_pos < 636 and before_x > 636:
    to_x *= -1

if y_pos < 180 and before_y > 180 and x_pos > 600 and x_pos < 750:
    to_y *= -1
elif y_pos > 216 and before_y < 216 and x_pos > 600 and x_pos < 750:
    y_pos = 206
    to_x = 0
if y_pos < 280 and y_pos > 234 and x_pos > 180 and before_x <180 :
    to_x *= -1
elif y_pos < 280 and y_pos > 234 and x_pos < 248 and before_x >248 :
    to_x *= -1

if y_pos < 234 and before_y > 234 and x_pos > 180 and x_pos <248 :
    to_y *= -1
elif y_pos > 280 and before_y < 280 and x_pos > 180 and x_pos <248 :
    y_pos = 224
    to_x = 0
if y_pos < 362 and y_pos > 326 and x_pos > 472 and before_x < 472:
    to_x *= -1
elif y_pos < 362 and y_pos > 326 and x_pos < 640 and before_x > 640:
    to_x *= -1

if y_pos < 326 and before_y > 326 and x_pos > 640 and x_pos < 640:
    to_y *= -1
elif y_pos > 362 and before_y < 362 and x_pos > 472 and x_pos < 472:
    y_pos = 316
    to_x = 0
if y_pos < 456 and y_pos > 420 and x_pos > 257 and before_x < 257:
    to_x *= -1
elif y_pos < 456 and y_pos > 420 and x_pos < 326 and before_x > 326:
    to_x *= -1

if y_pos < 420 and before_y > 420 and x_pos > 257 and x_pos < 326:
    to_y *= -1
elif y_pos > 456 and before_y < 456 and x_pos > 257 and x_pos < 326:
    y_pos = 410
    to_x = 0
if y_pos < 536 and y_pos > 500 and x_pos > 26 and before_x < 26:
    to_x *= -1
elif y_pos < 536 and y_pos > 500 and x_pos < 121 and before_x > 121:
    to_x *= -1

if y_pos < 500 and before_y > 500 and x_pos > 26 and x_pos < 121:
    to_y *= -1
elif y_pos > 536 and before_y < 536 and x_pos > 26 and x_pos < 121:
    y_pos = 490
    to_x = 0

    # 4번맵