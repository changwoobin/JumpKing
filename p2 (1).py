
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

        pygame.display.update()

    fpsclock.tick(3)


main()
"""if y_pos <90  and y_pos >54  and x_pos >64  and before_x <64 :
    to_x = -1
elif y_pos <90  and y_pos >54  and x_pos <172  and before_x >172 :
    to_x= -1

if y_pos <  and before_y >90  and x_pos >64  and x_pos <172 :
    to_y = -1
elif y_pos >54  and before_y <54  and x_pos >64  and x_pos <172 :
    y_pos =34
    to_x = 0
if y_pos < 104 and y_pos >90  and x_pos >292  and before_x <292 :
    to_x= -1
elif y_pos <104  and y_pos >90  and x_pos <361  and before_x >361 :
    to_x = -1

if y_pos <104  and before_y >104  and x_pos >472  and x_pos <690 :
    to_y= -1
elif y_pos >68  and before_y <68  and x_pos >472  and x_pos <690 :
    y_pos =58
    to_x = 0
if y_pos <147  and y_pos >111  and x_pos >472  and before_x <472 :
    to_x = -1
elif y_pos <147  and y_pos >111  and x_pos <690  and before_x >690 :
    to_x= -1

if y_pos <147 and before_y >147  and x_pos >427  and x_pos <690 :
    to_y = -1
elif y_pos >111  and before_y <111  and x_pos >427  and x_pos <690 :
    y_pos =101
    to_x = 0
if y_pos <270  and y_pos >234  and x_pos >753  and before_x <753 :
    to_x= -1
elif y_pos <270  and y_pos >254  and x_pos <987  and before_x >987 :
    to_x *= -1
if y_pos <270  and before_y >270  and x_pos >753  and x_pos <987 :
    to_y = -1
elif y_pos >234  and before_y <234  and x_pos >753  and x_pos <987 :
    y_pos =224
    to_x = 0
if y_pos <362  and y_pos >326  and x_pos >427  and before_x <427 :
    to_x= -1
elif y_pos <362  and y_pos >326  and x_pos <595  and before_x >595 :
    to_x = -1

if y_pos <362  and before_y >362  and x_pos >427  and x_pos <595 :
    to_y= -1
elif y_pos >326  and before_y <326  and x_pos >427  and x_pos <427 :
    y_pos =316
    to_x = 0
if y_pos <417  and y_pos >381  and x_pos >257  and before_x <257 :
    to_x = -1
elif y_pos <417  and y_pos >417  and x_pos <638  and before_x >638 :
    to_x= -1

if y_pos <417  and before_y >417  and x_pos >257  and x_pos <638 :
    to_y = -1
elif y_pos >381  and before_y <381  and x_pos >257  and x_pos <257 :
    y_pos =371
    to_x = 0
if y_pos <459  and y_pos >423  and x_pos >26  and before_x <26 :
    to_x= -1
elif y_pos <459  and y_pos >423  and x_pos <121  and before_x >121 :
    to_x = -1

if y_pos <459  and before_y >459  and x_pos >26  and x_pos <121 :
    to_y= -1
elif y_pos >423  and before_y <423  and x_pos >26  and x_pos <26 :
    y_pos =413
    to_x = 0"""
