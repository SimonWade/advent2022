import numpy

# Solution for problem: https://adventofcode.com/2022/day/9

def is_touching(head_coords, tail_coords):
    head_x, head_y = head_coords
    tail_x, tail_y = tail_coords

    # If either axis is greater than one space away, they are not touching
    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        return False
    return True

def get_new_position(head_coords, tail_coords):
    head_x, head_y = head_coords
    tail_x, tail_y = tail_coords

    # If head is to the right, move right
    if head_x > tail_x:
        tail_x += 1
    # Else, move left
    elif head_x < tail_x:
        tail_x -= 1

    # If head is above, move up
    if head_y > tail_y:
        tail_y += 1
    # Else, move down
    elif head_y < tail_y:
        tail_y -= 1

    return tail_x, tail_y

def count_positions(commands, knots=2):
    grid = numpy.zeros((300, 300))
    head_x, head_y = 0, 0

    # Create a dictionary of knot coordinates
    coordinates = {}
    for index in range(knots):
        coordinates[index] = (head_x, head_y)

    for command in commands:
        direction, moves = command
        for _ in range(int(moves)):
            for knot in range(knots):
                # Move the head and save coordinates
                if knot == 0:
                    if direction == 'R':
                        head_x += 1
                    elif direction == 'L':
                        head_x -= 1
                    elif direction == 'D':
                        head_y -= 1
                    else:
                        head_y += 1
                    coordinates[knot] = (head_x, head_y)
                else:
                    if not is_touching(coordinates[knot-1], coordinates[knot]):
                        coordinates[knot] = get_new_position(coordinates[knot-1],
                                                             coordinates[knot])
                    # else, knot position is unchanged

                    # Mark the position if it was the final knot
                    if knot == knots-1:
                        grid[coordinates[knot]] = 1
    return numpy.count_nonzero(grid)

def main():
    with open('day_nine.txt', encoding='utf-8') as file:
        commands = [line.strip().split() for line in file.readlines()]

    p1_count = count_positions(commands, knots=2)
    print(f"The Part 1 position count is {p1_count}")

    p2_count = count_positions(commands, knots=10)
    print(f"The Part 2 position count is {p2_count}")

if __name__ == "__main__":
    main()
