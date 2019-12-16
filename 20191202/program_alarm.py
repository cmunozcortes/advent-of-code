""" Solution to Day 2: 1202 Program Alarm from adventofcode.com """

def run_program(program):
    
    # Initialize pointers
    opcode_index = 0
    operand1_index = 1
    operand2_index = 2
    result_index = 3
    
    # Execute program while opcode is not
    while program[opcode_index] != 99:
        if program[opcode_index] == 1:
            result = program[program[operand1_index]] + program[program[operand2_index]]
        elif program[opcode_index] == 2:
            result = program[program[operand1_index]] * program[program[operand2_index]]
        else:
            result = None
            print('[ERROR] Invalid opcode. Terminating program.')
            break
        program[program[result_index]] = result
        
        # Update pointers (increment by 4)
        opcode_index += 4
        operand1_index += 4
        operand2_index += 4
        result_index += 4

    print('Halting program execution...')
    return

# Read input file
with open('20191202/input_part1.txt') as f:
    for line in f:
        program = list(map(int, line.strip('\n').split(',')))

# Execute program
run_program(program)

# Part 1: 
print('First position: ', program[0])
print('Done.')

# Part 2: