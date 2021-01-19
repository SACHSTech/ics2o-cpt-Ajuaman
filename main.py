  
import pygame
import settings as s
import time
import random
from random import randint

pygame.init()
pygame.font.init()
collide_counter = 0
life_to_subtract = 0
life_left = 50000

def floor_looper():
    screen.blit(floor_surface, (s.floorX, 900))
    screen.blit(floor_surface, (s.floorX + 576, 900))

# CREATING VIRUS OBSTACLES
def create_virus():
    random_virus_position = randint(0, 800)
    new_virus = virus_surface.get_rect(midtop = (700, random_virus_position))
    return new_virus

def move_virus(viruses):
    for virus in viruses:
        virus.centerx -=10
    return viruses

def draw_virus(viruses):
    for virus in viruses:
        screen.blit(virus_surface, virus)

# SOME INITIALIZATION OF OUR FRAME
size = (s.WIDTH, s.HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("(Kinda) Fake Flappy Bird")

programIcon = pygame.image.load('assets/bird.png')

pygame.display.set_icon(programIcon)

font = pygame.font.SysFont('Comic Sans MS', 20)
troll_font_surface = font.render('haha jk no flabby birb', False, (0, 0, 0))
dodge_font_surface = font.render('dodge da viruses! they are computer malware and they hurt!!!', False, (0, 0, 0))
lives_text = font.render("Life left:", False, (0, 0, 0))

run = True
transparent = (0, 0, 0, 0)
# SETTING A BACKGROUND
bg_surface = pygame.image.load("assets/back.png").convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load("assets/base.png")
floor_surface = pygame.transform.scale2x(floor_surface)

player_surface = pygame.image.load("assets/bird.png")
player_surface = pygame.transform.scale(player_surface, (70, 70))
player_rect = player_surface.get_rect()

game_over_surface = pygame.transform.scale2x(pygame.image.load("assets/message.png")).convert_alpha()
game_over_ract = game_over_surface.get_rect(center = (288, 512))

virus_surface = pygame.image.load('assets/virus man.png')
virus_surface = pygame.transform.scale(virus_surface, (130, 130))
virus_list = []

# LIFE BAR
life_bar = pygame.Rect(110, 977, 200, 20)

SPAWNVIRUS = pygame.USEREVENT 

# SPAWN A VIRUS OBSTACLE EVERY 500 MILLISECOND
pygame.time.set_timer(SPAWNVIRUS, 500)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# FLAPPY SCREEN DETERMINES WHAT SCREEN YOU ARE ON. IF YOU ARE ON STARTUP SCREEN FLAPPY SCRREN WILL BE EQUAL TO 0. OTHERWISE, 1
flappy_screen = 0
# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop
        if event.type == SPAWNVIRUS:
            virus_list.append(create_virus())
             
    # GET KEY PRESSED FROM USER. STORE IN KEYS VARIABLE
    keys = pygame.key.get_pressed()
    # IF A CONTROL BUTTON IS PRESSED THE STARTUP SCREEN DISAPPEARS

    screen.blit(bg_surface, (0,0))

    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT] and flappy_screen == 0:
        game_over_surface.fill(transparent)
        screen.blit(troll_font_surface,(0,0))
        screen.blit(dodge_font_surface,(0, 50))
        flappy_screen = 1
        

    if keys[pygame.K_UP]:
        s.playerY -= s.player_jump_height
        if s.playerY < 0:
            s.playerY = 0

    elif keys[pygame.K_DOWN]:
        s.playerY += s.player_jump_height
        if s.playerY + 186 > s.HEIGHT:
            s.playerY = s.HEIGHT - 186 # 186 is just an arbitrary number that looks best in my opinion. No calculation.
            
    elif keys[pygame.K_RIGHT]:
        s.playerX += s.player_jump_height
        if s.playerX + 68 > s.WIDTH:
            s.playerX = s.WIDTH - 68 # 68 is just an arbitrary number that looks best in my opinion. No calculation.

    elif keys[pygame.K_LEFT]:
        s.playerX -= s.player_jump_height
        if s.playerX < 0:
            s.playerX = 0

    player_rect.centerx = s.playerX
    player_rect.centery = s.playerY

    # FLOOR LOOPS
    s.floorX -= 7
    floor_looper()

    # RESETING THE FLOORX POSITION ONCE IT REACHES A CERTAIN POSITION
    if s.floorX <= -576:
        s.floorX = 0

    screen.blit(floor_surface, (s.floorX, s.floorY))
    screen.blit(game_over_surface, game_over_ract)
    screen.blit(player_surface, (s.playerX, s.playerY))

    # DRAWING THE LIVES ICON
    
    screen.blit(lives_text,(10, 970))
    pygame.draw.rect(screen, s.GREEN, life_bar)
    if flappy_screen > 0:
        # VIRUSES
        virus_list = move_virus(virus_list)
        draw_virus(virus_list)
        for virus in virus_list:
            if player_rect.colliderect(virus):
                life_to_subtract += 1
                life_left -= life_to_subtract
                print(life_left)

    pygame.display.update()
     # --- Limit to 60 frames per second
    clock.tick(s.FPS)



pygame.quit()