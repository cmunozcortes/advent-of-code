""" Solution to Day 6: Universal Orbit Map from adventofcode.com """

# Read input file and parse objects into list
objs = []
with open('20191206/small.txt') as f:
    for line in f:
        objs.append(line.strip('\n').split(')'))
    print(objs)