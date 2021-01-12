import pygame
import settings as s

pygame.init()

# SOME INITIALIZATION OF OUR FRAME
size = (s.WIDTH, s.HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platformer")
 
run = True

# SETTING A BACKGROUND

bg_surface = pygame.image.load("assets/back.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png")
floor_surface = pygame.transform.scale2x(floor_surface)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# screen.fill(settings.WHITE)
# screen.blit(bg_surface, (0,0))

# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop

    screen.blit(bg_surface, (0,0))

    s.floorX -=1
    screen.blit(floor_surface, (s.floorX, s.floorY))
    pygame.display.update()
     # --- Limit to 60 frames per second
    clock.tick(s.FPS)
pygame.quit()