import copy
import heapq
import math

# Solution for problem: https://adventofcode.com/2022/day/11

class Monkey:
    def __init__(self, index, items):
        self.index = index
        self.items = items
        self.operator = ''
        self.operation_diff = 0
        self.test_divisor = 0
        self.true_dest = 0
        self.false_dest = 0
        self.inspection_count = 0

def create_monkeys(lines):
    monkeys = []
    index = 0

    for line in lines:
        # Items
        if line.startswith("Start"):
            _, items = line.split(":")
            items = [int(item) for item in items.split(",")]

            # Create new monkey and assign unique index so we know
            # where to send items
            monkey = Monkey(index, items)
            index += 1

        # Operation
        elif line.startswith("Operation"):
            _, operator = line.strip().split("=")
            _, symbol, operation_diff = operator.split()
            monkey.operator = symbol

            # If the operation uses 'old' worry level, record it as 0
            monkey.operation_diff = int(operation_diff) if operation_diff.isdigit() else 0

        # Test
        elif line.startswith("Test"):
            _, _, _, test_divisor = line.split()
            monkey.test_divisor = int(test_divisor)

        # True condition
        elif line.startswith("If true"):
            _, _, _, _, _, true_dest = line.split()
            monkey.true_dest = int(true_dest)

        # False condition
        elif line.startswith("If false"):
            _, _, _, _, _, false_dest = line.split()
            monkey.false_dest = int(false_dest)
            monkeys.append(monkey)
        # else, not a line we care about.

    return monkeys

def do_instructions(monkeys, rounds):
    if rounds == 20:
        part_one = True
    else:
        part_one = False
        # Least common multiple required if no relief
        lcm = math.prod([monkey.test_divisor for monkey in monkeys])

    while rounds > 0:
        for monkey in monkeys:
            for item in monkey.items:
                # If operation_diff was recorded as 'old' in text, it uses its own item worry level
                if monkey.operation_diff == 0:
                    operation_diff = item
                else:
                    operation_diff = monkey.operation_diff

                # Do operation
                if monkey.operator == '+':
                    item += operation_diff
                elif monkey.operator == '-':
                    item -= operation_diff
                elif monkey.operator == '*':
                    item *= operation_diff
                else:
                    item /= operation_diff

                # Do test
                if part_one:
                    item = math.floor(item / 3)
                else:
                    item = item % lcm
                if item % monkey.test_divisor == 0:
                    monkeys[monkey.true_dest].items.append(item)
                else:
                    monkeys[monkey.false_dest].items.append(item)

                monkey.inspection_count += 1
            # All monkey's items have been passed so clear list
            monkey.items.clear()  
        rounds -= 1

    # Get two highest counts and multiply together for sum
    inspection_counts = []
    for monkey in monkeys:
        inspection_counts.append(monkey.inspection_count)

    top, second_top = heapq.nlargest(2, inspection_counts)
    return top * second_top

def main():
    with open('day_eleven.txt', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    # Create a copy of monkeys so we don't have to read file twice
    monkeys  = create_monkeys(lines)
    monkeys_copy = copy.deepcopy(monkeys)

    p1_count = do_instructions(monkeys, rounds=20)
    print(f"The Part 1 sum is {p1_count}")

    p2_count = do_instructions(monkeys_copy, rounds=10000)
    print(f"The Part 2 sum is {p2_count}")

if __name__ == "__main__":
    main()
