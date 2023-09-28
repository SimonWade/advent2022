
import collections

# Solution for problem: https://adventofcode.com/2022/day/12

class Graph():
    def __init__(self):
        self.graph = []
        self.height = 0
        self.width = 0
        self.start = (0, 0)
        self.end = (0, 0)
        self.a_start_positions = []

    def populate_graph(self, lines):
        self.height = len(lines) - 1
        self.width = len(lines[0]) - 1

        for x_index, line in enumerate(lines):
            row = []
            for y_index, char in enumerate(line):
                #  Start position is an 'a' so record its value as such
                if char == 'S':
                    row.append(ord('a'))
                    self.start = (x_index, y_index)
                    self.a_start_positions.append(self.start)
                # If it's an 'a' and on the edge of graph, record as potential start point
                elif char == 'a':
                    if x_index in [0, self.height] or y_index in [0, self.width]:
                        self.a_start_positions.append((x_index, y_index))
                    row.append(ord(char))
                # Replace end position with the next decimal value after z (curly bracket)
                elif char == 'E':
                    row.append(ord('{'))
                    self.end = (x_index, y_index)
                else:
                    row.append(ord(char))
            self.graph.append(row)

    def get_adjacent_coords(self, coords):
        x_index, y_index = coords
        current_val = self.graph[x_index][y_index]

        # Check value of adjacent positions is <= the current value + 1
        # and add to list if so.
        adjacent_coords = []
        if x_index > 0 and self.graph[x_index - 1][y_index] <= (current_val + 1):
            adjacent_coords.append((x_index - 1, y_index))

        if y_index < self.width and self.graph[x_index][y_index + 1] <= (current_val + 1):
            adjacent_coords.append((x_index, y_index + 1))

        if x_index < self.height and self.graph[x_index + 1][y_index] <= (current_val + 1):
            adjacent_coords.append((x_index + 1, y_index))

        if y_index > 0 and self.graph[x_index][y_index - 1] <= (current_val + 1):
            adjacent_coords.append((x_index, y_index - 1))

        return adjacent_coords

    def breadth_first_search(self, start_pos):
        queue = collections.deque()
        queue.append([start_pos])
        visited = set()

        while queue:
            # Remove element from left side of deque
            path = queue.popleft()

            # Get last coordinate from path
            node = path[-1]

            if node == self.end:
                # Return number of steps so do not include start and end positions
                return path[1:-1]
            if node not in visited:
                # If adjacent coordinates contain valid values, add new paths to queue
                for neighbour in self.get_adjacent_coords(node):
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                visited.add(node)

def main():
    with open('day_twelve.txt', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    graph = Graph()
    graph.populate_graph(lines)
    path = graph.breadth_first_search(graph.start)
    print(f"The steps taken for Part 1 is: {len(path) - 1}")

    steps_taken_list = []
    for start_pos in graph.a_start_positions:
        path = graph.breadth_first_search(start_pos)
        if path is not None:
            steps_taken_list.append(len(path) - 1)
    print(f"The minimum potential steps for Part 2 is {min(steps_taken_list)}")

if __name__ == "__main__":
    main()
