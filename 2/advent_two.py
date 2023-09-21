# Solution for problem: https://adventofcode.com/2022/day/2

class ActionScores:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class ResultScores:
    LOSS = 0
    DRAW = 3
    WIN = 6

def get_action_score(chr):
    if chr == 'A' or chr == 'X':
        return ActionScores.ROCK
    elif chr == 'B' or chr == 'Y':
        return ActionScores.PAPER
    elif chr == 'C' or chr == 'Z':
        return ActionScores.SCISSORS

def get_intended_result(chr):
    if chr == 'X':
        return ResultScores.LOSS
    elif chr == 'Y':
        return ResultScores.DRAW
    else:
        return ResultScores.WIN

def get_intended_score(opp_score, intended_result):
    if opp_score == ActionScores.ROCK:
        if intended_result == ResultScores.WIN:
            my_score = ActionScores.PAPER
        elif intended_result == ResultScores.LOSS:
            my_score = ActionScores.SCISSORS
        else:
            my_score = ActionScores.ROCK
    elif opp_score == ActionScores.PAPER:
        if intended_result == ResultScores.WIN:
            my_score = ActionScores.SCISSORS
        elif intended_result == ResultScores.LOSS:
            my_score = ActionScores.ROCK
        else:
            my_score = ActionScores.PAPER
    else:
        if intended_result == ResultScores.WIN:
            my_score = ActionScores.ROCK
        elif intended_result == ResultScores.LOSS:
            my_score = ActionScores.PAPER
        else:
            my_score = ActionScores.SCISSORS
    return intended_result + my_score

def get_result(opp_score, my_score):
    if opp_score == ActionScores.ROCK:
        if my_score == ActionScores.PAPER:
            result = ResultScores.WIN
        elif my_score == ActionScores.SCISSORS:
            result = ResultScores.LOSS
        else:
            result = ResultScores.DRAW
    elif opp_score == ActionScores.PAPER:
        if my_score == ActionScores.SCISSORS:
            result = ResultScores.WIN
        elif my_score == ActionScores.ROCK:
            result = ResultScores.LOSS
        else:
            result = ResultScores.DRAW
    else:
        if my_score == ActionScores.ROCK:
            result = ResultScores.WIN
        elif my_score == ActionScores.PAPER:
            result = ResultScores.LOSS
        else:
            result = ResultScores.DRAW
    return result + my_score

def main():
    with open('day_two.txt', 'r') as f:
        part_one_sum = 0
        part_two_sum = 0

        for line in f:
            first_chr, second_chr = line.strip().split(" ")

            opp_score = get_action_score(first_chr)
            my_score = get_action_score(second_chr)
            part_one_score = get_result(opp_score, my_score)
            part_one_sum += part_one_score

            intended_result = get_intended_result(second_chr)
            part_two_score = get_intended_score(opp_score, intended_result)
            part_two_sum += part_two_score

    print(f"My total score for part one was {part_one_sum}")
    print(f"My total score for part two was {part_two_sum}")

if __name__ == '__main__':
    main()
