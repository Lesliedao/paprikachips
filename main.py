##
# Chips & Circuits
# Team Paprikachips
# Programma om de ondergrens te berekenen.
##

import math

class Chip(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.layers = []
        self.addLayer()
    def newLayer(self):
        return Layer(self.width, self.height)
    def addLayer(self):
        self.layers.append(self.newLayer())
    def addGate(self, gate, x, y):
        self.layers[0].grid[x][y] = gate

class Layer(object):
    def __init__(self, width, height):
        self.grid = [[0 for x in range(width)] for x in range(height)]
    def printGrid(self):
        for row in self.grid:
            print row

chip1 = Chip(18, 13)
chip1.addGate(1, 1, 1)
for layer in chip1.layers:
    layer.printGrid()

#TODO: collision detection
class Wire(object):
    def __init__(self):
        self.path = []
    def addNode(self, node):
        self.path.append(node)

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

thread = Wire()
print thread.path
thread.addNode(5)
thread.addNode(4)
print thread.path


# De layout van grid 1.
grid1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 11, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 13, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 15, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 16, 0, 0, 0, 17, 0, 0, 18, 0, 19, 0, 0, 0, 20, 0, 0],
    [0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 22, 0, 0, 0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 25, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Lists met de nodes die met elkaar verbonden moeten worden.
netlist_1 = [(23, 4), (5, 7), (1, 0), (15, 21), (3, 5), (7, 13), (3, 23), (23, 8), (22, 13), (15, 17), (20, 10), (15, 8), (13, 18), (19, 2), (22, 11), (10, 4), (11, 24), (3, 15), (2, 20), (3, 4), (20, 19), (16, 9), (19, 5), (3, 0), (15, 5), (6, 14), (7, 9), (9, 13), (22, 16), (10, 7)]

# wires = [
#     [{"n": 0, "e": 1, "w": 0, "s": 1, "u": 0, "d": 0}],
#     []
# ]

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

# Berekenen van de ondergrens met behulp van de manhattan distance.
wire_length = 0

for i in netlist_1:
	wire_length += manhattan(i[0]+1, i[1]+1, grid1)

print wire_length
