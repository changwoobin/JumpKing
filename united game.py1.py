import pygame
import sys
from pygame.locals import QUIT, Rect

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

        pygame.display.update()

    fpsclock.tick(3)


main()

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

        pygame.display.update()

    fpsclock.tick(3)


main()  # 5번맵
if y_pos < 846 and y_pos > 54 and x_pos > 800 and before_x < 800:
    to_x *= -1
elif y_pos < 846 and y_pos > 54 and x_pos < 908 and before_x > 908:
    to_x *= -1

if y_pos < 846 and before_y > 846 and x_pos > 908 and x_pos < 908:
    to_y *= -1
elif y_pos > 54 and before_y < 54 and x_pos > 846 and x_pos < 908:
    y_pos = 44
    to_x = 0
if y_pos < 328 and y_pos > 68 and x_pos > 292 and before_x < 292:
    to_x *= -1
elif y_pos < 328 and y_pos > 68 and x_pos < 361 and before_x > 361:
    to_x *= -1

if y_pos < 328 and before_y > 328 and x_pos > 361 and x_pos < 361:
    to_y *= -1
elif y_pos > 68 and before_y < 68 and x_pos > 328 and x_pos < 361:
    y_pos = 58
    to_x = 0
if y_pos < 636 and y_pos > 180 and x_pos > 600 and before_x < 600:
    to_x *= -1
elif y_pos < 636 and y_pos > 180 and x_pos < 636 and before_x > 636:
    to_x *= -1

if y_pos < 600 and before_y > 636 and x_pos > 600 and x_pos < 750:
    to_y *= -1
elif y_pos > 180 and before_y < 180 and x_pos > 600 and x_pos < 750:
    y_pos = 101
    to_x = 0
if y_pos < 216 and y_pos > 234 and x_pos > 180 and before_x < 180:
    to_x *= -1
elif y_pos < 216 and y_pos > 234 and x_pos < 216 and before_x > 216:
    to_x *= -1

if y_pos < 180 and before_y > 216 and x_pos > 180 and x_pos < 180:
    to_y *= -1
elif y_pos > 216 and before_y < 234 and x_pos > 180 and x_pos < 216:
    y_pos = 224
    to_x = 0
if y_pos < 506 and y_pos > 326 and x_pos > 472 and before_x < 472:
    to_x *= -1
elif y_pos < 506 and y_pos > 326 and x_pos < 506 and before_x > 506:
    to_x *= -1

if y_pos < 472 and before_y > 506 and x_pos > 472 and x_pos < 640:
    to_y *= -1
elif y_pos > 326 and before_y < 326 and x_pos > 472 and x_pos < 472:
    y_pos = 316
    to_x = 0
if y_pos < 293 and y_pos > 420 and x_pos > 257 and before_x < 257:
    to_x *= -1
elif y_pos < 293 and y_pos > 420 and x_pos < 293 and before_x > 293:
    to_x *= -1

if y_pos < 420 and before_y > 293 and x_pos > 257 and x_pos < 326:
    to_y *= -1
elif y_pos > 420 and before_y < 420 and x_pos > 257 and x_pos < 326:
    y_pos = 410
    to_x = 0
if y_pos < 62 and y_pos > 500 and x_pos > 26 and before_x < 26:
    to_x *= -1
elif y_pos < 26 and y_pos > 62 and x_pos < 26 and before_x > 121:
    to_x *= -1

if y_pos < 26 and before_y > 62 and x_pos > 26 and x_pos < 121:
    to_y *= -1
elif y_pos > 500 and before_y < 500 and x_pos > 26 and x_pos < 121:
    y_pos = 490
    to_x = 0

    # 4번맵
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
elif y_pos < 718 and y_pos > 600 and x_pos < 71 and before_x > 718:
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

if y_pos < 780 and before_y > 816 and x_pos > 780 and x_pos < 930:
    to_y *= -1
elif y_pos > 200 and before_y < 200 and x_pos > 780 and x_pos < 930:
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
elif y_pos < 472 and y_pos > 326 and x_pos < 472 and before_x > 472:
    to_x *= -1

if y_pos < 472 and before_y > 580 and x_pos > 472 and x_pos < 640:
    to_y *= -1
elif y_pos > 326 and before_y < 326 and x_pos > 472 and x_pos < 640:
    y_pos = 316
    to_x = 0
if y_pos < 465 and y_pos > 280 and x_pos > 465 and before_x < 465:
    to_x *= -1
elif y_pos < 465 and y_pos > 280 and x_pos < 257 and before_x > 257:
    to_x *= -1

if y_pos < 257 and before_y > 465 and x_pos > 257 and x_pos < 326:
    to_y *= -1
elif y_pos > 326 and before_y < 326 and x_pos > 257 and x_pos < 326:
    y_pos = 316
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
