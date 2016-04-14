##
# Chips & Circuits
# Team Paprikachips
##

class Layer(object):
    def __init__(self):
        print "Hallo, wereld"

chip = Layer()

grid = [
    [1, 0, 2],
    [0, 3, 0],
    [0, 4, 0]
]

wires = [
    [{"n": 0, "e": 1}],
    []
]

print grid[1][1]
