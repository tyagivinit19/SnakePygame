from random import randrange

import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = pygame.Color("#00b906")
red = (255, 0, 0)

displayX = 800
displayY = 600

blockSize = 10

FPS = 15

gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)


def scoreDisplay(score, color):
    text = font.render(score, True, color)
    gameDisplay.blit(text, [300, 300])
    print("msg")


def increseLength(snakeX, snakeY):
    snakeX.append(snakeX[-1] - 10)
    snakeY.append(snakeY[-1] - 10)


def snake():
    gameExit = False

    lead_x = displayX / 2
    lead_y = displayY / 2
    lead_x_change = 0
    lead_y_change = 0
    keyX = True
    keyY = True

    foodX = randrange(10, 780)
    foodY = randrange(10, 580)

    score = 0

    image = pygame.image.load("background.png")
    image = pygame.transform.scale(image, (displayX, displayY))

    snakeX = [lead_x]
    snakeY = [lead_y]

    while not gameExit:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and keyY and not lead_x == 10:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("left")

                elif event.key == pygame.K_RIGHT and keyY and not lead_x == 780:
                    lead_x_change = blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("right")

                elif event.key == pygame.K_UP and keyX and not lead_y == 10:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                    keyX = False
                    keyY = True
                    print("up")

                elif event.key == pygame.K_DOWN and keyX and not lead_y == 580:
                    lead_y_change = blockSize
                    lead_x_change = 0
                    keyX = False
                    keyY = True
                    print("down")

        lead_x += lead_x_change
        lead_y += lead_y_change





        if lead_x >= displayX - 20 or lead_x < 0 + 20:
            lead_x_change = 0
            # lead_y_change = blockSize
            # keyX = True
            # keyY = False

        if lead_y >= displayY - 20 or lead_y < 0 + 20:
            lead_y_change = 0
            # lead_x_change = blockSize
            # keyY = True
            # keyX = False


        snakeX.pop(-1)
        snakeX.insert(0, lead_x)
        snakeY.pop(-1)
        snakeY.insert(0, lead_y)

        # print(lead_x, lead_y)

        if foodX - 10 <= lead_x <= foodX + 10 and foodY - 10 <= lead_y <= foodY + 10:
            foodX = randrange(10, 780)
            foodY = randrange(10, 580)
            score = score + 1
            scoreDisplay("you", red)
            increseLength(snakeX, snakeY)
            # pygame.display.update()

        gameDisplay.fill(black)
        # gameDisplay.blit(image, (0, 0))
        for i in range(1, len(snakeX)):
            pygame.draw.rect(gameDisplay, green, [snakeX[i], snakeY[i], blockSize, blockSize])
        pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, blockSize, blockSize])

        pygame.draw.rect(gameDisplay, red, [0, 0, 10, 600])
        pygame.draw.rect(gameDisplay, red, [0, 0, 800, 10])
        pygame.draw.rect(gameDisplay, red, [0, 590, 800, 10])
        pygame.draw.rect(gameDisplay, red, [790, 0, 10, 600])

        pygame.draw.rect(gameDisplay, red, [foodX, foodY, 10, 10])

        pygame.display.update()

        clock.tick(FPS)


snake()

pygame.quit()

quit()
