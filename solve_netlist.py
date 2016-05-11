import math
import random
import json
from sets import Set

from grid_info import *

class Chip(object):
    def __init__(self, width, height, grid, netlist):
        self.maxlayers = 8
        self.width = width
        self.height = height
        self.bottomlayer = [[0 for i in range(self.width)] for i in range(self.height)]
        self.grid = grid
        self.netlist = netlist
        self.reset()
    def reset(self):
        self.wires = []
        self.obstacles = Set()
        for gate in self.grid:
            name, x, y = gate
            self.bottomlayer[y][x] = name
            self.obstacles.add((x, y, 0))
    def print_grid(self):
        for row in self.bottomlayer:
            print row
    def used_layers(self):
        return len(set([i[2] for i in self.obstacles]))

chip1 = Chip(18, 13, grid1, netlist_1)
chip2 = Chip(18, 13, grid1, netlist_2)
chip3 = Chip(18, 13, grid1, netlist_3)
chip4 = Chip(18, 17, grid2, netlist_4)
chip5 = Chip(18, 17, grid2, netlist_5)
chip6 = Chip(18, 17, grid2, netlist_6)

def manhattan(x, y):
    x1, x2, x3 = x
    y1, y2, y3 = y

    return math.fabs(x1 - y1) + math.fabs(x2 - y2) + math.fabs(x3 - y3)

def get_coord(name, grid):
    for gate in grid:
        if gate[0] == name:
            return (gate[1], gate[2], 0)

def on_chip(coord, chip):
    x, y, z = coord
    if x < 0 or x >= chip.width or y < 0 or y >= chip.height or z < 0 or z >= chip.maxlayers:
        return False
    return True

def make_neighbours(coord, chip, closedlist, obs):
    x, y, z = coord
    neighs = []
    # N
    north_neigh = (x, y - 1, z)
    if north_neigh not in closedlist and on_chip(north_neigh, chip) and north_neigh not in obs:
        neighs.append(north_neigh)
    # E
    east_neigh = (x + 1, y, z)
    if east_neigh not in closedlist and on_chip(east_neigh, chip) and east_neigh not in obs:
        neighs.append(east_neigh)
    # S
    south_neigh = (x, y + 1, z)
    if south_neigh not in closedlist and on_chip(south_neigh, chip) and south_neigh not in obs:
        neighs.append(south_neigh)
    # W
    west_neigh = (x - 1, y, z)
    if west_neigh not in closedlist and on_chip(west_neigh, chip) and west_neigh not in obs:
        neighs.append(west_neigh)
    # U
    up_neigh = (x, y, z + 1)
    if up_neigh not in closedlist and on_chip(up_neigh, chip) and up_neigh not in obs:
        neighs.append(up_neigh)
    # D
    down_neigh = (x, y, z - 1)
    if down_neigh not in closedlist and on_chip(down_neigh, chip) and down_neigh not in obs:
        neighs.append(down_neigh)

    return neighs

def Astar(startgate, goalgate, chip):
    start = {"node": get_coord(startgate + 1, chip.grid), "G": 0, "H": 0, "F": 0, "parent": None}
    goal = get_coord(goalgate + 1, chip.grid)
    print start["node"], "to", goal

    open_list = []
    closed_list = Set()
    open_list.append(start)

    obstacles = chip.obstacles
    obstacles_no_goal = [i for i in obstacles if i != goal]
    obstacles_gates_only = [i for i in obstacles if i != goal and chip.bottomlayer[i[1]][i[0]] != 0]

    while open_list:
        q = open_list.pop(open_list.index(min(open_list, key = lambda i: i["F"])))
        closed_list.add(q["node"])

        if q["node"] == goal:
            path = []
            while q["parent"] != None:
                path.append(q["node"])
                chip.obstacles.add(q["node"])
                q = q["parent"]
            path.append(q["node"])
            chip.obstacles.add(q["node"])
            path.reverse()
            return path

        neighbours = make_neighbours(q["node"], chip, closed_list, obstacles_no_goal)
        for nbour in neighbours:
            if nbour in [d["node"] for d in open_list]:
                new_G = q["G"] + 1
                oldnode = [i for i in open_list if i["node"] == nbour][0]
                if oldnode["G"] > new_G:
                    oldnode["G"] = new_G
                    oldnode["parent"] = q
            else:
                G = q["G"] + 1
                H = manhattan(nbour, goal)
                F = G + H
                open_list.append({"node": nbour, "G": G, "H": H, "F": F, "parent": q})

        if not open_list:
            neighbours = make_neighbours(q["node"], chip, closed_list, obstacles_gates_only)
            nbour = min(neighbours, key = lambda i: manhattan(i, goal))

            global paths
            for solution in paths:
                if type(solution) is not str:
                    if nbour in solution:
                        paths[paths.index(solution)] = "verwijderd"

                        for i in range(1, len(solution) - 1):
                            chip.obstacles.remove(solution[i])

            G = q["G"] + 1
            H = manhattan(nbour, goal)
            F = G + H
            open_list.append({"node": nbour, "G": G, "H": H, "F": F, "parent": q})

    return []

max_iterations = 1000

# Netlist 1
chip1.netlist = sorted(chip1.netlist, key = lambda i: manhattan(get_coord(i[0] + 1, chip1.grid), get_coord(i[1] + 1, chip1.grid)))
iteration = 0
paths = []
while len(paths) < len(chip1.netlist) and iteration < max_iterations and not any(i == "verwijderd" for i in paths):
    chip1.reset()
    paths = []
    iteration += 1
    print "Running iteration %d" % iteration
    for pair in chip1.netlist:
        path = Astar(pair[0], pair[1], chip1)
        if len(path) > 0:
            paths.append(path)
        else:
            break

    if len(paths) == len(netlist_1):
        its = 0
        while any(i == "verwijderd" for i in paths) and its < 200:
            its += 1
            print "Subiteration %d..." % its
            for i in range(len(chip1.netlist)):
                if paths[i] == "verwijderd":
                    path = Astar(chip1.netlist[i][0], chip1.netlist[i][1], chip1)
                    if len(path) > 0:
                        paths[i] = path
            random.shuffle(paths)

    random.shuffle(chip1.netlist)
    # if any(i == "verwijderd" for i in paths):
    #     continue

print "Netlist 1"
if len(paths) < len(chip1.netlist):
    print "Could not find a solution in %d iterations" % max_iterations
else:
    chip1.wires = paths[:]
    cost1 = 0
    for wire in chip1.wires:
        cost1 += len(wire) - 1
    print "Found a solution in %d iterations with cost %d" % (iteration, cost1)
    for i in range(len(chip1.netlist)):
        print "Path from %d to %d" % (chip1.netlist[i][0] + 1, chip1.netlist[i][1] + 1)
        print chip1.wires[i]
    print "Used %d layers" % chip1.used_layers()
    with open("nl1sol.py", "w") as f:
              f.write("solution = ")
              json.dump(paths, f)
print ""




# Astar(chip1)
# print chip1.obstacles
# chip1.print_grid()
# print "Used layers:", chip1.used_layers()
