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
playerX_change = 0


def player(x,y):
    # We DRAW the image, that is what blit means
    screen.blit(playerImg, (x,y))


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

        # If key is pressed, check if it's left or right key
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -3
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke has been released")

    playerX += playerX_change
    player(playerX,playerY)

    pygame.display.update()

