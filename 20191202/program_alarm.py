""" Solution to Day 2: 1202 Program Alarm from adventofcode.com """

def run_program(program):
    
    # Initialize pointers
    instr_pointer = 0
    
    # Execute program while opcode is not
    while program[instr_pointer] != 99:
        operand1_pointer = instr_pointer + 1
        operand2_pointer = instr_pointer + 2
        result_pointer = instr_pointer + 3
        
        # Parse opcode and perform operation (add/multiply)
        if program[instr_pointer] == 1:
            result = program[program[operand1_pointer]] + program[program[operand2_pointer]]
        elif program[instr_pointer] == 2:
            result = program[program[operand1_pointer]] * program[program[operand2_pointer]]
        else:
            result = None
            print('[ERROR] Invalid opcode. Terminating program.')
            break

        # Store the result according to the result pointer
        program[program[result_pointer]] = result
        
        # Update pointers (increment by 4)
        instr_pointer += 4
    return

# Read input file
with open('20191202/input.txt') as f:
    for line in f:
        program = list(map(int, line.strip('\n').split(',')))

# Modify input positions 1 and 2
program[1] = 12
program[2] = 2

# Execute program
run_program(program)

# Part 1: 
print('Part 1 Answer')
print('First position: ', program[0])

# Part 2:
# Modify operand1 and operand2
program[1] = 89
program[2] = 76
part2_result = 100 * program[1] + program[2]
print('\nPart 2 Answer: ', part2_result)