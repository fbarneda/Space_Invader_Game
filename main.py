import pygame

# Initialize the Pygame
pygame.init()

# Create the screen 'X' weight 800px - 'Y' height 600px
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("SPACE INVADERS GAME")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480


def player():
    # We DRAW the image, that is what blit means
    screen.blit(playerImg, (playerX,playerY))


# Main Game Loop
running = True
while running:

    # I want that persistent in the window
    # We set the color in RGB(Red, Green, Blue) in the tuple
    screen.fill((50, 0, 0))

    for event in pygame.event.get():
        # event.type -> <Event(12-Quit {})>
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()

