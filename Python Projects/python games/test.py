import pygame
import sys 

# Pygame pls work
pygame.init()

# game window
screen_height = 800
screen_width = 1280
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shooter") #Title of window

# setting frame rate
clock = pygame.time.Clock()

# players
player_width = 75
player_height = 60
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 10 
player_speed = 5 

# Bullet settings 
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# main game loop 
while True:
 for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            # bullet at current player position
            bullet_x = player_x + player_width // 2 - bullet_width // 2
            bullet_y = player_y
            bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width,bullet_height))
 # Player movement
 keys = pygame.key.get_pressed()
 if keys[pygame.K_LEFT] and player_x > 0:
    player_x -= player_speed
 if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
    player_x += player_speed
 if keys[pygame.K_UP] and player_y > 0:
    player_y += player_speed
 if keys[pygame.K_DOWN] and player_y < screen_width - player_width:
    player_y -= player_speed
 # Update bullet positions
 for bullet in bullets:
    bullet.y -= bullet_speed

 # Remove bullets that are off the screen
 bullets = [bullet for bullet in bullets if bullet.y > 0 ]

 # screen color
 screen.fill((0, 0, 0))

 # Draw the player
 pygame.draw.rect(screen, (128,0, 128), (player_x,player_y, player_width, player_height))

 # display
 pygame.display.flip()

 # Frame rate cap
 clock.tick(60)






