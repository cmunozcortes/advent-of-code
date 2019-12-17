""" 
Solution to 'Day 4: Secure Container' puzzle from adventofcode.com
https://adventofcode.com/2019/day/4
"""
def count_passwords(range):
    pwd = int(range[0])
    num_valid_pwds = 0
    while (pwd < int(range[1])):
        if (is_pwd_valid(str(pwd))):
            num_valid_pwds += 1
        pwd += 1
    return num_valid_pwds

def is_pwd_valid(pwd):
    valid = False
    if has_two_adjacent_digits(pwd) and digits_never_decrease(pwd):
        valid = True
    return valid

def has_two_adjacent_digits(pwd):
    meets_criteria = False
    for index, digit in enumerate(pwd[:-1]):
        if digit == pwd[index+1]:
            meets_criteria = True
            break
    return meets_criteria

def digits_never_decrease(pwd):
    meets_criteria = True
    for index, digit in enumerate(pwd[:-1]):
        if digit <= pwd[index+1]:
            continue
        else:
            meets_criteria = False
    return meets_criteria

# Read input file
with open('20191204/input.txt') as f:
    for line in f:
        # pwd_range = list(map(int, line.strip('\n').split('-')))
        pwd_range = line.strip('\n').split('-')

### Part 1
# Count number of valid passwords in range
num_valid_pwds = count_passwords(pwd_range)
print('Number of valid passwords: ', num_valid_pwds)