
import ast
import copy

# Solution for problem: https://adventofcode.com/2022/day/13

def is_list_order_correct(left, right):
    is_correct_order = None

    # Make copies of left and right lists so we don't edit originals
    left_copy = copy.copy(left)
    right_copy = copy.copy(right)

    # While one of the lists still has items...
    while left_copy or right_copy:
        if not left_copy:
            # Left side has ran out of items so order is correct
            return True
        if not right_copy:
            # Right side has ran out of items so order is incorrect
            return False

        # Pop the first item and check they are lists
        left_val = left_copy.pop(0)
        right_val = right_copy.pop(0)

        left_is_list = isinstance(left_val, list)
        right_is_list = isinstance(right_val, list)

        # Convert to list if only one is of type list
        if left_is_list and right_is_list:
            is_correct_order = is_list_order_correct(left_val, right_val)
        elif left_is_list:
            is_correct_order = is_list_order_correct(left_val, [right_val])
        elif right_is_list:
            is_correct_order = is_list_order_correct([left_val], right_val)
        else:
            if left_val < right_val:
                # Left integer is smaller than right integer so order is correct
                return True
            if right_val < left_val:
                # Right integer is smaller than left integer so order is incorrect
                return False

        # Only return value when order is determined
        if is_correct_order is not None:
            return is_correct_order
        # else, continue to work through packet

def do_part_one(lefts, rights):
    indices_sum = 0
    packets = []
    for index, left in enumerate(lefts):
        if is_list_order_correct(left, rights[index]):
            # Pairs start at 1 so always one greater than index
            indices_sum += (index + 1)
        packets.append(left)
        packets.append(rights[index])

    print(f"The sum for Part 1 is {indices_sum}")
    return packets

def do_part_two(packets):
    for right_index, right_packet in enumerate(packets):
        # Make copies of left and right items as we pop items from the lists
        right_copy = copy.copy(right_packet)
        for left_index, left_packet in enumerate(packets):
            left_copy = copy.copy(left_packet)
            if right_index != left_index:
                if not is_list_order_correct(left_copy, right_copy):
                    packets[left_index] = right_copy
                    packets[right_index] = left_copy

                    left_copy = packets[left_index]
                    right_copy = packets[right_index]

    for index, packet in enumerate(packets):
        # Pairs start at one so always one greater than index
        if packet == [2]:
            first_index = index + 1
        elif packet == [6]:
            second_index = index + 1

    print(f"The sum for Part 2 is {first_index * second_index}")

def main():
    with open('day_thirteen.txt', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    lefts = []
    rights = []
    index = 0
    for line in lines:
        if line:
            if index == 0 or index % 2 == 0:
                lefts.append(ast.literal_eval(line))
            else:
                rights.append(ast.literal_eval(line))
            index += 1

    packets = do_part_one(lefts, rights)

    # Add the divider packets for Part 2
    packets.append([2])
    packets.append([6])

    do_part_two(packets)

if __name__ == "__main__":
    main()
