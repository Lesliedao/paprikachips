# pylint: disable=C0103,C0111,C0303,C0301,C0330,C0326
##
# Chips & Circuits
# Team Paprikachips
#
# Script voor het Chips & Circuits project, waarbij verschillende gates aan de
# hand van netlists met elkaar verbonden moeten worden. Hierbij wordt
# gebruikgemaakt van het A-star algoritme, wat het kortste pad tussen twee
# punten vindt.
#
# Bron: http://web.mit.edu/eranki/www/tutorials/search/
# Bron: http://www.redblobgames.com/pathfinding/a-star/implementation.html
# Bron: https://gist.github.com/jamiees2/5531924
##

# Importeer modules
import math
import random
import json
import sys
import subprocess
# Importeer de grids en netlists uit externe file grid_info.
import grid_info

# De breedte van elk grid is altijd 18
mainwidth = 18

##############
# User input #
##############
# Prompts en error berichten bij verkeerde input
netlistprompt = "Which netlist (1-6)? > "
sortprompt = "Would you like to sort the initial netlist (Y/N)? >"
error_wrong_input = "Please enter a number (1-6)"
error_wrong_sort = "Please enter either Y or N"

# Verkrijg user input
while True:
    rawnetlist = raw_input(netlistprompt)
    try:
        netlistnum = int(rawnetlist)
    except ValueError:
        print error_wrong_input
        sys.exit(1)
    else:
        # Check of een getal tussen 1 en 6 is ingevuld
        if netlistnum < 1 or netlistnum > 6:
            print error_wrong_input
            sys.exit(1)

        # Bepaal de lengte van een grid adhv het netlistnummer
        if netlistnum <= 3:
            maingrid = grid_info.grid1
            mainheight = 13
        else:
            maingrid = grid_info.grid2
            mainheight = 17


        # Maak een variabele adhv het netlistnummer en lees die variabele in uit
        # grid_info
        mainnetlist = getattr(grid_info, "netlist_" + str(netlistnum))
        break

#################
# Initiele sort #
#################
while True:
    # Vraag de user of hij de initiele netlist gesorteerd wil hebben op
    # manhattan distance
    initial_sort = raw_input(sortprompt).upper()
    if initial_sort == "Y" or initial_sort == "N":
        break
    else:
        print error_wrong_sort
        sys.exit(1)

class Chip(object):
    # Houd het maximum aantal lagen, de lagen zelf, breedte en hoogte en de draden bij.
    def __init__(self, width, height, grid):
        self.maxlayers = 8
        self.layers = [[[0 for x in range(width)] for x in range(height)] for x in range (self.maxlayers)]
        self.width = width
        self.height = height
        self.grid = grid
        self.wires = []
        self.obstacles = []
        for gate in self.grid:
            name, x, y = gate
            self.layers[0][y][x] = name
            self.obstacles.append((x, y, 0))
    # Functie om alle lagen te laten printen.
    def print_grid(self):
        for i in range(len(self.layers)):
            print "Layer %d" % (i + 1)
            for row in self.layers[i]:
                print row
    def reset(self):
        self.wires = []
        self.obstacles = []
        for gate in self.grid:
            name, x, y = gate
            self.layers[0][y][x] = name
            self.obstacles.append((x, y, 0))
    def used_layers(self):
        used = []
        for thing in self.obstacles:
            if thing[2] not in used:
                used.append(thing[2])
        return len(used)

# Chips definieren
mainchip = Chip(mainwidth, mainheight, maingrid)

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

# Bepaal de coordinaten van een gate in een grid.
def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 0)

# Bepaalt of een coordinaat op de chip zit
def on_chip(coord):
    x, y, z = coord
    if x < 0 or x >= mainchip.width or y < 0 or y >= mainchip.height or z < 0 or z >= mainchip.maxlayers:
        return False
    return True

# Maak kindjes adhv een coordinaat op de chip
def generate_children(coord, obs):
    x, y, z = coord
    children = []

    # Bepaal voor elke richting of het kind op de chip zit en of er geen
    # obstakel in de weg zit
    # Noord
    n_child = (x, y - 1, z)
    if on_chip(n_child) and n_child not in obs:
        children.append(n_child)
    # Oost
    e_child = (x + 1, y, z)
    if on_chip(e_child) and e_child not in obs:
        children.append(e_child)
    # Zuid
    s_child = (x, y + 1, z)
    if on_chip(s_child) and s_child not in obs:
        children.append(s_child)
    # West
    w_child = (x - 1, y, z)
    if on_chip(w_child) and w_child not in obs:
        children.append(w_child)
    # Up
    u_child = (x, y, z + 1)
    if on_chip(u_child) and u_child not in obs:
        children.append(u_child)
    # Down
    d_child = (x, y, z - 1)
    if on_chip(d_child) and d_child not in obs:
        children.append(d_child)

    return children

