""" Solution to Day 1 Puzzle from adventofcode.com """
import numpy as np

# Function to calculate the fuel required for a module given its mass
def calculate_fuel(mass):
    return (mass // 3) - 2

def calculate_fuel_for_fuel(fuel):
    total_fuel_for_fuel = 0
    while (fuel > 0):
        fuel_for_fuel = calculate_fuel(fuel)
        if (fuel_for_fuel < 0):
            fuel_for_fuel = 0
        total_fuel_for_fuel += fuel_for_fuel
        fuel = fuel_for_fuel
    return total_fuel_for_fuel

# Read input file and calculate the fuel required for each module
# Expect the mass for each module to be in a separate line
fuel = []
with open('20191201/input.txt') as f:
    for line in f:
        fuel.append(calculate_fuel(int(line)))

# Part 1: Calculate total amount of fuel
total_amount_fuel = np.sum(fuel)
print('Total fuel requirement: ', total_amount_fuel)

# Part 2: Same as 1, but include the fuel needed for the fuel
total_fuel_for_fuel = []
for fuel_amount in fuel:
    total_fuel_for_fuel.append(calculate_fuel_for_fuel(fuel_amount))

total_amount_fuel_for_fuel = np.sum(total_fuel_for_fuel)
print('Total fuel requirement, including fuel for fuel: ', total_amount_fuel + total_amount_fuel_for_fuel)