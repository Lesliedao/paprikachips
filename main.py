# pylint: disable=C0103,C0111,C0303,C0301,C0330,C0326
##
# Chips & Circuits
# Team Paprikachips
# Programma om de ondergrens te berekenen.
# Bron: http://web.mit.edu/eranki/www/tutorials/search/
# Bron: http://www.redblobgames.com/pathfinding/a-star/implementation.html
# Bron: https://gist.github.com/jamiees2/5531924
##

# Importeer modules
import math
import random
import json
# Importeer de grids en netlists uit externe file grid_info.
from grid_info import *

class Chip(object):
    # Houd het maximum aantal lagen, de lagen zelf, breedte en hoogte en de
    # draden bij.
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
            self.layers[3][y][x] = name
            self.obstacles.append((x, y, 3))
    # # Start een nieuw draad.
    # def add_new_wire(self, x, y, z = 3):
    #     self.wires.append(Wire(x, y, z))
    # # Voeg een segment aan een bestaande draad toe.
    # def add_wire_segment(self, x, y, z = 3, wire_index = -1):
    #     if self.detect_collision(x, y, z):
    #         print "Obstacle detected. Adding wire segment aborted."
    #     else:
            # self.wires[wire_index].extend_wire(x, y, z)
    # Functie om de gates aan de chip toe te voegen.
    def add_gate(self, gate, x, y, z = 3):
        if self.detect_collision(x, y, z):
            print "Obstacle detected. Adding gate aborted."
        else:
            self.layers[z][y][x] = gate
            self.obstacles.append((x, y, z))
    # Functie om alle lagen te laten printen.
    def print_grid(self):
        for i in range(len(self.layers)):
            print "Layer %d" % (i + 1)
            for row in self.layers[i]:
                print row
    # # Functie om alle draden op een chip te laten printen.
    # def print_wires(self):
    #     for wire in self.wires:
    #         print wire.path
    def print_obstacles(self):
        print self.obstacles
    # # Bekijk of een draad een gate of een andere draad snijdt.
    # def detect_collision(self, x, y, z):
    #     if (x, y, z) in self.obstacles:
    #         return True
    #     return False
    def reset(self):
        self.wires = []
        self.obstacles = []
        for gate in self.grid:
            name, x, y = gate
            self.layers[3][y][x] = name
            self.obstacles.append((x, y, 3))
    def used_layers(self):
        used = []
        for thing in self.obstacles:
            if thing[2] not in used:
                used.append(thing[2])
        return len(used)
    #TODO: functie voor elk van de algoritmes
    # def dijkstra_algorithm(self):
    #     pass
    # def lee_algorithm(self):
    #     pass
    # def a_star_algorithm(self):
    #     pass
    # def depth_first (self):
    #     pass

# # Wire houdt een list path bij met coordinaten waar het draad loopt.
# class Wire(object):
#     def __init__(self, x, y, z):
#         self.path = []
#         self.path.append((x, y, z))
#     # Voeg een segment toe aan dit draad naar de coordinaten (x, y, z).
#     def extend_wire(self, x, y, z):
#         self.path.append((x, y, z))

# Chips definieren
chip1 = Chip(18, 13, grid1)
chip2 = Chip(18, 13, grid1)
chip3 = Chip(18, 13, grid1)
chip4 = Chip(18, 17, grid2)
chip5 = Chip(18, 17, grid2)
chip6 = Chip(18, 17, grid2)

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

# Bepaal de coordinaten van een gate in een grid
def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 3)

# Out of bounds functie
def out_of_bounds(x, y, z, width, height, n_layers):
    if x < 0 or x >= width or y < 0 or y >= height or z < 0 or z >= n_layers:
        return True
    return False

