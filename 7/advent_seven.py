from pathlib import Path
from collections import defaultdict

# Solution for problem: https://adventofcode.com/2022/day/7

def do_part_one(lines):
    dir_sizes = defaultdict(int)
    file_paths = set()
    current_dir = Path('/')

    for line in lines:
        # If line starts with a number, it's a file size in format [size file_name]
        if line[0].isdigit():
            file_path = current_dir / Path(line[1])
            if file_path not in file_paths:
                file_paths.add(file_path)
                file_size = int(line[0])
                for dir in file_path.parents:
                    dir_sizes[dir] += file_size
        # If line has a 'cd', we've changed directory in format [cd dir]
        elif line[1] == 'cd':
            if line[2] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir / Path(line[2])
        # else, do nothing.

    part_one_total = 0
    for size in dir_sizes.values():
        if size <= 100000:
            part_one_total += size

    print(f"The Part 1 answer is {part_one_total}.")
    return dir_sizes

def do_part_two(dir_sizes):
    total_space_used = max(dir_sizes.values())
    space_available = 70000000 - total_space_used
    space_needed = 30000000 - space_available

    applicable_sizes = []
    for size in dir_sizes.values():
        if size >= space_needed:
            applicable_sizes.append(size)

    smallest_dir_to_delete = min(applicable_sizes)
    print(f"The Part 2 answer is {smallest_dir_to_delete}")

def main():
    with open("day_seven.txt") as file:
        lines = [line.strip().split() for line in file.readlines()]

    dir_sizes = do_part_one(lines)
    do_part_two(dir_sizes)

if __name__ == "__main__":
    main()
