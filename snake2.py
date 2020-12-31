#Attempt #2 at snake, half guided, half self.
#sdfghjklkljhggfghgjk
import pygame
import time
import random

pygame.init()

#colors!
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
snake_color = (0, 220, 190)

#display setup
display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake")

#Snake and game speed
clock = pygame.time.Clock()
s_chunk = 10
s_speed = 15


#Our collective boi
def the_Snake(s_chunk, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, snake_color, [x[0], x[1], s_chunk, s_chunk])


#Message box.
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)
def message(msg, color):
    m_msg = font_style.render(msg, True, color)
    display.blit(m_msg, [display_width/6, display_height/3])


def theGame():
    game_over = False
    game_close = False

    posx = display_width/2
    posy = display_height/2
    posx_change = 0
    posy_change = 0

    snake_list = []
    snake_length = 1

    pelletx = round(random.randrange(0, display_width-s_chunk)/10)*10
    pellety = round(random.randrange(0, display_height-s_chunk)/10)*10

    while not game_over:
        while game_close:
            display.fill(black)
            message("You lose. C - Try again. Q - Quit", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        theGame()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posx_change = s_chunk
                    posy_change = 0
                elif event.key == pygame.K_LEFT:
                    posx_change = -s_chunk
                    posy_change = 0
                elif event.key == pygame.K_DOWN:
                    posx_change = 0
                    posy_change = s_chunk
                elif event.key == pygame.K_UP:
                    posx_change = 0
                    posy_change = -s_chunk

        if posx >= display_width or posx < 0 or posy >= display_height or posy < 0:
            game_close = True
        posx += posx_change
        posy += posy_change
        display.fill(black)
        pygame.draw.rect(display, red, [pelletx, pellety, s_chunk, s_chunk])
        snake_Head = []
        snake_Head.append(posx)
        snake_Head.append(posy)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        the_Snake(s_chunk, snake_list)
        pygame.display.update()

        if posx == pelletx and posy == pellety:
            pelletx = round(random.randrange(0, display_width - s_chunk) / 10) * 10
            pellety = round(random.randrange(0, display_height - s_chunk) / 10) * 10
            snake_length += 1

        clock.tick(s_speed)

    pygame.quit()
    quit()


theGame()