def Astar(startgate, goalgate, chip):
    # Initialiseer een open list
    open_list = []
    # Initialiseer een closed list
    closed_list = []
    grid = chip.grid

    # Plaats de start node in de open list, waarvan de F op 0 kan blijven
    start = {"node": get_coord(startgate, grid), "G": 0, "F": 0, "parent": None}
    goal = get_coord(goalgate, grid)
    open_list.append(start)

    obstacles = chip.obstacles
    obstacles_filtered = [x for x in obstacles if x != goal]

    # Zolang de open list niet leeg is
    while open_list:
        # Zoek de node met de laagste F in open_list, noem deze q en pop deze uit
        # open_list
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

        # Genereer de (6, n/e/s/w/u/d) children van q en zet hun parent op q
        children = []
        # North child
        if not out_of_bounds(q["node"][0], q["node"][1] - 1, q["node"][2], chip.width, chip.height, chip.maxlayers) and (q["node"][0], q["node"][1] - 1, q["node"][2]) not in obstacles_filtered:
            children.append((q["node"][0], q["node"][1] - 1, q["node"][2]))
        # East child
        if not out_of_bounds(q["node"][0] + 1, q["node"][1], q["node"][2], chip.width, chip.height, chip.maxlayers) and (q["node"][0] + 1, q["node"][1], q["node"][2]) not in obstacles_filtered:
            children.append((q["node"][0] + 1, q["node"][1], q["node"][2]))
        # South child
        if not out_of_bounds(q["node"][0], q["node"][1] + 1, q["node"][2], chip.width, chip.height, chip.maxlayers) and (q["node"][0], q["node"][1] + 1, q["node"][2]) not in obstacles_filtered:
            children.append((q["node"][0], q["node"][1] + 1, q["node"][2]))
        # West child
        if not out_of_bounds(q["node"][0] - 1, q["node"][1], q["node"][2], chip.width, chip.height, chip.maxlayers) and (q["node"][0] - 1, q["node"][1], q["node"][2]) not in obstacles_filtered:
            children.append((q["node"][0] - 1, q["node"][1], q["node"][2]))
        # Up child
        if not out_of_bounds(q["node"][0], q["node"][1], q["node"][2] + 1, chip.width, chip.height, chip.maxlayers) and (q["node"][0], q["node"][1], q["node"][2] + 1) not in obstacles_filtered:
            children.append((q["node"][0], q["node"][1], q["node"][2] + 1))
        # Down child
        if not out_of_bounds(q["node"][0], q["node"][1], q["node"][2] - 1, chip.width, chip.height, chip.maxlayers) and (q["node"][0], q["node"][1], q["node"][2] - 1) not in obstacles_filtered:
            children.append((q["node"][0], q["node"][1], q["node"][2] - 1))
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
    return []

max_iterations = 100

# Netlist 1
iteration = 0
paths = []
while len(paths) < len(netlist_1) and iteration < max_iterations:
    chip1.reset()
    paths = []
    iteration += 1
    print "Running iteration %d" % iteration
    for i in netlist_1:
        path = Astar(i[0] + 1, i[1] + 1, chip1)
        if len(path) > 0:
            paths.append(path)
<<<<<<< HEAD
=======
        else:
            break
>>>>>>> 073d2467438e94e2302e3d3611b33d2979921478
    random.shuffle(netlist_1)

print "Netlist 1"
if len(paths) < len(netlist_1):
    print "Could not find a solution in %d iterations" % max_iterations
else:
    chip1.wires = paths[:]
    cost1 = 0
    for wire in paths:
        cost1 += len(wire) - 1
    print "Found a solution in %d iterations with cost %d" % (iteration, cost1)
    for i in range(len(netlist_1)):
        print "Path from %d to %d" % (netlist_1[i][0] + 1, netlist_1[i][1])
        print paths[i]
    print "Used %d layers" % chip1.used_layers()
    with open("netlist1sol.py", "w") as f:
        json.dump(paths, f)
print ""

<<<<<<< HEAD
# Netlist 2
# iteration = 0
# paths = []
# while len(paths) < len(netlist_2) and iteration < max_iterations:
#     chip2.reset()
#     paths = []
#     iteration += 1
#     print "Running iteration %d" % iteration
#     for i in netlist_2:
#         path = Astar(i[0] + 1, i[1] + 1, chip2)
#         if len(path) > 0:
#             paths.append(path)
#     random.shuffle(netlist_2)

