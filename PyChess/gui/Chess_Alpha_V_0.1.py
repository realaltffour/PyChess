import pygame

pygame.init()

board_h = 512
board_w = 512

windowSize = [board_h, board_w]

screen = pygame.display.set_mode(windowSize)

board_img = pygame.image.load('~\assest\CA.png')

x = 0
y = 0

screen.blit(board_img, (x , y), (C, D, E, F))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()

pygame.quit