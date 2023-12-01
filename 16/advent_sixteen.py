
import collections

# Solution for problem: https://adventofcode.com/2022/day/16

P1_TIME_LIMIT_MINS = 30
P2_TIME_LIMIT_MINS = 26

class ValveNavigator():
    def __init__(self):
        self.non_zero_flows = {}
        self.tunnels = {}
        self.distances = {}
        self.best_path = []     # We use this to remove opened valves for second run
        self.time_limit_mins = 0

    def process_input(self, lines):
        for line in lines:
            # Record valves and non-zero flow rates
            valve = line[0][6:8]
            _, flow_rate = line[0].split("=")

            flow_rate = int(flow_rate)
            if flow_rate > 0:
                self.non_zero_flows[valve] = flow_rate
            # else, ignore non-zero flow rate.

            # Record potential destinations from each valve
            destinations = line[1].split(",")
            dest_list = []
            for idx, val in enumerate(destinations):
                if idx == 0:
                    dest_list.append(val[-2:].strip())
                else:
                    dest_list.append(val.strip())

            self.tunnels[valve] = dest_list

    def record_valve_distances(self):
        for src_valve in self.tunnels:
            self.distances[src_valve] = {}
            for dest_valve in self.tunnels:
                if src_valve != dest_valve:
                    self.distances[src_valve][dest_valve] = self.get_shortest_path(src_valve,
                                                                                   dest_valve)
                # else, same valve so do nothing.

    def get_shortest_path(self, start_pos, end_pos):
        queue = collections.deque()
        queue.append([start_pos])
        visited = set()

        while queue:
            path = queue.popleft()
            valve = path[-1]

            if valve == end_pos:
                return len(path)
            if valve not in visited:
                # Go through list of destinations from valve and add paths to queue
                for neighbour in self.tunnels[valve]:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                visited.add(valve)

    def get_path_details(self, path):
        pressure = 0
        mins_elapsed = 0

        for index, src_valve in enumerate(path):
            if index < len(path) - 1:
                dest_valve = path[index + 1]
                steps = self.distances[src_valve][dest_valve]
                pressure += self.calculate_pressure(steps, mins_elapsed, dest_valve)
                mins_elapsed += steps
            # else, end of path reached so do nothing.

        return pressure, mins_elapsed

    def calculate_pressure(self, steps, mins_elapsed, valve):
        time_remaining = self.time_limit_mins - (steps + mins_elapsed)
        pressure = time_remaining * self.non_zero_flows[valve]
        return pressure

    def get_max_pressure(self, start_valve, time_limit_mins):
        self.time_limit_mins = time_limit_mins

        queue = collections.deque()
        queue.append([start_valve])
        max_pressure = 0

        while queue:
            path = queue.popleft()

            # Get pressure released and minutes elapsed for the path so far
            pressure, mins_elapsed = self.get_path_details(path)

            for valve in self.non_zero_flows:
                if valve not in path:
                    # Get number of steps between last valve in path and new valve
                    steps = self.distances[path[-1]][valve]

                    # Calculate new pressure of path and minutes elapsed
                    new_pressure = pressure + self.calculate_pressure(steps,
                                                                      mins_elapsed,
                                                                      valve)
                    new_mins_elapsed = mins_elapsed + steps

                    if new_mins_elapsed < self.time_limit_mins:
                        new_path = list(path)
                        new_path.append(valve)

                        if new_pressure > max_pressure:
                            # Record this path (apart from start valve) and new max pressure
                            max_pressure = new_pressure
                            self.best_path = new_path[1:]

                        # It's still a viable path so add to queue
                        queue.append(new_path)
                    # else, too much time has elapsed for this path to be viable, so do nothing.

                # else, this valve has already been opened so do nothing.

        return max_pressure

def main():
    with open('day_sixteen.txt', encoding='utf-8') as file:
        lines = [line.strip().split(";") for line in file.readlines()]

    processor = ValveNavigator()
    processor.process_input(lines)
    processor.record_valve_distances()

    # Part 1
    p1_pressure = processor.get_max_pressure(start_valve='AA',
                                             time_limit_mins=P1_TIME_LIMIT_MINS)
    print(f"The Part 1 pressure is {p1_pressure}.")

    # Part 2
    pressure_one = processor.get_max_pressure(start_valve='AA',
                                              time_limit_mins=P2_TIME_LIMIT_MINS)

    # Remove the valves with non-zero flows that we opened in the first run
    for valve in processor.best_path:
        processor.non_zero_flows.pop(valve)

    pressure_two = processor.get_max_pressure(start_valve='AA',
                                              time_limit_mins=P2_TIME_LIMIT_MINS)

    print(f"The Part 2 pressure is {pressure_one + pressure_two}.")

if __name__ == "__main__":
    main()
