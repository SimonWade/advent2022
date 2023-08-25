
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

    print(f"The maximum calories carried  was {max(sums)}.")

    sums.sort(reverse=True)
    top_sum = 0
    for i in range(0, 3):
        top_sum += sums[i]
    print(f"The top three were carrying {top_sum} calories.")
        
if __name__ == '__main__':
    main()