# print "Netlist 2"
# if len(paths) < len(netlist_2):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     chip2.wires = paths[:]
#     cost2 = 0
#     for wire in paths:
#         cost2 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost2)
#     for i in range(len(netlist_2)):
#         print "Path from %d to %d" % (netlist_2[i][0] + 1, netlist_2[i][1])
#         print paths[i]
#     print "Used %d layers" % chip2.used_layers()
#     with open("netlist2sol.py", "w") as f:
=======
# # Netlist 2
# iteration = 0
# paths = []
# # Zolang de netlist nog niet geheel getraverseerd is en het maximal aantal iteraties nog niet is bereikt
# while len(paths) < len(netlist_2) and iteration < max_iterations:
#     # Reset de chip om eerere mislukte paden weg te halen
#     chip2.reset()
#     # Maak de padenlijst leeg
#     paths = []
#     # Voeg een iteratie toe en print het nummer ervan
#     iteration += 1
#     print "Running iteration %d" % iteration
#     # Zolang i(een paar van nodes waartussen je een pad zoekt) in de netlist zit
#     for i in netlist_2:
#         # Roep functie Astar aan voor startnode, goalnode en grid
#         path = Astar(i[0] + 1, i[1] + 1, chip2)
#         # Als er een pad is
#         if len(path) > 0:
#             #  Voeg deze toe aan de padenlijst
#             paths.append(path)
#         else:
#             break
#     # Shuffle willekeurig om nieuwe paden te vinden
#     random.shuffle(netlist_2)

# print "Netlist 2"
# # Als er minder paden zijn gevonden dan er nodecombinaties in de netlist zijn 
# if len(paths) < len(netlist_2):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     # Kopieer lijst van paths om wires in op te slaan
#     chip2.wires = paths[:]
#     # Zet kosten op 0
#     cost2 = 0
#     # Bereken kosten voor elke gelegde wire
#     for wire in paths:
#         cost2 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost2)
#     # Voor elke nodecombinatie in netlist 2
#     for i in range(len(netlist_2)):
#         # Print de oplossing (pad van sart naar goal)
#         print "Path from %d to %d" % (netlist_2[i][0] + 1, netlist_2[i][1])
#         print paths[i]
#     # Roep usd_layers aan en print het aantal layers
#     print "Used %d layers" % chip2.used_layers()
#     # Maak bestand aan met oplossingen voor visualisatie
#     with open("netlist2sol.py", "w") as f:
#         # Stop de paden hierin
>>>>>>> 073d2467438e94e2302e3d3611b33d2979921478
#         json.dump(paths, f)
# print ""

# # Netlist 3
# iteration = 0
# paths = []
# while len(paths) < len(netlist_3) and iteration < max_iterations:
#     chip3.reset()
#     paths = []
#     iteration += 1
#     print "Running iteration %d" % iteration
#     for i in netlist_3:
#         path = Astar(i[0] + 1, i[1] + 1, chip3)
#         if len(path) > 0:
#             paths.append(path)
#         else:
#             break
#     random.shuffle(netlist_3)

# print "Netlist 3"
# if len(paths) < len(netlist_3):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     chip3.wires = paths[:]
#     cost3 = 0
#     for wire in paths:
#         cost3 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost3)
#     for i in range(len(netlist_3)):
#         print "Path from %d to %d" % (netlist_3[i][0] + 1, netlist_3[i][1])
#         print paths[i]
#     print "Used %d layers" % chip3.used_layers()
#     with open("netlist3sol.py", "w") as f:
#         json.dump(paths, f)
# print ""

