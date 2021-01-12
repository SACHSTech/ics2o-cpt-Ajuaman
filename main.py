import pygame
import settings

pygame.init()

# SOME INITIALIZATION OF OUR FRAME
size = (settings.WIDTH, settings.HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platformer")
 
run = True

# SETTING A BACKGROUND

bg_surface = pygame.image.load("assets/back.png")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop
  
    screen.blit(bg_surface, (0,0))

    # --- Limit to 60 frames per second
    clock.tick(settings.FPS)

pygame.quit()