import math
import random
import json
import sys
from sets import Set

from grid_info import *

mainwidth = 18

prompt = "Which netlist (1-6)? > "
error_wrong_input = "Please enter a number (1-6)"

while True:
    rawnetlist = raw_input(prompt)
    try:
        netlistnum = int(rawnetlist)
    except ValueError:
        print error_wrong_input
        sys.exit(1)
    else:
        if netlistnum <= 3:
            maingrid = grid1
            mainheight = 13
        else:
            maingrid = grid2
            mainheight = 17
        if netlistnum == 1:
            mainnetlist = netlist_1
            break
        elif netlistnum == 2:
            mainnetlist = netlist_2
            break
        elif netlistnum == 3:
            mainnetlist = netlist_3
            break
        elif netlistnum == 4:
            mainnetlist = netlist_4
            break
        elif netlistnum == 5:
            mainnetlist = netlist_5
            break
        elif netlistnum == 6:
            mainnetlist = netlist_6
            break
        else:
            print error_wrong_input
            sys.exit(1)

class Chip(object):
    def __init__(self, width, height, grid):
        self.width = mainwidth
        self.height = mainheight
        self.bottomlayer = [[0 for i in range(self.width)] for i in range(self.height)]
        self.grid = grid
        self.reset()
    def reset(self):
        self.obstacles = Set()
        for gate in self.grid:
            name, x, y = gate
            self.bottomlayer[y][x] = name
            self.obstacles.add((x, y, 0))
    def print_gatelayer(self):
        for row in self.bottomlayer:
            print row

mainchip = Chip(mainwidth, mainheight, maingrid)
mainchip.print_gatelayer()
