
priorities_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,
                   'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16,
                   'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24,
                   'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32,
                   'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40,
                   'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48,
                   'W':49, 'X':50, 'Y':51, 'Z':52}

def get_match(input_one, input_two, input_three=None):
    for i in input_one:
        for j in input_two:
            if input_three is not None:
                for k in input_three:
                    if i == j == k:
                        return i
            else:
                if i == j:
                    return i

def get_part_one_priority(line):
    length = int(len(line) / 2)
    comp_one = line[0:length]
    comp_two = line[length:]

    item = get_match(comp_one, comp_two)
    return priorities_dict[item]

def get_part_two_priority(group):
    return priorities_dict[get_match(group[0], group[1], group[2])]

def main():
    with open('day_three.txt') as f:
        part_one_priority = 0
        part_two_priority =0
        group = []
        for index, line in enumerate(f, start=1):
            line = line.strip()
            part_one_priority += get_part_one_priority(line)

            group.append(line)
            if index % 3 == 0:
                part_two_priority += get_part_two_priority(group)
                group.clear()

    print(f"The total is {part_one_priority}")
    print(f"The badge total is {part_two_priority}")

if __name__ == '__main__':
        main()
