# Solution for problem: https://adventofcode.com/2022/day/5

import copy

# Each crate is four spaces apart
STACK_SEPARATOR = 4
FIRST_STACK_INDEX = 1
SECOND_STACK_INDEX = FIRST_STACK_INDEX + STACK_SEPARATOR
THIRD_STACK_INDEX = SECOND_STACK_INDEX + STACK_SEPARATOR
FOURTH_STACK_INDEX = THIRD_STACK_INDEX + STACK_SEPARATOR
FIFTH_STACK_INDEX = FOURTH_STACK_INDEX + STACK_SEPARATOR
SIXTH_STACK_INDEX = FIFTH_STACK_INDEX + STACK_SEPARATOR
SEVENTH_STACK_INDEX = SIXTH_STACK_INDEX + STACK_SEPARATOR
EIGHTH_STACK_INDEX = SEVENTH_STACK_INDEX + STACK_SEPARATOR
NINTH_STACK_INDEX = EIGHTH_STACK_INDEX + STACK_SEPARATOR

instructions = []

def read_and_process_file():
    stack_one = []
    stack_two = []
    stack_three = []
    stack_four = []
    stack_five = []
    stack_six = []
    stack_seven = []
    stack_eight = []
    stack_nine = []

    with open('day_five.txt') as file:
        for line in file:
            # Stacks in file
            if line.startswith("["):
                if line[FIRST_STACK_INDEX] != " ":
                    stack_one.append(line[FIRST_STACK_INDEX])
                if line[SECOND_STACK_INDEX] != " ":
                    stack_two.append(line[SECOND_STACK_INDEX])
                if line[THIRD_STACK_INDEX] != " ":
                    stack_three.append(line[THIRD_STACK_INDEX])
                if line[FOURTH_STACK_INDEX] != " ":
                    stack_four.append(line[FOURTH_STACK_INDEX])
                if line[FIFTH_STACK_INDEX] != " ":
                    stack_five.append(line[FIFTH_STACK_INDEX])
                if line[SIXTH_STACK_INDEX] != " ":
                    stack_six.append(line[SIXTH_STACK_INDEX])
                if line[SEVENTH_STACK_INDEX] != " ":
                    stack_seven.append(line[SEVENTH_STACK_INDEX])
                if line[EIGHTH_STACK_INDEX] != " ":
                    stack_eight.append(line[EIGHTH_STACK_INDEX])
                if line[NINTH_STACK_INDEX] != " ":
                    stack_nine.append(line[NINTH_STACK_INDEX])
            # Instructions in file
            elif line.startswith("move"):
                _, crates_to_move, _, source_stack, _, dest_stack = line.strip().split(" ")
                instructions.append([int(crates_to_move), int(source_stack), int(dest_stack)])
            # else, do nothing.

    return [stack_one, stack_two, stack_three, stack_four, 
            stack_five, stack_six, stack_seven, stack_eight, stack_nine]

def execute_p1_instructions(stacks):
    for instruction in instructions:
        crates_to_move, source_stack, dest_stack = instruction
        for _ in range(0, crates_to_move):
            # Remove crate from top of source stack
            crate = stacks[source_stack-1].pop()
            # Add crate to top of destination stack
            stacks[dest_stack-1].append(crate)
    return stacks

def execute_p2_instructions(stacks):
    for instruction in instructions:
        crates_to_move, source_stack, dest_stack = instruction
        crates = []

        for _ in range(0, crates_to_move):
            # Remove crate from top of source stack
            crate = stacks[source_stack-1].pop()
            crates.append(crate)
        # Crates should be sorted as they were so reverse and append
        crates.reverse()
        for crate in crates:
            stacks[dest_stack-1].append(crate)
    return stacks

def main():
    stacks = read_and_process_file()
    # Stacks are read from top to bottom so reverse
    for stack in stacks:
        stack.reverse()

    # Make a copy for Part 2 to avoid re-reading file
    stacks_copy = copy.deepcopy(stacks)

    # Part 1
    part_1_stacks = execute_p1_instructions(stacks)
    print("The stacks are sorted as follows for Part 1:")
    for stack in part_1_stacks:
        print(stack)

    # Part 2
    part_2_stacks = execute_p2_instructions(stacks_copy)
    print("The stacks are sorted as follows for Part 2:")
    for stack in part_2_stacks:
        print(stack)

if __name__ == '__main__':
    main()
