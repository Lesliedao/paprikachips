import math
from grid_info import *

grid = [(1, 1, 1), (2, 6, 1), (3, 10, 1), (4, 15, 1), (5, 3, 2), (6, 12, 2), (7, 14, 2), (8, 12, 3), (9, 8, 4),
(10, 1, 5), (11, 4, 5), (12, 11, 5), (13, 16, 5), (14, 13, 6), (15, 16, 6), (16, 2, 8), (17, 6, 8), (18, 9, 8),
(19, 11, 8), (20, 15, 8), (21, 1, 9), (22, 2, 10), (23, 9, 10), (24, 1, 11), (25, 12, 11)]

startpoint = grid[2]
endpoint = grid[4]
visited_list = []

east_child = ((startpoint[0]), (startpoint[1] + 1), (startpoint[2]))
west_child = ((startpoint[0]), (startpoint[1] - 1), (startpoint[2]))
north_child = ((startpoint[0]), (startpoint[1]), (startpoint[2] - 1))
south_child = ((startpoint[0]), (startpoint[1]), (startpoint[2] + 1))
print "child coordinates: e->", east_child, "w->", west_child, "n->", north_child, "s->", south_child

# Functie voor het berekenen van de manhattan distance.
def manhattan(x, y):
	x1, x2, x3 = x
	y1, y2, y3 = y
	return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

def check_shortest(east_child, west_child, north_child, south_child):
	leslies_list = [east_child, west_child, north_child, south_child]
	
	east_child_man = manhattan(east_child, endpoint)
	west_child_man = manhattan(west_child, endpoint)
	north_child_man = manhattan(north_child, endpoint)
	south_child_man = manhattan(south_child, endpoint)
	print "manhattans:", east_child_man, west_child_man, north_child_man, south_child_man
	
	sort = [east_child_man, west_child_man, north_child_man, south_child_man]
	return leslies_list[sort.index(min(sort))]

shortie = check_shortest(east_child, west_child, north_child, south_child)
print "shortie:", shortie
