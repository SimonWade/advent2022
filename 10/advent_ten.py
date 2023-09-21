
# Solution for problem: https://adventofcode.com/2022/day/10

NOOP_CYCLES = 1
ADDX_CYCLES = 2

def create_queue(commands):
    queue = []
    total_cycles = 0

    for cmd in commands:
        # addx command
        if len(cmd) > 1:
            _, value = cmd
            total_cycles += ADDX_CYCLES
            queue.append((int(value), ADDX_CYCLES))
        # noop command
        else:
            total_cycles += NOOP_CYCLES
            queue.append((0, NOOP_CYCLES))

    return queue, total_cycles

def process_commands(queue, total_cycles):
    strength_sum = 0
    register_value = 1

    queue_index = 0
    char_index = 0

    with open('part_two.txt', 'w', encoding='utf-8') as file:
        for cycle in range(1, total_cycles + 1):
            # Update strength sum if it's a relevant cycle
            if (cycle + 20) % 40 == 0:
                strength_sum += (cycle * register_value)

            # Draw sprite if it's a position match
            if char_index in [register_value - 1, register_value, register_value + 1]:
                file.write("#")
            else:
                file.write(".")

            # Update the char index and move to new line if necessary
            if cycle % 40 == 0:
                file.write("\n")
                char_index = 0
            else:
                char_index += 1

            # Update remaining cycles for existing commands
            value, cycles = queue[queue_index]
            if cycles > 0:
                cycles -= 1
            queue[queue_index] = ((value, cycles))

            # If instruction has finished, move to next queue item and update register
            if cycles == 0:
                queue_index += 1
                register_value += value

    print(f"The Part 1 sum is {strength_sum}")
    print(f"Part 2 is written to '{file.name}'")

def main():
    with open('day_ten.txt', encoding='utf-8') as file:
        commands = [line.strip().split() for line in file.readlines()]

    queue, total_cycles = create_queue(commands)
    process_commands(queue, total_cycles)

if __name__ == "__main__":
    main()
