import time
import pygame
import random
def car(x,y,screen):
        image=pygame.image.load('car_racer\Images\car.png')
        vechiel=pygame.transform.scale(image,(120,240))
        screen.blit(vechiel,(x,y))
def crash(text,screen,game_file):
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 80)
        text = font.render(text, True, white,green)
        textRect = text.get_rect()
        textRect.center = (400 ,300)
        screen.blit(text, textRect)
        pygame.display.update()        
        time.sleep(4)
        game_file()
def things(display_surface,thingx,thingy,thingw,thingh,color):
        pygame.draw.rect(display_surface,color,[thingx,thingy,thingw,thingh])
def cone(x,y,screen):
        image=pygame.image.load('car_racer\Images\Cone.png')
        cone=pygame.transform.scale(image,(120,120))
        screen.blit(cone,(x,y))
def points(screen,score):
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf',25)
        score = font.render(score, True,white)
        scoreRect = score.get_rect()
        scoreRect.topright = (100 ,100)
        screen.blit(score, scoreRect)
        pygame.display.update()








            

            
        

    