import pygame
from PIL import Image
import random

# Change the size of image(player.png)
image = Image.open('space-invaders.png')
player = image.resize((50, 50))
player.save('player.png')

# Change the size of image(enemy.png)
image2 = Image.open('silly.png')
enemy = image2.resize((60, 60))
enemy.save('enemy.png')

# Change the size of image(galaxy.png)
image3 = Image.open('kissing-galaxy.png')
galaxy = image3.resize((800, 600))
galaxy.save('galaxy.png')

# Change the size of image(bullet.png)
image4 = Image.open('bullet.png')
bul = image4.resize((30, 30))
bul.save('bul.png')


# Initialize the pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))  # 높이(height) 800, 너비(width) 600

# Background
background = pygame.image.load('galaxy.png')

# Title and Icon
pygame.display.set_caption("Space Invader by @rameon")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 150)
enemyX_change = 0.3
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load('bul.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 30


def player(x, y):  # Define Function player()
    screen.blit(playerImg, (x, y))  # 처음 player icon이 나타나는 위치를 지정함


def enemy(x, y):  # Define Function enemy()
    screen.blit(enemyImg, (x, y))  # 처음 enemy icon이 나타나는 위치를 지정함


    
# Game Loop
running = True
while running:
    # RGB - Screen에 점 채우기 후에 player 등이 나타나야함
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0,0))

    for event in pygame.event.get():  # event : 게임 내에서 일어나는 모든 일들(모든 input control)
        if event.type == pygame.QUIT:  # If exit button is pressed, then exit.
            running = False

        # If Key-stroke is pressed, check whether its right or left
        if event.type == pygame.KEYDOWN:  # 키보드가 눌렸을때
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:  # 키보드가 안눌렸을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    # player가 Screen 밖으로 벗어나지 않도록 함
    if playerX <= 0.0:
        playerX = 0.0
    elif playerX > 736.0:  # 800 - 64bit =736
        playerX = 736.0

    enemyX += enemyX_change
    # enemy가 Screen 밖으로 벗어나지 않도록 함
    if enemyX <= 0.0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX > 736.0:  # 800 - 64bit =736
        enemyX_change = -0.1
        enemyY += enemyY_change

    player(playerX, playerY)  # 위에서 define한 player() function을 무한 Game Loop 내에 포함시켜서 항상 player가 Screen에 나타나도록 함
    enemy(enemyX, enemyY)
    pygame.display.update()
