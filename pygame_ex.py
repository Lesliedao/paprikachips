##
# Chips & Circuits
# Team Paprikachips
# Programma om de data te visualiseren.
# Werkt met python 3. Om te runnen, gebruik: python3 ./pygame_ex.py
##
 
import pygame
from grid_info import *
from test import *
 
# De game engine initialiseren. 
pygame.init()
 
# Variabelen voor de kleuren.
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
 
# Stelt de groote van elementen van de visualisatie vast.
screenlength = 500
screenwidth = 400
block_size = 22
grid_font_size = 9
node_size = 8

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
    font_other = pygame.font.SysFont('Helvetica', 20, True, False)
    font_grid = pygame.font.SysFont('Helvetica', grid_font_size, True, False)
    text_title = font_title.render("Chips and circuits: Grids", True, BLACK)
    text_next = font_other.render("Next layer", True, BLACK)
    text_prev = font_other.render("Previous layer", True, BLACK)

    def make_grid(blocks_x, blocks_y, node_list):
        line_length_hor = blocks_x * block_size
        line_length_vert = blocks_y * block_size
        line_counter = 0

        # Bepalen van de banners rond de grid.
        banner_left = (screenwidth - line_length_hor) / 2 # 65
        banner_right = screenwidth - banner_left # 335
        banner_top = (screenlength - line_length_vert) / 2 # 152,5
        banner_bottom = screenlength - banner_top # 347,5

        # While loop voor de lijnen op de x-as, dus de verticale lijnen.
        x_start = banner_left
        while line_counter != (blocks_x + 1):
            pygame.draw.line(screen, BLACK, [x_start, banner_top], [x_start, banner_bottom])
            x_start = x_start + block_size
            line_counter = line_counter + 1

        # While loop voor de lijnen op de y-as, dus de horizontale lijnen.
        line_counter = 0
        y_start = banner_top
        while line_counter != (blocks_y + 1):
            pygame.draw.line(screen, BLACK, [banner_left, y_start], [banner_right, y_start])
            y_start = y_start + block_size
            line_counter = line_counter + 1

        # Zet de verschillende texten op de juiste plek.
        screen.blit(text_title, [20, (banner_top - 50)])
        screen.blit(text_next, [65, (banner_top + line_length_vert + 20)])
        screen.blit(text_prev, [(screenwidth - 195), (banner_top + line_length_vert + 20)])

        for i in range (len (astar_list) -1):
            pygame.draw.line(screen, BLUE, (int(banner_left + (astar_list[i][0] * block_size)), int(banner_top + (astar_list[i][1] * block_size))), (int(banner_left + (astar_list[i+1][0] * block_size)), int(banner_top + (astar_list[i+1][1] * block_size))), 3)

        # Zet de nodes met nummers op de grid.
        for i in node_list:
            node_number = font_grid.render("%d" %i[0], True, BLACK)
            pygame.draw.circle(screen, RED, (int(banner_left + (i[1] * block_size)), int(banner_top+ (i[2] * block_size))), node_size, 0)
            screen.blit(node_number, [int(banner_left + (i[1] * block_size)) - 4, int(banner_top+ (i[2] * block_size)) - 4])
            
    # Maakt het daadwerkelijke grid met het meegegeven aantal blokjes.
    #make_grid(17, 12, grid1)
    make_grid(17, 16, grid2)
    
    # Geeft de images weer op het scherm.
    pygame.display.flip()
 
    # Iets om later zorgen over te maken (limits the while loop to a max of 60 times per second).
    clock.tick(60)
 
# Stopt de visualisatie.
pygame.quit()