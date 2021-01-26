'''
-------------------------------------------------------------------------------
Name:		main.py
Purpose:	Main game functionality goes in here
Author:	Chin.T
Created: 010/1/2021
------------------------------------------------------------------------------
'''

import pygame
import settings as s
import time
import random
from random import randint
import math

pygame.init()
pygame.font.init()

# GENERAL VARIABLES
collide_counter = 0
life_to_subtract = 0
life_left = 50000
run = True
transparent = (0, 0, 0, 0)

# RANDOM POSITION
random_antivirus_positionY = randint(0, 800)


# LOOPING THE FLOOR TO CREATE INFINITE SCROLL ILLUSION
def floor_looper():
    screen.blit(floor_surface, (s.floorX, 900))
    screen.blit(floor_surface, (s.floorX + 576, 900))

# CREATING VIRUS OBSTACLES
def create_virus():
    random_virus_positionX = randint(600, 900)
    random_virus_positionY = randint(0, 800)
    new_virus = virus_surface.get_rect(midtop = (random_virus_positionX, random_virus_positionY))
    return new_virus

def move_virus(viruses):
    for virus in viruses:
        virus.centerx -=10
    return viruses

def draw_virus(viruses):
    for virus in viruses:
        screen.blit(virus_surface, virus)

# DRAWING ANTI VIRUSES FUNCTIONS
def create_antivirus():
    random_antivirus_positionX = randint(600, 1000)
    random_antivirus_positionY = randint(0, 800)
    new_antivirus = antivirus_surface.get_rect(midtop = (random_antivirus_positionX, random_antivirus_positionY))
    return new_antivirus

def move_antivirus(antiviruses):
    for antivirus in antiviruses:
        antivirus.centerx -= 10
    return antiviruses

def draw_antivirus(antiviruses):
    for antivirus in antiviruses:
        screen.blit(antivirus_surface, antivirus)


def calculate_healthbar_length(hp_remaining):
    return math.floor(((200 * hp_remaining)/50000))

# SOME INITIALIZATION OF OUR FRAME
size = (s.WIDTH, s.HEIGHT)
screen = pygame.display.set_mode(size)

# TITLE
pygame.display.set_caption("(Kinda) Fake Flappy Bird")

# SETTING THE PROGRAM LOGO TO THE BIRD
programIcon = pygame.image.load('assets/bird.png')

pygame.display.set_icon(programIcon)

# DEALING WITH FONTS AND SIZES 
font = pygame.font.SysFont('Comic Sans MS', 20)
lives_text = font.render("Life left:", False, (0, 0, 0))


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

antivirus_surface = pygame.image.load('assets/pog box.png')
antivirus_surface = pygame.transform.scale(antivirus_surface, (90, 90))
antivirus_list = []

endgame_surface = pygame.image.load('assets/endgame.png')
endgame_surface = pygame.transform.scale2x(endgame_surface)

SPAWNVIRUS = pygame.USEREVENT 
SPAWNANTIVIRUS = pygame.USEREVENT + 1
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# FLAPPY SCREEN DETERMINES WHAT SCREEN YOU ARE ON. IF YOU ARE ON STARTUP SCREEN FLAPPY SCRREN WILL BE EQUAL TO 0. OTHERWISE, 1
flappy_screen = 0

pygame.time.set_timer(SPAWNVIRUS, 500)
pygame.time.set_timer(SPAWNANTIVIRUS, 10000)

# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            run = False # Flag that we are done so we exit this loop
        if flappy_screen == 1 and event.type == SPAWNVIRUS:
            virus_list.append(create_virus())
        if flappy_screen == 1 and event.type == SPAWNANTIVIRUS:
            antivirus_list.append(create_antivirus())
    
    # LIFE BAR LOGIC
    life_bar = pygame.Rect(110, 977, calculate_healthbar_length(life_left), 20)

    # GET KEY PRESSED FROM USER. STORE IN KEYS VARIABLE
    keys = pygame.key.get_pressed()
    
    # IF A CONTROL BUTTON IS PRESSED THE STARTUP SCREEN DISAPPEARS

    screen.blit(bg_surface, (0,0))

    if (keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]) and flappy_screen == 0:
        game_over_surface.fill(transparent)
        
        # CHANGING THE VALUE OF flappy_screen
        flappy_screen = 1

    # LOGIC FOR DETERMINING PLAYER MOVEMENTS
    if keys[pygame.K_UP]:
        s.playerY -= s.player_jump_height
        # CREATING BOUNDARIES
        if s.playerY < 0:
            s.playerY = 0

    elif keys[pygame.K_DOWN]:
        s.playerY += s.player_jump_height
         # CREATING BOUNDARIES
        if s.playerY + 186 > s.HEIGHT:
            s.playerY = s.HEIGHT - 186 # 186 is just an arbitrary number that looks best in my opinion. No calculation.
            
    elif keys[pygame.K_RIGHT]:
        s.playerX += s.player_jump_height
         # CREATING BOUNDARIES
        if s.playerX + 68 > s.WIDTH:
            s.playerX = s.WIDTH - 68 # 68 is just an arbitrary number that looks best in my opinion. No calculation.

    elif keys[pygame.K_LEFT]:
        s.playerX -= s.player_jump_height
         # CREATING BOUNDARIES
        if s.playerX < 0:
            s.playerX = 0

    # MOVING THE PLAYER'S RECTANGLE COLLIDER WITH THE PLAYER
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
    
    if flappy_screen > 0:
        # VIRUSES
        virus_list = move_virus(virus_list)
        draw_virus(virus_list)

        # ANTIVIRUSES
        antivirus_list = move_antivirus(antivirus_list)
        draw_antivirus(antivirus_list)

        for virus in virus_list:
            if player_rect.colliderect(virus):
                life_to_subtract += 10
                life_left -= life_to_subtract
                print(calculate_healthbar_length(life_left))
            pygame.draw.rect(screen, s.GREEN, life_bar)

        for antivirus in antivirus_list:
            if player_rect.colliderect(antivirus):
                life_to_subtract -= 10
                life_left += life_to_subtract
                print(calculate_healthbar_length(life_left))
            pygame.draw.rect(screen, s.GREEN, life_bar)
    

    # GAME LOGIC HERE
    if calculate_healthbar_length(life_left) <= 0:
        screen.blit(bg_surface, (0,0))
        screen.blit(endgame_surface, (100, 412))
        screen.blit(floor_surface, (s.floorX, s.floorY))

        # LOOP THE FLOOR AGAIN
        s.floorX -= 2
        floor_looper()

        # RESETING THE FLOORX POSITION ONCE IT REACHES A CERTAIN POSITION
        if s.floorX <= -576:
            s.floorX = 0

    # UPDATING THE SCREEN
    pygame.display.update()

     # --- Limit to 60 frames per second
    clock.tick(s.FPS)




pygame.quit()