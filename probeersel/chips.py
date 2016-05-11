import math
import random
import json
import sys
from sets import Set

import grid_info

# De breedte van elke chip is 18
mainwidth = 18

##############
# User input #
##############
netlistprompt = "Which netlist (1-6)? > "
methodprompt = "Hill climbing (H) or random shuffle (R)? > "
error_wrong_input = "Please enter a number (1-6)"
error_wrong_method = "Please enter either H or R"

while True:
    rawnetlist = raw_input(netlistprompt)
    try:
        netlistnum = int(rawnetlist)
    except ValueError:
        print error_wrong_input
        sys.exit(1)
    else:
        if netlistnum < 1 or netlistnum > 6:
            print error_wrong_input
            sys.exit(1)

        if netlistnum <= 3:
            maingrid = grid_info.grid1
            mainheight = 13
        else:
            maingrid = grid_info.grid2
            mainheight = 17

        mainnetlist = getattr(grid_info, "netlist_" + str(netlistnum))
        break

###########
# Methode #
###########
while True:
    shufflemethod = raw_input(methodprompt)
    if shufflemethod == "H" or shufflemethod == "R":
        break
    else:
        print error_wrong_method
        sys.exit(1)

############
# Functies #
############
# Functie om de obstacles set te resetten (leeg te maken) voor meer iteraties
def reset(obs):
    obs.clear()
    for gate in maingrid:
        name, x, y = gate
        gatelayer[y][x] = name
        obstacles.add((x, y, 0))

