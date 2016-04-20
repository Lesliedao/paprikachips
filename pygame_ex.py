##
# Chips & Circuits
# Team Paprikachips
# Programma om de data te visualiseren.
##
 
import pygame
 
# De game engine initialiseren. 
pygame.init()
 
# Variabelen voor de kleuren.
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

 
# Stelt de groote van het scherm van de visualisatie vast.
screenlength = 500
screenwidth = 400
size = (screenwidth, screenlength)
screen = pygame.display.set_mode(size)
 
# Stelt de naam van het scherm vast.
pygame.display.set_caption("Pygame: A* pathfinder for chips and circuits")
 
# Loop todat de gebruiker het scherm afsluit.
exit = False
clock = pygame.time.Clock()
while not exit:
 
    # Zorgt ervoor dat de loop stopt als de gebruiker het scherm afsluit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True  
 
    # Zet de achtergrond van de visualisatie op wit.
    screen.fill(WHITE)

    def makegrid(blocks_x, blocks_y):
        line_length_hor = blocks_x * 15
        line_length_vert = blocks_y * 15
        line_counter = 0

        # Bepalen van de start en eindpunten van de lijnen.
        pointx = (screenwidth - line_length_hor) / 2 # 65
        startpointy = (screenlength - line_length_vert) / 2 # 152,5
        endpointy = screenlength - startpointy # 347,5

        # While loop voor de lijnen op de x-as, dus de verticale lijnen.
        while line_counter != (blocks_x + 1):
            pygame.draw.line(screen, BLACK, [pointx, startpointy], [pointx, endpointy])
            pointx = pointx + 15
            line_counter = line_counter + 1


        line_counter = 0

        # Bepalen van de start en eindpunten van de lijnen.
        pointy = (screenlength - line_length_vert) / 2 # 152,5
        startpointx = (screenwidth - line_length_hor) / 2 # 65
        endpointx = screenwidth - startpointx # 335

        # While loop voor de lijnen op de y-as, dus de horizontale lijnen.
        while line_counter != (blocks_y + 1):
            pygame.draw.line(screen, BLACK, [startpointx, pointy], [endpointx, pointy])
            pointy = pointy + 15
            line_counter = line_counter + 1

    # Maakt het daadwerkelijke grid met het meegegeven aantal blokjes.
    makegrid(18, 13)
 
    # Maakt de verschillende teksten op het scherm aan. 
    font = pygame.font.SysFont('Helvetica', 25, True, False)
    text = font.render("Chips and circuits: Grid 1", True, BLACK)
    text_next = font.render("Next layer", True, BLACK)
    text_prev = font.render("Previous layer", True, BLACK)
 
    # Zet de verschillende texten op de juiste plek (MOET NOG AAN GRID WORDEN AANGEPAST).
    screen.blit(text, [50, 50])
    screen.blit(text_next, [50, 300])
    screen.blit(text_prev, [190, 300])
    pygame.display.flip()
 
    # Iets om later zorgen over te maken (limits the while loop to a max of 60 times per second).
    clock.tick(60)
 
# Stopt de visualisatie.
pygame.quit()