import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

displayX = 800
displayY = 600

blockSize = 10

FPS = 15

gameDisplay = pygame.display.set_mode((displayX, displayY))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()


def snake():
    gameExit = False

    lead_x = displayX / 2
    lead_y = displayY / 2
    lead_x_change = 0
    lead_y_change = 0
    keyX = True
    keyY = True

    snakeX = []
    snakeY = []

    while not gameExit:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and keyY:
                    lead_x_change = -blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("left")

                elif event.key == pygame.K_RIGHT and keyY:
                    lead_x_change = blockSize
                    lead_y_change = 0
                    keyX = True
                    keyY = False
                    print("right")

                elif event.key == pygame.K_UP and keyX:
                    lead_y_change = -blockSize
                    lead_x_change = 0
                    keyX = False
                    keyY = True
                    print("up")

                elif event.key == pygame.K_DOWN and keyX:
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

        if lead_y >= displayY - 20 or lead_y < 0 + 20 :
            lead_y_change = 0
            # lead_x_change = blockSize
            # keyY = True
            # keyX = False



        print(lead_x, lead_y)

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, blockSize, blockSize])
        pygame.draw.rect(gameDisplay, red, [0, 0, 10, 600])
        pygame.draw.rect(gameDisplay, red, [0, 0, 800, 10])
        pygame.draw.rect(gameDisplay, red, [0, 590, 800, 10])
        pygame.draw.rect(gameDisplay, red, [790, 0, 10, 600])

        # pygame.draw.rect(gameDisplay, red, [400, 300, 10, 10])

        pygame.display.update()

        clock.tick(FPS)


snake()

pygame.quit()

quit()
