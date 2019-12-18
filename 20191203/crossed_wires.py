""" Solution to Day 3: Crossed Wires from adventofcode.com """

# Function to find the final position given a starting position and a path
def find_coordinates(initial, path):
    # Path is a list of directions in the format (left/right, distance)
    (x, y) = (initial[0], initial[1])
    coords = [(x, y)]
    for direction in path:
        if direction[0] == 'R':
            coords.extend([tuple((x+i, y)) for i in range(1, int(direction[1])+1)])
        elif direction[0] == 'L':
            coords.extend([tuple((x-i, y)) for i in range(1, int(direction[1])+1)])
        elif direction[0] == 'U':
            coords.extend([tuple((x, y+i)) for i in range(1, int(direction[1])+1)])
        elif direction[0] == 'D':
            coords.extend([tuple((x, y-i)) for i in range(1, int(direction[1])+1)])
        (x, y) = coords[-1]
    return coords

# Read input file
paths = []
with open('20191203/small.txt') as f:
    for line in f:
        paths.append(line.strip('\n').split(','))

# For each wire, find all the coordinates
wire1 = find_coordinates((0,0), paths[0])
wire2 = find_coordinates((0,0), paths[1])