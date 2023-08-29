# Solution for problem: https://adventofcode.com/2022/day/1

def main():
    with open('day_one.txt', 'r') as f:
        sums = []
        current_sum = 0
        for line in f:
            line = line.strip()
            if line:
                current_sum += int(line)
            else:
                sums.append(current_sum)
                current_sum = 0

    print(f"The Part 1 answer is {max(sums)}.")

    sums.sort(reverse=True)
    top_three_sum = 0
    for i in range(0, 3):
        top_three_sum += sums[i]
    print(f"The Part 2 answer is {top_three_sum}.")
        
if __name__ == '__main__':
    main()
