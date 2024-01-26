import pygame
from Fighters import Fighter

pygame.init()

# Create game window
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Warrior Life")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# Colors
black  = (   0,   0,   0)
white  = ( 255, 255, 255)
yellow = ( 255, 255,   0)
green  = (   0, 255,   0)
red    = ( 255,   0,   0)
blue   = (   0,   0, 255)

# Define fighter variables
KRATOS_SIZE = 70
KRATOS_SCALE = 4
KRATOS_OFFSET = [42, 16]
KRATOS_DATA = [KRATOS_SIZE, KRATOS_SCALE, KRATOS_OFFSET]
ZOMBIE_SIZE = 250
ZOMBIE_SCALE = 3
ZOMBIE_OFFSET = [112, 107]
ZOMBIE_DATA = [ZOMBIE_SIZE, ZOMBIE_SCALE, ZOMBIE_OFFSET]

# Load backgroung image
bg_image = pygame.image.load("Fondo_Castillo.gif").convert_alpha()

# Load spritesheets
kratos_sheet = pygame.image.load("Kratosbetter.png").convert_alpha()
zombie_sheet = pygame.image.load("wizard.png").convert_alpha()

# Define number of steps in each animation
KRATOS_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
ZOMBIE_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

# Function for drawing backgroung
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, white, (x - 5, y - 5, 410, 50) )
    pygame.draw.rect(screen, red, (x, y, 400, 40) )
    pygame.draw.rect(screen, green, (x, y, 400 + ratio, 40) )

# Create two intances of fighters
fighter_1 = Fighter(200, 560, False, KRATOS_DATA, kratos_sheet, KRATOS_ANIMATION_STEPS)
fighter_2 = Fighter(1150, 560, True, ZOMBIE_DATA, zombie_sheet, ZOMBIE_ANIMATION_STEPS)

# Game loop
run = True
while run:

    clock.tick(FPS)

    # Draw background
    draw_bg()

    # Show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 980, 20)

    # Move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    # Update fighters
    fighter_1.update()
    fighter_2.update()

    # Draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    # Update display
    pygame.display.update()

# Exit game
pygame.quit()