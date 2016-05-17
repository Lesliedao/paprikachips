##
# Chips & Circuits
# Team Paprikachips
# Programma om de data te visualiseren.
# Werkt met python 3. Om te runnen, gebruik: python3 ./pygame_ex.py
##

import pygame
import math
import sys
import grid_info
# from test import *
from solution import *
import time

# De game engine initialiseren.
pygame.init()

# Variabelen voor de kleuren.
GREY2 = (120, 120, 120)
BLACK = (0,0,0)
GREY = (200,200,200)
WHITE = (255, 255, 255)
RED = (239,138,98)
BLUE = (0,99,104)

# Stelt de groote van elementen van de visualisatie vast.
screenlength = 500
screenwidth = 400
block_size = 22
grid_font_size = 9
current_layer = 0
node_size = 8
max_layer = 0
for path in solution:
    for i in range(len(path)):
        if path[i][2] > max_layer:
            max_layer = path[i][2]

block_am_x = int(sys.argv[1]) #17 #17
block_am_y = int(sys.argv[2]) #12 #16
if block_am_y == 12:
    maingrid = getattr(grid_info, "grid1")
else:
    maingrid = getattr(grid_info, "grid2")

size = (screenwidth, screenlength)
screen = pygame.display.set_mode(size)

# Stelt de naam van het scherm vast.
pygame.display.set_caption("Pygame: A* pathfinder for chips and circuits")

# Loop todat de gebruiker het scherm afsluit.
exit = False
clock = pygame.time.Clock()
while not exit:

    # Zorgt ervoor dat de loop stopt als de gebruiker het scherm afsluit.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Zet de achtergrond van de visualisatie op wit.
    screen.fill(WHITE)

    # Maakt de verschillende teksten op het scherm aan.
    font_title = pygame.font.SysFont('Helvetica', 30, True, False)
    font_other = pygame.font.SysFont('Helvetica', 14, True, False)
    font_grid = pygame.font.SysFont('Helvetica', grid_font_size, True, False)
    text_title = font_title.render("Current layer %d" % current_layer, True, BLACK)
    text_next = font_other.render("Next layer", True, BLACK)
    text_prev = font_other.render("Previous layer", True, BLACK)

    line_length_hor = block_am_x * block_size
    line_length_vert = block_am_y * block_size

    # Bepalen van de banners rond de grid.
    banner_left = (screenwidth - line_length_hor) / 2 # 65
    banner_right = screenwidth - banner_left # 335
    banner_top = (screenlength - line_length_vert) / 2 # 152,5
    banner_bottom = screenlength - banner_top # 347,5

    def distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return math.sqrt(math.fabs(x1 - x2)**2 + math.fabs(y1 - y2)**2)

    def make_grid(blocks_x, blocks_y, node_list):
        # While loop voor de lijnen op de x-as, dus de verticale lijnen.
        line_counter = 0
        x_start = banner_left
        while line_counter != (blocks_x + 1):
            pygame.draw.line(screen, GREY2, [x_start, banner_top], [x_start, banner_bottom])
            x_start = x_start + block_size
            line_counter = line_counter + 1

        # While loop voor de lijnen op de y-as, dus de horizontale lijnen.
        line_counter = 0
        y_start = banner_top
        while line_counter != (blocks_y + 1):
            pygame.draw.line(screen, GREY2, [banner_left, y_start], [banner_right, y_start])
            y_start = y_start + block_size
            line_counter = line_counter + 1

        pygame.draw.rect(screen, GREY, (65, (banner_top + line_length_vert + 20), 14, 14))
        pygame.draw.rect(screen, GREY, ((screenwidth - 195), (banner_top + line_length_vert + 20), 14, 14))

        # Zet de verschillende texten op de juiste plek.
        screen.blit(text_title, [20, (banner_top - 50)])
        screen.blit(text_next, [65 + 22, (banner_top + line_length_vert + 20)])
        screen.blit(text_prev, [(screenwidth - 195) + 22, (banner_top + line_length_vert + 20)])


        # Zet de threads op de grid.
        for i in range (len (solution) -1):
            for j in range (len (solution[i]) - 1):
                if solution[i][j][2] == current_layer:
                    pygame.draw.line(screen, BLUE, (int(banner_left + (solution[i][j][0] * block_size)), int(banner_top + (solution[i][j][1] * block_size))), (int(banner_left + (solution[i][j+1][0] * block_size)), int(banner_top + (solution[i][j+1][1] * block_size))), 3)


        # Zet de nodes met nummers op de grid.
        if current_layer == 0:
            for i in node_list:
                node_number = font_grid.render("%d" %i[0], True, BLACK)
                pygame.draw.circle(screen, RED, (int(banner_left + (i[1] * block_size)), int(banner_top+ (i[2] * block_size))), node_size, 0)
                screen.blit(node_number, [int(banner_left + (i[1] * block_size)) - 4, int(banner_top+ (i[2] * block_size)) - 4])

        # Laat zien waar de threads naar boven of naar beneden gaan.
        for i in range (len (solution) -1):
            for j in range (len (solution[i]) - 1):
                if solution[i][j][2] == current_layer:
                    if solution[i][j+1][2] != current_layer:
                        pygame.draw.circle(screen, BLUE, (int(banner_left + (solution[i][j+1][0] * block_size)), int(banner_top + (solution[i][j+1][1] * block_size))), node_size - 4, 0)
                    if solution[i][j-1][2] != current_layer:
                        pygame.draw.circle(screen, BLUE, (int(banner_left + (solution[i][j-1][0] * block_size)), int(banner_top + (solution[i][j-1][1] * block_size))), node_size - 4, 0)

    # Verandert de layer als er op de next en previous buttons wordt geklikt.
    def button_pressed():
        global current_layer
        # Als "Next layer" wordt geklikt.
        if current_layer == max_layer:
            pass
        else:
            if distance(pygame.mouse.get_pos(), (65, banner_top + line_length_vert + 20)) < 14:
                current_layer += 1
        # Als "Previous layer" wordt geklikt.
        if current_layer != 0:
            if distance(pygame.mouse.get_pos(), ((screenwidth - 195), (banner_top + line_length_vert + 20))) < 14:
                current_layer -= 1


    # Maakt het daadwerkelijke grid met het meegegeven aantal blokjes.
    make_grid(block_am_x, block_am_y, maingrid)

    # Checkt of er geklikt wordt.
    if event.type == pygame.MOUSEBUTTONDOWN:
        button_pressed()
        time.sleep(0.15)

    # Geeft de images weer op het scherm.
    pygame.display.flip()

    # Iets om later zorgen over te maken (limits the while loop to a max of 60 times per second).
    clock.tick(60)

# Stopt de visualisatie.
pygame.quit()
