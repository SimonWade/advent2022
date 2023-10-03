
import numpy

def plot_rocks(graph, paths, offset):
    for path in paths:
        for index in range(0, len(path) - 1):
            # Rock is marked on graph as 1
            x, y = path[index]
            x -= offset
            graph[x][y] = 1

            next_x, next_y = path[index + 1]
            next_x -= offset

            # Keep plotting rocks while destination is not reached
            while (x, y) != (next_x, next_y):
                if y < next_y:
                    y += 1
                if y > next_y:
                    y -= 1
                if x < next_x:
                    x += 1
                if x > next_x:
                    x -= 1
                graph[x][y] = 1

def plot_sand(graph, x, y, height):
    resting = False
    in_void = False

    while not resting and not in_void:
        # Check whether the tile below is blocked
        if graph[x][y + 1] != 0:

            # Check whether the tile down to the left is blocked
            if graph[x - 1][y + 1] != 0:

                # Check whether the tile down to the right is blocked
                if graph[x + 1][y + 1] != 0:
                    resting = True
                # If not, sand can rest here
                else:
                    x += 1
                    y += 1
            else:
                x -= 1
                y += 1
        else:
            y += 1

        # Sand has fallen below lowest rocks
        if y >= height:
            in_void = True

    graph[x][y] = 2

    return resting, in_void

def main():
    with open('day_fourteen.txt', encoding='utf-8') as file:
        paths = [line.strip().split(" -> ") for line in file.readlines()]

    # Need to find min and max values to determine size of array and where void begins
    min_x = 500
    max_x = 0
    max_y = 0

    line_paths = []
    for path in paths:
        line_path = []
        for coord in path:
            x, y = coord.split(",")
            x, y = int(x), int(y)

            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            line_path.append((x, y))
        line_paths.append(line_path)

    width = max_x - min_x
    height = max_y

    graph = numpy.zeros((width + 1, height + 1))

    # Min x is used as an offset as the x values begin in high 400s - start from 0 instead
    plot_rocks(graph, line_paths, min_x)

    sand_count = 0
    in_void = False
    while not in_void:
        # Sand always starts at coordinates 500,0
        resting, in_void = plot_sand(graph, 500 - min_x, 0, height)

        if resting:
            sand_count += 1

    print(f"The Part 1 count is {sand_count}")

if __name__ == "__main__":
    main()
