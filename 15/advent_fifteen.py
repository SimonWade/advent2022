
# Solution for problem: https://adventofcode.com/2022/day/15

SENSOR_COORD_START_POS = 10
BEACON_COORD_START_POS = 21

X_POS_INDEX = 0
Y_POS_INDEX = 1

TARGET_ROW = 2000000        # For Part 1
SEARCH_BOUNDARY = 4000000   # For Part 2 - applies to x and y axes

def get_manhattan_distance(one_x, one_y, two_x, two_y):
    return abs(one_x - two_x) + abs(one_y - two_y)

class Sensor():
    def __init__(self, sensor_x, sensor_y, nearest_beacon_x, nearest_beacon_y):
        self.sensor_x = sensor_x
        self.sensor_y = sensor_y
        self.manhattan_distance = get_manhattan_distance(sensor_x, sensor_y,
                                                         nearest_beacon_x, nearest_beacon_y)

        # Calculate borders of sensor boundaries
        self.left_boundary = (sensor_x - self.manhattan_distance, sensor_y)
        self.top_boundary = (sensor_x, sensor_y - self.manhattan_distance)
        self.right_boundary = (sensor_x + self.manhattan_distance, sensor_y)
        self.bottom_boundary = (sensor_x, sensor_y + self.manhattan_distance)

class BeaconLocator():
    def __init__(self):
        self.sensors = []
        self.filled_positions = set()

    def get_position(self, strings):
        _, x_pos = strings[0].split("=")
        _, y_pos = strings[1].split("=")
        return int(x_pos), int(y_pos)

    def process_input(self, lines):
        for line in lines:
            # Sensors
            sensor_strings = line[0][SENSOR_COORD_START_POS:].split(",")
            sensor_x, sensor_y = self.get_position(sensor_strings)

            # Beacons
            beacon_strings = line[1][BEACON_COORD_START_POS:].split(",")
            beacon_x, beacon_y = self.get_position(beacon_strings)

            # Record positions we know are filled
            self.filled_positions.add((sensor_x, sensor_y))
            self.filled_positions.add((beacon_x, beacon_y))

            sensor = Sensor(sensor_x, sensor_y, beacon_x, beacon_y)
            self.sensors.append(sensor)

    def record_boundary_positions(self, y_pos=TARGET_ROW):
        boundary_positions = set()
        for sensor in self.sensors:
            # If y pos is between the top and bottom boundaries of sensor, record the position.
            if y_pos >= sensor.top_boundary[Y_POS_INDEX] and y_pos <= sensor.bottom_boundary[Y_POS_INDEX]:
                distance_to_sensor = abs(sensor.sensor_y - y_pos)
                positions = sensor.manhattan_distance - distance_to_sensor
                # This goes from left to right on line
                for pos in range(-positions, positions + 1):
                    boundary_positions.add((sensor.sensor_x - pos, y_pos))

        return boundary_positions

    def is_position_empty(self, x_pos, y_pos):
        for sensor in self.sensors:
            # If distance between positions is <= to manhattan distance, it cannot be empty
            if get_manhattan_distance(x_pos, y_pos, sensor.sensor_x, sensor.sensor_y) <= sensor.manhattan_distance:
                return False
        return True

    def find_distress_beacon(self, search_boundary=SEARCH_BOUNDARY):
        for sensor in self.sensors:
            # One space above the top of sensor boundary
            top_y = sensor.top_boundary[Y_POS_INDEX] - 1
            if top_y >= 0:
                if self.is_position_empty(sensor.sensor_x, top_y):
                    print(f"Empty position found at ({sensor.sensor_x},{top_y})")
                    return (sensor.sensor_x, top_y)

            # One space below the bottom boundary
            bottom_y = sensor.bottom_boundary[Y_POS_INDEX] + 1
            if bottom_y <= search_boundary:
                if self.is_position_empty(sensor.sensor_x, bottom_y):
                    print(f"Empty position found at ({sensor.sensor_x},{bottom_y})")
                    return (sensor.sensor_x, bottom_y)

            # Only search rows within specified parameters
            min_row = max(0, sensor.top_boundary[Y_POS_INDEX])
            max_row = min(search_boundary, sensor.bottom_boundary[Y_POS_INDEX])

            for y_pos in range(min_row, max_row):
                distance = abs(y_pos - sensor.sensor_y)
                left_x = abs(sensor.left_boundary[X_POS_INDEX] + distance) - 1
                right_x = abs(sensor.right_boundary[X_POS_INDEX] - distance) + 1

                # Search left
                if left_x <= search_boundary:
                    if self.is_position_empty(left_x, y_pos):
                        print(f"Empty position found at ({left_x},{y_pos})")
                        return (left_x, y_pos)

                # Search right
                if right_x <= search_boundary:
                    if self.is_position_empty(right_x, y_pos):
                        print(f"Empty position found at ({right_x},{y_pos})")
                        return (right_x, y_pos)

def main():
    with open('day_fifteen.txt', encoding='utf-8') as file:
        lines = [line.strip().split(":") for line in file.readlines()]

    beacon_locator = BeaconLocator()
    beacon_locator.process_input(lines)

    # Subtract the filled positions we know of from boundary positions before counting
    boundary_positions = beacon_locator.record_boundary_positions(TARGET_ROW)
    print(f"Part 1 count: {len(boundary_positions - beacon_locator.filled_positions)}")

    # Multiply x by search boundary and add y to calculate tuning frequency
    x_pos, y_pos = beacon_locator.find_distress_beacon(SEARCH_BOUNDARY)
    print(f"Part 2 tuning frequency: {(x_pos * SEARCH_BOUNDARY) + y_pos}")

if __name__ == "__main__":
    main()
