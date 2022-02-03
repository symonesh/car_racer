from socket import gethostbyname_ex
import pygame
from settings import  setting 
import time
import Car
import random
def run_game():
    pygame.init()
    ai_settings=setting()
    gameDisplay=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Racer122')
    clock=pygame.time.Clock()
    x=(ai_settings.screen_width*0.4)
    y=(ai_settings.screen_height*0.5)     
    white = (255, 255, 255)
    thing_x=ai_settings.screen_height
    thing_y=ai_settings.screen_width/2
    x_change=0
    crashed=False
    thing_x=360
    thing_y=0
    thing_w=50
    thing_h=20
    thing_z=0
    cone_x=0
    cone_y=0
    cone_change=0
    score=0
    while not crashed:
            for event in pygame.event.get():            
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        thing_y=15

                    if event.key==pygame.K_DOWN:
                        thing_y=-5
                        
                    if event.key==pygame.K_LEFT:
                        x_change=-15
                    elif event.key==pygame.K_RIGHT:
                        x_change=15
                    elif event.key==pygame.K_SPACE:
                        pygame.time.wait(1000)                                      
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        x_change=0
                        thing_y=0
                    if event.key==pygame.K_DOWN or event.key==pygame.K_UP:
                        while thing_y>0:
                            thing_y-=1
            x+=x_change
            thing_z+=thing_y
            cone_y+=thing_y
            Car.things(gameDisplay,thing_x,thing_z,thing_h,thing_w,white)
            Car.car(x,y,gameDisplay)
            Car.cone(cone_x,cone_y,gameDisplay)
            Car.points(gameDisplay,("Score:"+str(score)))

            if x>ai_settings.screen_height or x<0   :
                Car.crash('YOu Crashed',gameDisplay,run_game)
            pygame.display.update()        
            gameDisplay.fill(ai_settings.bg_color)
            if thing_z>ai_settings.screen_height:
                thing_z=0
                score+=1

                Car.things(gameDisplay,thing_x,thing_z,thing_h,thing_w,white)
            if cone_y>ai_settings.screen_height:
                cone_y=0
                cone_x=random.randrange(0,ai_settings.screen_width)
                Car.cone(cone_x,cone_y,gameDisplay)
            if y<cone_y+120:
                if x<cone_x and x<cone_x +120 or x+120>cone_x and x+120<cone_x+120:
                    Car.crash('You Crashed on cone',gameDisplay,run_game)
            clock.tick(60)
run_game()
pygame.quit()
quit()