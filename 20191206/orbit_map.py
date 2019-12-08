""" Solution to Day 6: Universal Orbit Map from adventofcode.com """
from collections import defaultdict

# Read input file and parse objects into a dictionary
orbit_map = {}
with open('20191206/small.txt') as f:
    for line in f:
        objs = line.strip('\n').split(')')
        # key, value -> node, parent
        orbit_map[objs[1]] = objs[0]

# For each object (value) in the orbit map find the number of orbits to COM 
orbit_count_dict = defaultdict(lambda:1)
for key, value in orbit_map.items():
    new_key = key
    new_value = value
    # while the value isn't 'COM, continue traversing the map
    # until getting to 'COM'
    if value == 'COM':
        orbit_count_dict[key] = 1
    else:
        while new_value != 'COM':
            orbit_count_dict[key] += 1
            new_key = new_value
            new_value = orbit_map[new_key]

# Sum all value in orbit_count_dict
total_num_orbits = 0
for obj in orbit_count_dict:
    total_num_orbits += orbit_count_dict[obj]

print('Total number of orbits: ', total_num_orbits)

# Find the shortest path between 'YOU' and 'SAN'
# Create a list of the tranfers needed from 'YOU' to 'COM'
key = 'YOU'
while obj != 'COM':
    obj = orbit_map[key]
    key = obj
    print('key: ', key)
    print('object: ', obj)