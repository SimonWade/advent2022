# Solution for problem: https://adventofcode.com/2022/day/6

def find_first_marker(lines, marker_len):
    for line in lines:
        for index, _ in enumerate(line):
            chars = line[index:index+marker_len]
            # Set removes duplicates
            if len(set(chars)) == marker_len:
                print(f"The first unique chars are {chars} and {index + marker_len} chars appeared before it.")
                break

def main():
    with open("day_six.txt") as file:
        lines = file.readlines()

    print("Part 1:")
    find_first_marker(lines, marker_len=4)

    print("Part 2:")
    find_first_marker(lines, marker_len=14)

if __name__ == "__main__":
        main()
