import pygame

# Initialize the Pygame
pygame.init()

# Create the screen 800px x 600px
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("SPACE INVADERS GAME")


# Main Game Loop
running = True
while running:
    for event in pygame.event.get():

        # event.type -> <Event(12-Quit {})>
        if event.type == pygame.QUIT:
            running = False

