import pygame, random

# Initialize the Pygame
pygame.init()

# Create the screen 'X' weight 800px - 'Y' height 600px
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('img/bg.png')

# Title and Icon
pygame.display.set_caption("SPACE INVADERS GAME")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('img/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40


def player(x, y):
    # We DRAW the image, that is what blit means
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # We DRAW the image, that is what blit means
    screen.blit(enemyImg, (x, y))


# Main Game Loop
running = True
while running:

    # I want that persistent in the window
    # We set the color in RGB(Red, Green, Blue) in the tuple
    screen.fill((50, 0, 0))
    # Background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():

        # event.type -> <Event(12-Quit {})>
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed, check if it's left or right key
        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -6
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 6
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("Keystroke has been released")

    # Create boundaries. Player cannot go over the screen limits
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Create boundaries. Enemy cannot go over the screen limits
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
