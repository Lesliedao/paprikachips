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
