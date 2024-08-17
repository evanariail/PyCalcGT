import math
import pygame
import numpy as np
import sys
import time

pygame.init()

state = "main"

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

gtext = ''
goutput = ''

input_text = font.render(text, True, BLACK, WHITE)
input_rect = input_text.get_rect()
input_rect.topleft = (0, 20)

graph_input_text = font.render(gtext, True, BLACK, WHITE)
graph_input_rect = graph_input_text.get_rect()
graph_input_rect.topleft = (0, 20)

cursor = pygame.Rect(input_rect.topright, (3, input_rect.height))

output_text = font.render(output, True, BLACK, WHITE)
output_rect = output_text.get_rect()
output_rect.topright = (750, 40)

graph_output_text = font.render(goutput, True, BLACK, WHITE)
graph_output_rect = output_text.get_rect()
graph_output_rect.topright = (750, 40)

graphswitch_text = font.render("Graphing", True, BLACK, WHITE)
graphswitch_textRect = graphswitch_text.get_rect()
graphswitch_textRect.bottomleft = (20, 580)
graphswitch_rect = pygame.Rect(graphswitch_textRect.left - 5, graphswitch_textRect.top - 5, graphswitch_textRect.width + 10, graphswitch_textRect.height + 10)

mainswitch_text = font.render("Return", True, BLACK, WHITE)
mainswitch_textRect = mainswitch_text.get_rect()
mainswitch_textRect.bottomleft = (730, 580)
mainswitch_rect = pygame.Rect(mainswitch_textRect.left - 5, mainswitch_textRect.top - 5, mainswitch_textRect.width + 10, mainswitch_textRect.height + 10)


def calculate(expression):
    try:
         output = eval(expression)
         return str(output)
    except:
         return "Error"

def main_screen():
    screen.fill(WHITE)
    screen.blit(intro_text, intro_textRect)
    pygame.draw.rect(screen, BLACK, graphswitch_rect, 3)
    screen.blit(graphswitch_text, graphswitch_textRect)
    screen.blit(input_text, input_rect)
    screen.blit(output_text, output_rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, BLACK, cursor) 
    pygame.display.update()

def graphing_screen():
    screen.fill(WHITE)
    graph_intro_text = font.render('Welcome to the Graphing Window!', True, BLACK, WHITE)
    graph_intro_textRect = graph_intro_text.get_rect()
    pygame.draw.rect(screen, BLACK, mainswitch_rect, 3)
    screen.blit(graph_intro_text, graph_intro_textRect)
    screen.blit(mainswitch_text, mainswitch_textRect)
    screen.blit(graph_input_text, graph_input_rect)
    screen.blit(graph_output_text, graph_output_rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, BLACK, cursor)
    pygame.display.update()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if state == "main" and graphswitch_textRect.collidepoint(mouse_pos):
                state = "graphing"
                cursor.topleft = graph_input_rect.topright
            if state == "graphing" and mainswitch_textRect.collidepoint(mouse_pos):
                state = "main"
                cursor.topleft = graph_input_rect.topright
        if state == "main":   
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
        if state == "graphing":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(gtext) > 0:
                        gtext = gtext[:-1]
                else:
                    gtext += event.unicode
                
                graph_input_text = font.render(gtext, True, BLACK, WHITE)
                graph_input_rect.size = graph_input_text.get_size()
                cursor.topleft = graph_input_rect.topright

    if state == "main":
        main_screen()
    if state == "graphing":
        graphing_screen()
        
    #keys = pygame.key.get_pressed()    #trying to figure out how to make BACKSPACE keep going if held down
    #if keys[pygame.K_BACKSPACE]:
        #if len(text) > 0:
            #text = text[:-1]