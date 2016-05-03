import math
from grid_info import netlist_1

def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

# print manhattan((0, 0, 0), (2, 2, 1))

def get_coord(gate, grid):
    for i in grid:
        if i[0] == gate:
            return (i[1], i[2], 3)


grid1 = [(1, 1, 1), (2, 6, 1), (3, 10, 1), (4, 15, 1), (5, 3, 2), (6, 12, 2), (7, 14, 2), (8, 12, 3), (9, 8, 4),
(10, 1, 5), (11, 4, 5), (12, 11, 5), (13, 16, 5), (14, 13, 6), (15, 16, 6), (16, 2, 8), (17, 6, 8), (18, 9, 8),
(19, 11, 8), (20, 15, 8), (21, 1, 9), (22, 2, 10), (23, 9, 10), (24, 1, 11), (25, 12, 11)]

# print get_coord(11, grid1)
# print manhattan(get_coord(1, grid1), get_coord(11, grid1))
# print manhattan(get_coord(21, grid1), get_coord(22, grid1))

# Out of bounds functie
def out_of_bounds(x, y, z, width, height, n_layers):
    if x < 0 or x >= width or y < 0 or y >= height or z < 0 or z >= n_layers:
        return True
    return False

def Astar(startgate, goalgate, grid):
    # A* test
    found_path = False
    # Initialiseer een open list
    open_list = []
    # Initialiseer een closed list
    closed_list = []

    # Plaats de start node in de open list, waarvan de F op 0 kan blijven
    start = {"node": get_coord(startgate, grid), "F": manhattan(get_coord(startgate, grid), get_coord(goalgate, grid)), "parent": None}
    goal = get_coord(goalgate, grid)
    open_list.append(start)

    # Zolang de open list niet leeg is
    while open_list:
        # Zoek de node met de laagste F in open_list, noem deze q en pop deze uit
        # open_list
        q = open_list.pop(open_list.index(min(open_list, key = lambda x: x["F"])))
        # TODO: Check of child een obstacle is voordat je appendt aan children
        # Genereer de (6, n/e/s/w/u/d) children van q en zet hun parent op q
        children = []
        # North child
        if not out_of_bounds(q["node"][0], q["node"][1] - 1, q["node"][2], 18, 13, 7):
            children.append((q["node"][0], q["node"][1] - 1, q["node"][2]))
        # East child
        if not out_of_bounds(q["node"][0] + 1, q["node"][1], q["node"][2], 18, 13, 7):
            children.append((q["node"][0] + 1, q["node"][1], q["node"][2]))
        # South child
        if not out_of_bounds(q["node"][0], q["node"][1] + 1, q["node"][2], 18, 13, 7):
            children.append((q["node"][0], q["node"][1] + 1, q["node"][2]))
        # West child
        if not out_of_bounds(q["node"][0] - 1, q["node"][1], q["node"][2], 18, 13, 7):
            children.append((q["node"][0] - 1, q["node"][1], q["node"][2]))
        # Up child
        if not out_of_bounds(q["node"][0], q["node"][1], q["node"][2] + 1, 18, 13, 7):
            children.append((q["node"][0], q["node"][1], q["node"][2] + 1))
        # Down child
        if not out_of_bounds(q["node"][0], q["node"][1], q["node"][2] - 1, 18, 13, 7):
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
    return path

# astar_list = Astar(1, 22, grid1)

netlist_1 = sorted(netlist_1, key = lambda i: manhattan(get_coord(i[0] + 1, grid1), get_coord(i[1] + 1, grid1)))

print netlist_1
