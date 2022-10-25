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
        surface.fill((255, 255, 255)) #R,G,B

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

        pygame.display.update()

    fpsclock.tick(3)

main()

"""if y_pos <92  and y_pos >56  and x_pos >199  and before_x <199 :
    to_x = -1
elif y_pos <92  and y_pos >56  and x_pos <329  and before_x >329 :
    to_x= -1

if y_pos <92  and before_y >92  and x_pos >199  and x_pos <329 :
    to_y = -1
elif y_pos >56  and before_y <56  and x_pos >199  and x_pos <329 :
    y_pos =46
    to_x = 0
if y_pos <146  and y_pos >110  and x_pos >464  and before_x <464 :
    to_x= -1
elif y_pos <146  and y_pos >110  and x_pos <594  and before_x >594 :
    to_x = -1

if y_pos <146  and before_y >146  and x_pos >464  and x_pos <594 :
    to_y= -1
elif y_pos >110  and before_y <110  and x_pos >464  and x_pos <594 :
    y_pos =100
    to_x = 0
if y_pos <237  and y_pos >201  and x_pos >690  and before_x <690 :
    to_x = -1
elif y_pos <237  and y_pos >201  and x_pos <812  and before_x >812 :
    to_x= -1

if y_pos <237  and before_y >237  and x_pos >690  and x_pos <812 :
    to_y = -1
elif y_pos >201  and before_y <201  and x_pos >690  and x_pos <812 :
    y_pos =191
    to_x = 0
if y_pos <325  and y_pos >289  and x_pos >480  and before_x <480 :
    to_x= -1
elif y_pos <325  and y_pos >325  and x_pos <610  and before_x >610 :
    to_x *= -1
if y_pos <325  and before_y >325  and x_pos >480  and x_pos <610 :
    to_y = -1
elif y_pos >289  and before_y <289  and x_pos >480  and x_pos <610 :
    y_pos =279
    to_x = 0
if y_pos <432  and y_pos >396  and x_pos >287  and before_x <287 :
    to_x= -1
elif y_pos <432  and y_pos >396  and x_pos <408  and before_x >408 :
    to_x = -1

if y_pos <432  and before_y >432  and x_pos >287  and x_pos <408 :
    to_y= -1
elif y_pos >396  and before_y <386  and x_pos >287  and x_pos <408 :
    y_pos =386
    to_x = 0
if y_pos <498  and y_pos >462  and x_pos >62  and before_x <62 :
    to_x = -1
elif y_pos <498  and y_pos >462  and x_pos <213  and before_x >213 :
    to_x= -1

if y_pos <498  and before_y >498  and x_pos >62  and x_pos <213 :
    to_y *= -1
elif y_pos >462  and before_y <462  and x_pos >62  and x_pos <213 :
    y_pos =452
    to_x = 0"""