# pylint: disable=C0103,C0111,C0303,C0301,C0330
##
# Chips & Circuits
# Team Paprikachips
# Programma om de ondergrens te berekenen.
##

# Importeer math module.
import math
# Importeer de grids en netlists uit externe file grid_info.
from grid_info import *
from Queue import PriorityQueue

class Chip(object):
    # Zorg dat chip gerest kan worden nadat algorithme is gebruikt
    # @resettable
    # Houd het maximum aantal lagen, de lagen zelf, breedte en hoogte en de
    # draden bij.
    def __init__(self, width, height, grid):
        self.maxlayers = 7
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
    # Start een nieuw draad.
    def add_new_wire(self, x, y, z = 0):
        self.wires.append(Wire(x, y, z))
    # Voeg een segment aan een bestaande draad toe.
    def add_wire_segment(self, x, y, z = 0, wire_index = -1):
        if self.detect_collision(x, y, z):
            print "Obstacle detected. Adding wire segment aborted."
        else:
            self.wires[wire_index].extend_wire(x, y, z)
    # Functie om de gates aan de chip toe te voegen.
    def add_gate(self, gate, x, y, z = 0):
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
    # Functie om alle draden op een chip te laten printen.
    def print_wires(self):
        for wire in self.wires:
            print wire.path
    def print_obstacles(self):
        print self.obstacles
    # Bekijk of een draad een gate of een andere draad snijdt.
    def detect_collision(self, x, y, z):
        if (x, y, z) in self.obstacles:
            return True
        return False
    def connect_gates(self, x1, y1, z1, x2, y2, z2):
        start = (x1, y1, z1)
        goal = (x2, y2, z2)
    def reset_chip(self):
        pass
        # TODO: algoritme bepaalt stuk voor stuk waar elk draad komt

        # Als het volgende stuk draad de rest met goal verbindt, check dan niet op collision
        # TODO: voeg het pad pas aan obstacles toe als het hele pad af is
        # for node in self.wires[-1].path:
        #     self.obstacles.append(node)

    #TODO: functie voor elk van de algoritmes
    #TODO: reset de chip
    def dijkstra_algorithm(object):
        pass
    def lee_algorithm(self):
        pass
    def a_star_algorithm(object):
        pass
    def depth_first (object):
        pass


# Wire houdt een list path bij met coordinaten waar het draad loopt.
class Wire(object):
    def __init__(self, x, y, z):
        self.path = []
        self.path.append((x, y, z))
    # Voeg een segment toe aan dit draad naar de coordinaten (x, y, z).
    def extend_wire(self, x, y, z):
        self.path.append((x, y, z))

# Chip 1 definieren
chip1 = Chip(18, 13, grid1)
# chip1.print_grid()
# chip1.print_obstacles()
# print ""

# Chip 2 definieren
chip2 = Chip(18, 17, grid2)
# chip2.print_grid()
# chip2.print_obstacles()
# print ""

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

# Bepaal de coordinaten van een gate in een grid
def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 0)

# Out of bounds functie
def out_of_bounds(x, y, z, width, height, n_layers):
    if x < 0 or x >= width or y < 0 or y >= height or z < 0 or z >= n_layers:
        return True
    return False

def Astar(startgate, goalgate, chip):
    # A* test
    found_path = False
    # Initialiseer een open list
    open_list = []
    # Initialiseer een closed list
    closed_list = []
    grid = chip.grid

    # Plaats de start node in de open list, waarvan de F op 0 kan blijven
    start = {"node": get_coord(startgate, grid), "F": manhattan(get_coord(startgate, grid), get_coord(goalgate, grid)), "parent": None}
    goal = get_coord(goalgate, grid)
    open_list.append(start)

    obstacles = chip.obstacles
    obstacles_filtered = [x for x in obstacles if x != goal]

    # Zolang de open list niet leeg is
    while open_list:
        # Zoek de node met de laagste F in open_list, noem deze q en pop deze uit
        # open_list
        q = open_list.pop(open_list.index(min(open_list, key = lambda x: x["F"])))
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
            if child == goal:
                # Stop the search
                found_path = True
                end = {"node": child, "F": 0, "parent": q}
                break
            F = manhattan(child, goal)
            if not any(d["node"] == child for d in open_list) and not any(d["node"] == child for d in closed_list):
                open_list.append({"node": child, "F": F, "parent": q})
        closed_list.append(q)
        if found_path:
            # Build a path
            path = []
            current = end
            while True:
                path.insert(0, current["node"])
                current = current["parent"]
                if current == None:
                    break
                else:
                    continue
            break

        # TODO: backtracking als er geen pad te vinden is
        if not open_list and not found_path:
            # backtrack
            pass

    if found_path:
        for node in path:
            if node not in chip.obstacles:
                chip.obstacles.append(node)
        print "Found path from %d to %d" % (startgate, goalgate)
        return path
    else:
        print "Could not find a path from %d to %d" % (startgate, goalgate)
        return []

for i in netlist_1:
    Astar(i[0] + 1, i[1] + 1, chip1)

# Berekenen van de ondergrens met behulp van de manhattan distance.
# Ondergrens netlist 1
wire_length = 0
for i in netlist_1:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 1: %d" % wire_length

# Ondergrens netlist 2
wire_length = 0
for i in netlist_2:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 2: %d" % wire_length

# Ondergrens netlist 3
wire_length = 0
for i in netlist_3:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 3: %d" % wire_length

# Ondergrens netlist 4
wire_length = 0
for i in netlist_4:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 4: %d" % wire_length

# Ondergrens netlist 5
wire_length = 0
for i in netlist_5:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 5: %d" % wire_length

# Ondergrens netlist 6
wire_length = 0
for i in netlist_6:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 6: %d" % wire_length
