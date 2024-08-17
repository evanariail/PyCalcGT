import math
import pygame
import numpy as np
import sys
import time

pygame.init()

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption("PyCalcGT - Evan Ariail")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font('Cascadia.ttf', 14)

intro_text = font.render('Welcome to PyCalcGT v1.0! Enter a calculation to continue.', True, BLACK, WHITE)
intro_textRect = intro_text.get_rect()

text = ''
output = ''

input_text = font.render(text, True, BLACK, WHITE)
input_rect = input_text.get_rect()
input_rect.topleft = (0, 20)

cursor = pygame.Rect(input_rect.topright, (3, input_rect.height))

output_text = font.render(output, True, BLACK, WHITE)
output_rect = output_text.get_rect()
output_rect.topright = (750, 40)

def calculate(expression):
    try:
         output = eval(expression)
         return str(output)
    except:
         return "Error"
    

while True:
    clock.tick(60)

    screen.fill(WHITE)
    screen.blit(intro_text, intro_textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                 output = calculate(text)
                 output_text = font.render(output, True, BLACK, WHITE)
                 output_rect.size = output_text.get_size()
                 output_rect.topright = (750, 40)

            elif event.key == pygame.K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            else:
                text += event.unicode

            input_text = font.render(text, True, BLACK, WHITE)
            input_rect.size = input_text.get_size()
            cursor.topleft = input_rect.topright
        
    #keys = pygame.key.get_pressed()    #trying to figure out how to make BACKSPACE keep going if held down
    #if keys[pygame.K_BACKSPACE]:
        #if len(text) > 0:
            #text = text[:-1]

    if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, BLACK, cursor) 
    
    screen.blit(input_text, input_rect)
    screen.blit(output_text, output_rect)


    pygame.display.update()