# # Netlist 4
# iteration = 0
# paths = []
# while len(paths) < len(netlist_4) and iteration < max_iterations:
#     chip4.reset()
#     paths = []
#     iteration += 1
#     print "Running iteration %d" % iteration
#     for i in netlist_4:
#         path = Astar(i[0] + 1, i[1] + 1, chip4)
#         if len(path) > 0:
#             paths.append(path)
#         else:
#             break
#     random.shuffle(netlist_4)

# print "Netlist 4"
# if len(paths) < len(netlist_4):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     chip4.wires = paths[:]
#     cost4 = 0
#     for wire in paths:
#         cost4 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost4)
#     for i in range(len(netlist_4)):
#         print "Path from %d to %d" % (netlist_4[i][0] + 1, netlist_4[i][1])
#         print paths[i]
#     print "Used %d layers" % chip4.used_layers()
#     with open("netlist4sol.py", "w") as f:
#         json.dump(paths, f)
# print ""

# # Netlist 5
# iteration = 0
# paths = []
# while len(paths) < len(netlist_5) and iteration < max_iterations:
#     chip5.reset()
#     paths = []
#     iteration += 1
#     print "Running iteration %d" % iteration
#     for i in netlist_5:
#         path = Astar(i[0] + 1, i[1] + 1, chip5)
#         if len(path) > 0:
#             paths.append(path)
#         else:
#             break
#     random.shuffle(netlist_5)

# print "Netlist 5"
# if len(paths) < len(netlist_5):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     chip5.wires = paths[:]
#     cost5 = 0
#     for wire in paths:
#         cost5 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost5)
#     for i in range(len(netlist_5)):
#         print "Path from %d to %d" % (netlist_5[i][0] + 1, netlist_5[i][1])
#         print paths[i]
#     print "Used %d layers" % chip5.used_layers()
#     with open("netlist5sol.py", "w") as f:
#         json.dump(paths, f)
# print ""

# # Netlist 6
# iteration = 0
# paths = []
# while len(paths) < len(netlist_6) and iteration < max_iterations:
#     chip6.reset()
#     paths = []
#     iteration += 1
#     print "Running iteration %d" % iteration
#     for i in netlist_6:
#         path = Astar(i[0] + 1, i[1] + 1, chip6)
#         if len(path) > 0:
#             paths.append(path)
#         else:
#             break
#     random.shuffle(netlist_6)

# print "Netlist 6"
# if len(paths) < len(netlist_6):
#     print "Could not find a solution in %d iterations" % max_iterations
# else:
#     chip6.wires = paths[:]
#     cost6 = 0
#     for wire in paths:
#         cost6 += len(wire) - 1
#     print "Found a solution in %d iterations with cost %d" % (iteration, cost6)
#     for i in range(len(netlist_6)):
#         print "Path from %d to %d" % (netlist_6[i][0] + 1, netlist_6[i][1])
#         print paths[i]
#     print "Used %d layers" % chip6.used_layers()
#     with open("netlist6sol.py", "w") as f:
#         json.dump(paths, f)
# print ""

# # Berekenen van de ondergrens met behulp van de manhattan distance.
# # Ondergrens netlist 1
# wire_length = 0
# for i in netlist_1:
#     wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
# print "Ondergrens netlist 1: %d" % wire_length
#
# # Ondergrens netlist 2
# wire_length = 0
# for i in netlist_2:
#     wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
# print "Ondergrens netlist 2: %d" % wire_length
#
# # Ondergrens netlist 3
# wire_length = 0
# for i in netlist_3:
#     wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
# print "Ondergrens netlist 3: %d" % wire_length
#
# # Ondergrens netlist 4
# wire_length = 0
# for i in netlist_4:
#     wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
# print "Ondergrens netlist 4: %d" % wire_length
#
# # Ondergrens netlist 5
# wire_length = 0
# for i in netlist_5:
#     wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
# print "Ondergrens netlist 5: %d" % wire_length
#
# # Ondergrens netlist 6
# wire_length = 0
# for i in netlist_6:
#     wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
# print "Ondergrens netlist 6: %d" % wire_length
