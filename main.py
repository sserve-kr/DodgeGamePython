import pygame
from lib import scene
from lib import object
from lib import base

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Dodge Game In Python")

# SETUP

# SETUP END

clock = pygame.time.Clock()

finished = False
while not finished:
  fps = clock.tick(60)  # fps limited to 60
  timer = pygame.time.get_ticks()  # ms
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      finished = True
    # EVENTS
  # OBJECT / SCENE EVENTS
  
  screen.fill(white)
  # Draws
  pygame.display.flip()
      
pygame.quit()