import pygame
display_width=900
display_height=720

display=pygame.display.set_mode((display_width,display_height))
x = (display_width * 0.45)
y = display_height * 0.8
x_change = 0
negx = 0
posx = 0
bun_speed = 0
white = (255, 255, 255)


while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    crashed = True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        posx = 0
                        if negx != -5:
                            negx = negx - 1
                            x_change = negx
                        elif negx == -5:
                            negx = 0
                            x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        negx = 0
                        if posx != 5:
                            posx = posx + 1
                            x_change = posx
                        elif posx == 5:
                            posx = 0
                            x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        x_change = 0
                elif event.key == pygame.K_RIGHT:
                        x_change = 0
            x += x_change

            display.fill(white)
            bunny(x,y)

            pygame.display.update()
            clock.tick(60)