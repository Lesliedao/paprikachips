##
# Chips & Circuits
# Team Paprikachips
##

class Layer(object):
    def __init__(self):
        print "Hallo, wereld"

chip = Layer()

grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 16],
    [0, 21, 0],
    [0, 0, 22],
    [0, 24, 0],
    [0, 0, 0]
]

print grid[1][1]