# Functie om de manhattan afstand te bepalen tussen a en b
def manhattan(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b

    return math.fabs(x1 - x2) + math.fabs(y1 - y2) + math.fabs(z1 - z2)

# Functie om de coordinaten van een gate op de chip te bepalen
def get_coord(gate):
    for i in maingrid:
        if i[0] == gate:
            return (i[1], i[2], 0)

# Functie om te bepalen of een coordinaten tripel (x, y, z) op de chip zit
def on_chip(coord):
    x, y, z = coord
    if x < 0 or x >= mainwidth or y < 0 or y >= mainheight or z < 0 or z >= maxlayers:
        return False
    return True

# Functie om de neighbours van een coordinaat te genereren
def generate_neighbours(coord, obs):
    x, y, z = coord
    neighs = []

    # Noord
    n_neigh = (x, y - 1, z)
    if on_chip(n_neigh) and n_neigh not in obs:
        neighs.append(n_neigh)
    # Oost
    e_neigh = (x + 1, y, z)
    if on_chip(e_neigh) and e_neigh not in obs:
        neighs.append(e_neigh)
    # Zuid
    s_neigh = (x, y + 1, z)
    if on_chip(s_neigh) and s_neigh not in obs:
        neighs.append(s_neigh)
    # West
    w_neigh = (x - 1, y, z)
    if on_chip(w_neigh) and w_neigh not in obs:
        neighs.append(w_neigh)
    # Up
    u_neigh = (x, y, z + 1)
    if on_chip(u_neigh) and u_neigh not in obs:
        neighs.append(u_neigh)
    # Down
    d_neigh = (x, y, z - 1)
    if on_chip(d_neigh) and d_neigh not in obs:
        neighs.append(d_neigh)

    return neighs

###########################
# Chip/netlist variabelen #
###########################
# Het maximum aantal lagen op de chip
maxlayers = 8

# Het aantal verbindingen dat gelegd moet worden volgens de netlist
maxconnections = len(mainnetlist)

# Nested list met waar de gates zich bevinden op de hoofdlaag
gatelayer = [[0 for i in range(mainwidth)] for i in range(mainheight)]

# Obstacles is een set, voor snellere opzoektijden en houdt bij op welke coordinaten een obstakel is
obstacles = Set()

# Reset plaatst in dit geval de gates in de obstacles set
reset(obstacles)

####################
# A-star algoritme #
####################
def Astar(startgate, goalgate):
    open_list = []
    closed_set = Set()

    start = {"node": get_coord(startgate), "G": 0, "H": 0, "F": 0, "parent": None}
    goal = get_coord(goalgate)
    open_list.append(start)

    global obstacles
    obstacles_filtered = set([i for i in obstacles if i != goal])
    obstacles_gates_only = set([i for i in obstacles if i != goal and gatelayer[i[1]][i[0]] != 0])

    while open_list:
        q = open_list.pop(open_list.index(min(open_list, key = lambda i: i["F"])))
        closed_set.add(q["node"])

        if q["node"] == goal:
            path = []
            while q["parent"] != None:
                path.append(q["node"])
                obstacles.add(q["node"])
                q = q["parent"]
            path.append(q["node"])
            obstacles.add(q["node"])
            path.reverse()
            return path

        neighbours = generate_neighbours(q["node"], obstacles_filtered)
        for nbour in neighbours:
            if nbour in closed_set:
                continue
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

        # Als je dit uncomment, loopt het algoritme vast
        # if not open_list:
        #     neighbours = generate_neighbours(q["node"], obstacles_gates_only)
        #     nbour = min(neighbours, key = lambda i: manhattan(i, goal))
        #
        #     global paths
        #     for solution in paths:
        #         if type(solution) is not str:
        #             if nbour in solution:
        #                 paths[paths.index(solution)] = "verwijderd"
        #
        #                 for i in range(1, len(solution) - 1):
        #                     obstacles.discard(solution[i])
        #
        #     G = q["G"] + 1
        #     H = manhattan(nbour, goal)
        #     F = G + H
        #     open_list.append({"node": nbour, "G": G, "H": H, "F": F, "parent": q})

    return []


########################
# mainnetlist oplossen #
########################
best_so_far = []
paths = []
indices = [i for i in range(maxconnections)]
max_iterations = 200

mainnetlist = sorted(mainnetlist, key = lambda i: manhattan(get_coord(i[0] + 1), get_coord(i[1] + 1)))
iteration = 0
while len(paths) < maxconnections and iteration < max_iterations:# and not any(x == "verwijderd" for x in paths):
    iteration += 1
    print "Running iteration %d..." % iteration
    paths = []
    reset(obstacles)
    for pair in mainnetlist:
        # print "Calculating path from %d to %d..." % (pair[0] + 1, pair[1] + 1)
        path = Astar(pair[0] + 1, pair[1] + 1)
        if len(path) > 0:
            paths.append(path)

    # Uncomment alleen als je oude draden ook weghaalt
    # if len(paths) == maxconnections:
    #     its = 0
    #     while any([x == "verwijderd" for x in paths]) and its < 200:
    #         its += 1
    #         print "Subiteration %d..." % its
    #         for i in range(maxconnections):
    #             if paths[i] == "verwijderd":
    #                 path = Astar(mainnetlist[i][0] + 1, mainnetlist[i][1] + 1)
    #                 if len(path) > 0:
    #                     paths[i] = path
    #         random.shuffle(paths)

    if len(paths) > len(best_so_far):# and not any(i == "verwijderd" for i in paths):
        iteration = 0
        best_so_far = paths[:]
        print "Current best: %d connections" % len(best_so_far)

    if shufflemethod == "H":
        # # # Kies twee willekeurige elementen in de netlist om te verwisselen (Hill climber)
        randi = random.sample(indices, 2)
        mainnetlist[randi[0]], mainnetlist[randi[1]] = mainnetlist[randi[1]], mainnetlist[randi[0]]
    else:
        # Shuffle de netlist willekeurig
        random.shuffle(mainnetlist)

print ""
print "Netlist", netlistnum
if len(best_so_far) < maxconnections:
    print "%d out of %d connections made" % (len(best_so_far), maxconnections)
else:
    print "Made all %d connections" % maxconnections

cost = 0
for wire in best_so_far:
    cost += len(wire) - 1
print "Cost: %d" % cost

# Niet altijd correct
# used_layers = len(set(i[2] for i in obstacles))
# print "Used %d layers" % used_layers
print ""

with open("solution.py", "w") as f:
    f.write("# Solution for netlist " + str(netlistnum) + "\n")
    f.write("solution = ")
    json.dump(best_so_far, f)

execfile("pygame_onderaan.py")
