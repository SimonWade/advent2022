
import numpy

#  Minus rock:
#  ####
MINUS_ROCK_WIDTH = 4
MINUS_ROCK_HEIGHT = 1

#  Plus rock:
#   #
#  ###
#   #
PLUS_ROCK_WIDTH = 3
PLUS_ROCK_HEIGHT = 3

#  L rock:
#    #
#    #
#  ###
L_ROCK_WIDTH = 3
L_ROCK_HEIGHT = 3

#  I rock:
#  #
#  #
#  #
#  #
I_ROCK_WIDTH = 1
I_ROCK_HEIGHT = 4

#  Square rock:
#  ##
#  ##
SQUARE_ROCK_WIDTH = 2
SQUARE_ROCK_HEIGHT = SQUARE_ROCK_WIDTH

class RockType:
    MINUS = 0
    PLUS = 1
    L = 2
    I = 3
    SQUARE = 4

class RockMap():
    def __init__(self, instructions):
        # Jet instructions and index for cycling through them
        self.instructions = instructions
        self.index = 0

        # Grid is always 7 wide, height doesn't matter as long as it's big enough
        self.height = 5000
        self.width = 7
        self.map = numpy.zeros((self.height, self.width))

        self.rock_y_peak = self.height - 1

    def can_move_right(self, rock_type, x, y):
        # Rock can only move right if it's not going to hit the border and there is space for shape
        if rock_type == RockType.MINUS:
            if (x + MINUS_ROCK_WIDTH) < self.width:
                if self.map[y][x + MINUS_ROCK_WIDTH] == 0:
                    return True

        elif rock_type == RockType.PLUS:
            if (x + PLUS_ROCK_WIDTH) < self.width:
                if self.map[y][x + 2] == 0 and self.map[y - 1][x + 3] == 0:
                    return True

        elif rock_type == RockType.L:
            if (x + L_ROCK_WIDTH) < self.width:
                if self.map[y][x + 3] == 0 and self.map[y - 1][x + 3] == 0:
                    return True

        elif rock_type == RockType.I:
            if (x + I_ROCK_WIDTH) < self.width:
                if self.map[y][x + 1] == 0 and self.map[y - 1][x + 1] == 0 and \
                        self.map[y - 2][x + 1] == 0 and self.map[y - 3][x + 1] == 0:
                    return True

        else:
            if (x + SQUARE_ROCK_WIDTH) < self.width:
                if self.map[y][x + 2] == 0 and self.map[y - 1][x + 2] == 0:
                    return True

        return False

    def can_move_left(self, rock_type, x, y):
        # Rock can only move left if it's not going to hit the border and there is space for shape
        if x > 0:
            if rock_type == RockType.MINUS:
                if self.map[y][x - 1] == 0:
                    return True

            elif rock_type == RockType.PLUS:
                if self.map[y][x] == 0 and self.map[y - 1][x - 1] == 0:
                    return True

            elif rock_type == RockType.L:
                if self.map[y][x - 1] == 0:
                    return True

            elif rock_type == RockType.I:
                if self.map[y][x - 1] == 0 and self.map[y - 1][x - 1] == 0 and \
                        self.map[y - 2][x - 1] == 0 and self.map[y - 3][x - 1] == 0:
                    return True
            else:
                if self.map[y][x - 1] == 0 and self.map[y - 1][x - 1] == 0:
                    return True

        return False

    def can_move_down(self, rock_type, x, y):
        # Rock can only move down if the spaces the shape will move to are not filled
        if rock_type == RockType.MINUS:
            if self.map[y + 1][x] == 0 and self.map[y + 1][x + 1] == 0 and \
                    self.map[y + 1][x + 2] == 0 and self.map[y + 1][x + 3] == 0:
                return True

        elif rock_type == RockType.PLUS:
            if self.map[y][x] == 0 and self.map[y][x + 2] == 0 and self.map[y + 1][x + 1] == 0:
                return True

        elif rock_type == RockType.L:
            if self.map[y + 1][x] == 0 and self.map[y + 1][x + 1] == 0 and \
                    self.map[y + 1][x + 2] == 0:
                return True

        elif rock_type == RockType.I:
            if self.map[y + 1][x] == 0:
                return True
        else:
            if self.map[y + 1][x] == 0 and self.map[y + 1][x + 1] == 0:
                return True

        return False

    def draw_rock(self, rock_type, x, y):
        # X and y are the bottom left of the shape / area it is in
        if rock_type == RockType.MINUS:
            self.map[y][x] = 1
            self.map[y][x + 1] = 1
            self.map[y][x + 2] = 1
            self.map[y][x + 3] = 1

        elif rock_type == RockType.PLUS:
            self.map[y - 2][x + 1] = 1
            self.map[y - 1][x] = 1
            self.map[y - 1][x + 1] = 1
            self.map[y - 1][x + 2] = 1
            self.map[y][x + 1] = 1

        elif rock_type == RockType.L:
            self.map[y][x] = 1
            self.map[y][x + 1] = 1
            self.map[y][x + 2] = 1
            self.map[y - 1][x + 2] = 1
            self.map[y - 2][x + 2] = 1

        elif rock_type == RockType.I:
            self.map[y][x] = 1
            self.map[y - 1][x] = 1
            self.map[y - 2][x] = 1
            self.map[y - 3][x] = 1

        else:
            self.map[y - 1][x] = 1
            self.map[y - 1][x + 1] = 1
            self.map[y][x] = 1
            self.map[y][x + 1] = 1

    def get_rock_peak(self, rock_type, y):
        # Get new rock peak depending on which rock just landed
        if rock_type == RockType.MINUS:
            height = MINUS_ROCK_HEIGHT - 1
        elif rock_type == RockType.PLUS:
            height = PLUS_ROCK_HEIGHT - 1
        elif rock_type == RockType.L:
            height = L_ROCK_HEIGHT - 1
        elif rock_type == RockType.I:
            height = I_ROCK_HEIGHT - 1
        else:
            height = SQUARE_ROCK_HEIGHT - 1

        if (y - height) < self.rock_y_peak:
            return y - height

        return self.rock_y_peak

    def get_resting_position(self, rock_type):
        # Rock starts three spaces above highest rock or floor
        y = self.rock_y_peak - 4

        # Each rock appears with left edge two spaces away from left wall
        x = 2

        while y < self.height - 1:

            if self.instructions[self.index] == '>':
                if self.can_move_right(rock_type, x, y):
                    x += 1
            else:
                if self.can_move_left(rock_type, x, y):
                    x -= 1

            if self.index < len(self.instructions) - 1:
                self.index += 1
            else:
                self.index = 0

            # Try down
            if self.can_move_down(rock_type, x, y):
                y += 1
            else:
                break

        # Get new highest y position and draw rock
        self.rock_y_peak = self.get_rock_peak(rock_type, y)

        self.draw_rock(rock_type, x, y)

    def do_rock_fall(self):
        fallen_rocks = 0
        rock_type = RockType.MINUS

        while fallen_rocks < 2022:
            self.get_resting_position(rock_type)

            # Rocks fall in a loop, starting with minus and ending with square
            if rock_type == RockType.SQUARE:
                rock_type = RockType.MINUS
            else:
                rock_type += 1

            fallen_rocks += 1

        return self.height - self.rock_y_peak

def main():
    with open('day_seventeen.txt', encoding='utf-8') as file:
        patterns = list(file.readline())

    rock_map = RockMap(patterns)
    part_one_peak = rock_map.do_rock_fall()
    print(f"The Part 1 answer is {part_one_peak}.")

if __name__ == "__main__":
    main()
