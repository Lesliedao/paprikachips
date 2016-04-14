##
# Chips & Circuits
# Team Paprikachips
##

import math

class Layer(object):
    def __init__(self):
        print "Hallo, wereld"

chip = Layer()

grid = [
    [1, 0, 2],
    [0, 3, 0],
    [0, 4, 0]
]

# wires = [
#     [{"n": 0, "e": 1, "w": 0, "s": 1, "u": 0, "d": 0}],
#     []
# ]

# Bereken de manhattan distance
def manhattan(x, y):
    # Zoek de coordinaten van x
    for i in xrange(len(grid)):
        if x in grid[i]:
            x1 = i
            break

    for i in xrange(len(grid[x1])):
        if x == grid[x1][i]:
            x2 = i
            break

    # Zoek de coordinaten van y
    for i in xrange(len(grid)):
        if y in grid[i]:
            y1 = i
            break

    for i in xrange(len(grid[y1])):
        if y == grid[y1][i]:
            y2 = i
            break

    return math.fabs(x1 - y1) + math.fabs(x2 - y2)

print manhattan(1, 4)
