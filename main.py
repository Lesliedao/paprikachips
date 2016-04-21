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

class Chip(object):
    # Houd het maximum aantal lagen, de lagen zelf, breedte en hoogte en de
    # draden bij.
    def __init__(self, width, height):
        self.maxlayers = 7
        self.layers = [[[0 for x in range(width)] for x in range(height)] for x in range (self.maxlayers)]
        self.width = width
        self.height = height
        self.wires = []
        self.obstacles = []
    # Start een nieuw draad.
    def add_new_wire(self, x, y, z = 0):
        self.wires.append(Wire(x, y, z))
        self.obstacles.append((x, y, z))
    # Voeg een segment aan een bestaande draad toe.
    def add_wire_segment(self, x, y, z = 0, wire_index = -1):
        self.wires[wire_index].extend_wire(x, y, z)
        self.obstacles.append((x, y, z))
    # Functie om de gates aan de chip toe te voegen.
    def add_gate(self, gate, x, y, z = 0):
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
        # TODO: algoritme bepaalt stuk voor stuk waar elk draad komt
        # Als het volgende stuk draad de rest met goal verbindt, check dan niet op collision

# Wire houdt een list path bij met coordinaten waar het draad loopt.
class Wire(object):
    def __init__(self, x, y, z):
        self.path = []
        self.path.append((x, y, z))
    # Voeg een segment toe aan dit draad naar de coordinaten (x, y, z).
    def extend_wire(self, x, y, z):
        self.path.append((x, y, z))

#TODO: klasse voor elk van de algoritmes
class Dijkstra(object):
    def __init__(self):
        pass

class Lee(object):
    def __init__(self):
        pass

class Astar(object):
    def __init__(self):
        pass

# Chip 1 definieren
chip1 = Chip(18, 13)
for gateloc in grid1:
    chip1.add_gate(gateloc[0], gateloc[1], gateloc[2])
# chip1.print_grid()
# chip1.print_obstacles()
# print ""

# Chip 2 definieren
chip2 = Chip(18, 17)
for gateloc in grid2:
    chip2.add_gate(gateloc[0], gateloc[1], gateloc[2])
# chip2.print_grid()
# chip2.print_obstacles()
# print ""

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y, grid):
    # Vindt de coordinaten van x.
    for i in xrange(len(grid)):
        if x in grid[i]:
            x1 = i
            break

    for i in xrange(len(grid[x1])):
        if x == grid[x1][i]:
            x2 = i
            break

    # Vindt de coordinaten van y.
    for i in xrange(len(grid)):
        if y in grid[i]:
            y1 = i
            break

    for i in xrange(len(grid[y1])):
        if y == grid[y1][i]:
            y2 = i
            break

    return math.fabs(x1 - y1) + math.fabs(x2 - y2)

# chip3 = Chip(18, 13)
# chip3.add_new_wire(1, 1)
# chip3.add_wire_segment(2, 1)
# chip3.add_wire_segment(3, 1)
# chip3.add_wire_segment(4, 1)
# chip3.add_wire_segment(5, 1)
# chip3.add_wire_segment(6, 1)
# chip3.print_obstacles()

# Berekenen van de ondergrens met behulp van de manhattan distance.
# Ondergrens netlist 1
wire_length = 0
for i in netlist_1:
    wire_length += manhattan(i[0]+1, i[1]+1, chip1.layers[0])
print "Ondergrens netlist 1: %d" % wire_length

# Ondergrens netlist 2
wire_length = 0
for i in netlist_2:
    wire_length += manhattan(i[0]+1, i[1]+1, chip1.layers[0])
print "Ondergrens netlist 2: %d" % wire_length

# Ondergrens netlist 3
wire_length = 0
for i in netlist_3:
    wire_length += manhattan(i[0]+1, i[1]+1, chip1.layers[0])
print "Ondergrens netlist 3: %d" % wire_length

# Ondergrens netlist 4
wire_length = 0
for i in netlist_4:
    wire_length += manhattan(i[0]+1, i[1]+1, chip2.layers[0])
print "Ondergrens netlist 4: %d" % wire_length

# Ondergrens netlist 5
wire_length = 0
for i in netlist_5:
    wire_length += manhattan(i[0]+1, i[1]+1, chip2.layers[0])
print "Ondergrens netlist 5: %d" % wire_length

# Ondergrens netlist 6
wire_length = 0
for i in netlist_6:
    wire_length += manhattan(i[0]+1, i[1]+1, chip2.layers[0])
print "Ondergrens netlist 6: %d" % wire_length