def Astar(startgate, goalgate, chip, netlist):
    # Initialiseer een open list.
    open_list = []
    # Initialiseer een closed list.
    closed_list = []
    grid = chip.grid

    # Plaats de start node in de open list, waarvan de F op 0 kan blijven.
    start = {"node": get_coord(startgate, grid), "G": 0, "F": 0, "parent": None}
    goal = get_coord(goalgate, grid)
    open_list.append(start)

    # Maak obstakellists aan voor alles, exclusief de doelcoordinaat, en alleen
    # voor de gates
    obstacles = chip.obstacles
    obstacles_filtered = [x for x in obstacles if x != goal]
    obstacles_gate_only = [x for x in obstacles if x != goal and chip.layers[x[2]][x[1]][x[0]] != 0]

    # Zolang de open list niet leeg is.
    while open_list:
        # Zoek de node met de laagste F in open_list, noem deze q en pop deze uit.
        q = open_list.pop(open_list.index(min(open_list, key = lambda x: x["F"])))
        closed_list.append(q)

        if q["node"] == goal:
            path = []
            while q["parent"] != None:
                path.append(q["node"])
                chip.obstacles.append(q["node"])
                q = q["parent"]
            path.append(q["node"])
            chip.obstacles.append(q["node"])
            path.reverse()
            return path

        # Genereer de (6, n/e/s/w/u/d) children van q en zet hun parent op q.
        children = generate_children(q["node"], obstacles_filtered)
        if len(children) > 0:
            for child in children:
                if child in [d["node"] for d in closed_list]:
                    continue
                if child in [d["node"] for d in open_list]:
                    new_G = q["G"] + 1
                    oldnode = [x for x in open_list if x["node"] == child][0]
                    if oldnode["G"] > new_G:
                        oldnode["G"] = new_G
                        oldnode["parent"] = q
                else:
                    G = q["G"] + 1
                    F = G + manhattan(child, goal)
                    open_list.append({"node": child, "G": G, "F": F, "parent": q})
        else:
            # Genereer toch kinderen, maar dan zonder obstakelcheck, behalve als het een gate is.
            children = generate_children(q["node"], obstacles_gate_only)
            # Kies een kind.
            baby = min(children, key = lambda x: manhattan(x, goal))
            # verwijder het obstakel (verwijder het HELE draad).
            global paths
            for sol in paths:
                if type(sol) is not str:
                    if baby in sol:
                        break
            # In paths, verbindt een string aan het verwijderde pad die zegt: verwijderd (sol is het obstakel draad).
            paths[paths.index(sol)] = "verwijderd"

            for i in range(1, len(sol) - 1):
                try:
                    chip.obstacles.remove(sol[i])
                except ValueError:
                    pass
            # Ga verder.
            G = q["G"] + 1
            F = G + manhattan(baby, goal)
            open_list.append({"node": baby, "G": G, "F": F, "parent": q})

    return []

# Het maximum aantal iteraties dat we willen doen om de netlist op te lossen
max_iterations = 1000

# Sorteer de initiele netlist als de user dat heeft aangegeven
if initial_sort == "Y":
    mainnetlist = sorted(mainnetlist, key = lambda i: manhattan(get_coord(i[0] + 1, maingrid), get_coord(i[1] + 1, maingrid)))
# Anders hussel hem willekeurig
else:
    random.shuffle(mainnetlist)

# Probeer de gehele netlist op te lossen met A-star
iteration = 0
paths = []
# Zolang niet alle paden gevonden zijn en het maximum aantal iteraties niet
# bereikt is
while len(paths) < len(mainnetlist) and iteration < max_iterations:
    # Reset de chip: alleen de gates zijn de obstakels in het begin
    mainchip.reset()
    paths = []
    iteration += 1
    print "Running iteration %d..." % iteration
    # Pas A-star toe op elk paar in de netlist
    for i in mainnetlist:
        path = Astar(i[0] + 1, i[1] + 1, mainchip, mainnetlist)
        # Als de lengte van het pad langer is dan 0, append hem dan en anders
        # break (geen pad kunnen vinden)
        if len(path) > 0:
            paths.append(path)
        else:
            break

    # Als de lengte van de padenlijst net zo lang is als de lengte van de
    # netlist, check of er paden verwijderd zijn en leg die opnieuw aan
    if len(paths) == len(mainnetlist):
        its = 0
        while any(i == "verwijderd" for i in paths) and its < 200:
            its += 1
            print "Subiteration %d..." % its
            for i in range(len(mainnetlist)):
                if paths[i] == "verwijderd":
                    path = Astar(mainnetlist[i][0] + 1, mainnetlist[i][1] + 1, mainchip, mainnetlist)
                    if len(path) > 0:
                        paths[i] = path
            random.shuffle(paths)

    random.shuffle(mainnetlist)

print "Netlist", netlistnum
# Als de lengte van de padenlijst korter is dan de lengte van de netlist, dan
# zijn niet alle paden gevonden
if len(paths) < len(mainnetlist):
    print "Could not find a complete solution in %d iterations" % max_iterations
    print "Try to find the maximum amount of connections instead"
# Als ze even lang zijn, zijn de paden gevonden. Laat dan de visualisatie
# automatisch zien
else:
    mainchip.wires = paths[:]
    maincost = 0
    for wire in paths:
        maincost += len(wire) - 1
    print "Found a solution in %d iterations with cost %d" % (iteration, maincost)
    with open("solution.py", "w") as f:
        f.write("# Solution for netlist " + str(netlistnum) + "\n")
        f.write("solution = ")
        json.dump(mainchip.wires, f)
        subprocess.Popen("python pygame_onderaan.py " + str(mainwidth - 1) + " " + str(mainheight - 1), shell = True)

