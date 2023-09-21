import numpy

# Solution for problem: https://adventofcode.com/2022/day/8

def get_column_visibility_and_dist(rows, row_index, col_index, height, check_up=True):
    tree_visible = True
    blocked_distances = []

    for other_row_index, other_row in enumerate(rows):
        if check_up:
            if other_row_index < row_index:
                if other_row[col_index] >= height:
                    blocked_distances.append(row_index - other_row_index)
                    tree_visible = False
        else:
            if other_row_index > row_index:
                if other_row[col_index] >= height:
                    blocked_distances.append(other_row_index - row_index)
                    tree_visible = False

    # Get the minimum distance at which the tree's view was blocked
    if blocked_distances:
        viewing_distance = min(blocked_distances)
    # Otherwise it wasn't blocked so get the max
    elif check_up:
        viewing_distance = row_index
    else:
        viewing_distance = len(rows) - (row_index + 1)

    return tree_visible, viewing_distance

def get_row_visibility_and_dist(row, col_index, height, check_left=True):
    tree_visible = True
    blocked_distances = []

    for other_col_index, other_height in enumerate(row):
        if check_left:
            if other_col_index < col_index and other_height >= height:
                blocked_distances.append(col_index - other_col_index)
                tree_visible = False
        else:
            if other_col_index > col_index and other_height >= height:
                blocked_distances.append(other_col_index - col_index)
                tree_visible = False

    if blocked_distances:
        viewing_distance = min(blocked_distances)
    elif check_left:
        viewing_distance = col_index
    else:
        viewing_distance = len(row) - (col_index + 1)

    return tree_visible, viewing_distance

def main():
    with open('day_eight.txt') as file:
        lines = [line.strip() for line in file.readlines()]

    # Create 2D array of required size and fill
    size = len(lines)
    trees = numpy.zeros((size, size))
    for row_index, row in enumerate(lines):
        for col_index, height in enumerate(row):
            trees[row_index][col_index] = int(height)

    trees_visible = 0
    max_scenic_score = 0
    for row_index, row in enumerate(trees):
        for col_index, height in enumerate(row):
            up_visible, up_viewing_dist = get_column_visibility_and_dist(trees, row_index, col_index, height, check_up=True)
            down_visible, down_viewing_dist = get_column_visibility_and_dist(trees, row_index, col_index, height, check_up=False)
            left_visible, left_viewing_dist = get_row_visibility_and_dist(row, col_index, height, check_left=True)
            right_visible, right_viewing_dist = get_row_visibility_and_dist(row, col_index, height, check_left=False)

            if up_visible or down_visible or left_visible or right_visible:
                trees_visible += 1

            new_scenic_score = up_viewing_dist * left_viewing_dist * down_viewing_dist * right_viewing_dist
            if new_scenic_score > max_scenic_score:
                max_scenic_score = new_scenic_score
    
    print(f"The Part 1 count is: {trees_visible}")
    print(f"The Part 2 score is: {max_scenic_score}")

if __name__ == "__main__":
    main()
