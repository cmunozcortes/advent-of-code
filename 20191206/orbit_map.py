""" Solution to Day 6: Universal Orbit Map from adventofcode.com """
from collections import defaultdict

# Function to find the path from any given object to 'COM'
def find_path_to_com(dict, key, path):
    # Find the complete path from 'YOU' to 'COM'
    obj = dict[key]
    while obj != 'COM':
        path.append(obj)
        key = obj               # update key
        obj = dict[key]    # update object
    return path 

# Main function implementing solutions to part 1 and part 2 of puzzle
def main():
    # Read input file and parse objects into a dictionary
    orbit_map = {}
    with open('20191206/input.txt') as f:
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
    print('Part 1 Answer:\n')
    print('Total number of orbits: ', total_num_orbits)
    
    # Find the shortest path between 'YOU' and 'SAN'
    # Create a list of the tranfers needed from 'YOU' to 'COM'
    key = 'YOU'
    you_to_com_path = []
    you_to_com_path =  find_path_to_com(orbit_map, key, you_to_com_path) 

    # Create a list of the transfers needed from 'SAN' to 'COM'
    key = 'SAN'
    san_to_com_path = []
    san_to_com_path = find_path_to_com(orbit_map, key, san_to_com_path)

    # Loop through objects in one of the list and if it exists in the other list we have a 'common' node
    # Min number of transfers will be the index of the common node/obj in list1 plus the index of the node in list2
    for obj in you_to_com_path:
        if obj in san_to_com_path:
            num_transfers = you_to_com_path.index(obj) + san_to_com_path.index(obj)
            break
    print('Part 2 Answer:\n')
    print('Number of transfers: ', num_transfers)

# Main
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()