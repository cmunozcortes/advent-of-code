""" Solution to Day 3: Crossed Wires from adventofcode.com """
import re
import numpy as np

# Function to find the final position given a starting position and a path
def find_coordinates(initial, path):
    # Path is a list of directions in the format (left/right, distance)
    (x, y) = (initial[0], initial[1])
    coords = [(x, y)]
    for direction in path:
        distance = int(re.search(r'\d+', direction).group())
        if direction[0] == 'R':
            coords.extend([tuple((x+i, y)) for i in range(1, distance+1)])
        elif direction[0] == 'L':
            coords.extend([tuple((x-i, y)) for i in range(1, distance+1)])
        elif direction[0] == 'U':
            coords.extend([tuple((x, y+i)) for i in range(1, distance+1)])
        elif direction[0] == 'D':
            coords.extend([tuple((x, y-i)) for i in range(1, distance+1)])
        (x, y) = coords[-1]
        print((x, y))
    return coords

def calculate_manh_distance(initial, point):
    return (abs(point[0]-initial[0]) + abs(point[1]-initial[1]))

# Read input file
paths = []
with open('20191203/input.txt') as f:
    for line in f:
        paths.append(line.strip('\n').split(','))

# For each wire, find all the coordinates
init = (0,0)
wire1_coords = find_coordinates(init, paths[0])
wire2_coords = find_coordinates(init, paths[1])

# print('Wire 1: ', wire1_coords)
# print('Wire 2: ', wire2_coords)

# Find common points
# crossing_points = [point for point in wire1_coords if point in wire2_coords
# and point != init]
crossing_points = []
for point in wire1_coords:
    if point in wire2_coords and point != init:
        crossing_points.append(point)
print('Crossing points: ', crossing_points)

# Find Manhattan distance for each crossing point
distances = []
for point in crossing_points:
    manh_distance = calculate_manh_distance(init, point)
    distances.append(manh_distance)

# Smallest distance
min_distance = min(distances)
closest_crossing_point = crossing_points[distances.index(min_distance)]
print('Closest crossing point: ', closest_crossing_point)
print('Min distance: ', min_distance)