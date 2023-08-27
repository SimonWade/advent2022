
def get_ranges(range):
    range_start, range_end = range.split("-")
    return int(range_start), int(range_end)

def do_p1_comparison(range_one, range_two):
    range_one_start, range_one_end = get_ranges(range_one)
    range_two_start, range_two_end = get_ranges(range_two)

    if range_one_start <= range_two_start and range_one_end >= range_two_end:
        return True
    elif range_two_start <= range_one_start and range_two_end >= range_one_end:
        return True
    else:
        return False

def do_p2_comparison(range_one, range_two):
    range_one_start, range_one_end = get_ranges(range_one)
    range_two_start, range_two_end = get_ranges(range_two)

    if range_one_start <= range_two_start and range_one_end >= range_two_start:
        return True
    elif range_two_start <= range_one_start and range_two_end >= range_one_start:
        return True
    else:
        return False

def main():
    with open('day_four.txt') as f:
        part_one_total = 0
        part_two_total = 0
        for line in f:
            range_one, range_two = line.strip().split(",")
            if do_p1_comparison(range_one, range_two):
                part_one_total += 1
            if do_p2_comparison(range_one, range_two):
                part_two_total += 1

    print(f"The part one total is {part_one_total}")
    print(f"The part two total is {part_two_total}")

if __name__ == '__main__':
        main()
