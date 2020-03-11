""" 
Solution to 'Day 4: Secure Container' puzzle from adventofcode.com
https://adventofcode.com/2019/day/4
"""
from collections import defaultdict

# Loop through all the passwords in the range and count how many meet the
# criteria according to part 1 or part 2
def count_passwords(range, criteria):
    pwd = int(range[0])
    num_valid_pwds = 0
    while (pwd < int(range[1])):
        if (is_pwd_valid(str(pwd), criteria)):
            num_valid_pwds += 1
        pwd += 1
    return num_valid_pwds

# Check whether password is valid according to criteria for part 1 or part 2
def is_pwd_valid(pwd, criteria):
    valid = False
    if criteria == 'part1':
        if has_two_adjacent_digits(pwd) and digits_never_decrease(pwd):
            valid = True
    if criteria == 'part2':
        if has_two_adjacent_digits_revised(pwd) and digits_never_decrease(pwd):
            valid = True
    return valid

# Find whether the password has adjacent digits that are equal
def has_two_adjacent_digits(pwd):
    meets_criteria = False
    for index, digit in enumerate(pwd[:-1]):
        if digit == pwd[index+1]:
            meets_criteria = True
            break
    return meets_criteria

# Finds whether the password contains two adjacent digits that aren't part of a
# larger group, e.g. 3 repeated digits would not be a valid password
# If there's at least 1 digit repeated twice, the password is meets the criteria
def has_two_adjacent_digits_revised(pwd):
    meets_criteria = False
    digit_count = defaultdict(lambda: 1)
    # Iterate over the digits and find adjacent pairs that are equal
    for index, digit in enumerate(pwd[:-1]):
        if digit == pwd[index+1]:
            digit_count[digit] += 1
    # If there's at least 1 digit that's repeated twice, this is a valid password
    if any(digit_count[digit] == 2 for digit in digit_count):
        meets_criteria = True
    else: 
        meets_criteria = False 
    return meets_criteria

# Check the digits in the password never decrease
def digits_never_decrease(pwd):
    meets_criteria = True
    for index, digit in enumerate(pwd[:-1]):
        if digit <= pwd[index+1]:
            continue
        else:
            meets_criteria = False
    return meets_criteria

# Read input file
with open('input.txt') as f:
    for line in f:
        # pwd_range = list(map(int, line.strip('\n').split('-')))
        pwd_range = line.strip('\n').split('-')

### Part 1
# Count number of valid passwords in range
num_valid_pwds = count_passwords(pwd_range, 'part1')
print('Number of valid passwords: ', num_valid_pwds)

### Part 2
# Same as before but with new criteria for adjacent equal digits
num_valid_pwds = count_passwords(pwd_range, 'part2')
print('Number of valid passwords: ', num_valid_pwds)
