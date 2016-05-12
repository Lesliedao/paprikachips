import math
from grid_info import *

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

# Bepaal de coordinaten van een gate in een grid.
def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 3)

# Berekenen van de ondergrens met behulp van de manhattan distance.
# Ondergrens netlist 1.
wire_length = 0
for i in netlist_1:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 1: %d" % wire_length

# Ondergrens netlist 2.
wire_length = 0
for i in netlist_2:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 2: %d" % wire_length

# Ondergrens netlist 3.
wire_length = 0
for i in netlist_3:
    wire_length += manhattan(get_coord(i[0]+1, grid1), get_coord(i[1]+1, grid1))
print "Ondergrens netlist 3: %d" % wire_length

# Ondergrens netlist 4.
wire_length = 0
for i in netlist_4:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 4: %d" % wire_length

# Ondergrens netlist 5.
wire_length = 0
for i in netlist_5:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 5: %d" % wire_length

# Ondergrens netlist 6.
wire_length = 0
for i in netlist_6:
    wire_length += manhattan(get_coord(i[0]+1, grid2), get_coord(i[1]+1, grid2))
print "Ondergrens netlist 6: %d" % wire_length
