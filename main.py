import pygame
import settings

pygame.init()
size = (settings.WIDTH, settings.HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platformer")
 
run = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop
  
    screen.fill(settings.BLACK)
 
    # --- Limit to 60 frames per second
    clock.tick(settings.FPS)
pygame.quit()