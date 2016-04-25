import math


def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

print manhattan((0, 0, 0), (2, 2, 1))

def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 0)


grid1 = [(1, 1, 1), (2, 6, 1), (3, 10, 1), (4, 15, 1), (5, 3, 2), (6, 12, 2), (7, 14, 2), (8, 12, 3), (9, 8, 4),
(10, 1, 5), (11, 4, 5), (12, 11, 5), (13, 16, 5), (14, 13, 6), (15, 16, 6), (16, 2, 8), (17, 6, 8), (18, 9, 8),
(19, 11, 8), (20, 15, 8), (21, 1, 9), (22, 2, 10), (23, 9, 10), (24, 1, 11), (25, 12, 11)]

print get_coord(11, grid1)
print manhattan(get_coord(1, grid1), get_coord(11, grid1))
print manhattan(get_coord(21, grid1), get_coord(22, grid1))
