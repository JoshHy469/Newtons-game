import pygame
import random
pygame.init()
win = pygame.display.set_mode((500,500))
#issac coordinates and image
x = 250
y = 400
xspeed = 2
yspeed = 4
issac = pygame.image.load("output-onlinepngtools (2).png")

#list 
applex = 250
appley = -25
while True: 
  win.fill((255,255,255))
  pygame.time.delay(20)
  pygame.event.pump()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a]:
    x = x - 10
  if keys[pygame.K_d]:
    x = x + 10
  

  appley += yspeed
  if appley > 525:
    applex = random.randint(50,450)
    appley = -25
  radius = 15
  pygame.draw.circle(win, (255, 45, 0), (applex,appley), radius)
  #barriers
  if x < 0:
    x = 0
  if x > 430:
    x = 430
  
  
 
  
  win.blit(issac,(x,y))

  pygame.display.update()
