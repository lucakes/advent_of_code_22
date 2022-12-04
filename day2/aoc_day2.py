import pathlib
import sys

SCORE_LOSS = 0
SCORE_DRAW = 3
SCORE_WIN = 6

TRANSLATION_LETTER_SHAPE = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

SHAPE_SCORE = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

POINTS_OUTCOME = {
    "Loss": 0,
    "Draw": 3,
    "Win": 6
}

TRANSLATION_LETTER_OUTCOME = {
    "X": "Loss",
    "Y": "Draw",
    "Z": "Win"
}


def game_logic_part_two(shape_opponent, desired_outcome):
    if shape_opponent == "Rock" and desired_outcome == "Loss":
        return "Scissors"
    elif shape_opponent == "Rock" and desired_outcome == "Draw":
        return "Rock"
    elif shape_opponent == "Rock" and desired_outcome == "Win":
        return "Paper"
    elif shape_opponent == "Paper" and desired_outcome == "Loss":
        return "Rock"
    elif shape_opponent == "Paper" and desired_outcome == "Draw":
        return "Paper"
    elif shape_opponent == "Paper" and desired_outcome == "Win":
        return "Scissors"
    elif shape_opponent == "Scissors" and desired_outcome == "Loss":
        return "Paper"
    elif shape_opponent == "Scissors" and desired_outcome == "Draw":
        return "Scissors"
    elif shape_opponent == "Scissors" and desired_outcome == "Win":
        return "Rock"


def game_logic(shape_opponent, shape_player):
    if shape_opponent == "Rock" and shape_player == "Rock":
        return "Draw"
    elif shape_opponent == "Rock" and shape_player == "Paper":
        return "Win"
    elif shape_opponent == "Rock" and shape_player == "Scissors":
        return "Loss"
    elif shape_opponent == "Paper" and shape_player == "Rock":
        return "Loss"
    elif shape_opponent == "Paper" and shape_player == "Paper":
        return "Draw"
    elif shape_opponent == "Paper" and shape_player == "Scissors":
        return "Win"
    elif shape_opponent == "Scissors" and shape_player == "Rock":
        return "Win"
    elif shape_opponent == "Scissors" and shape_player == "Paper":
        return "Loss"
    elif shape_opponent == "Scissors" and shape_player == "Scissors":
        return "Draw"


def calculate_shape(shape_player):
    return SHAPE_SCORE[TRANSLATION_LETTER_SHAPE[shape_player]]


def calculate_match(shape_player, shape_opponent):
    return POINTS_OUTCOME[game_logic(TRANSLATION_LETTER_SHAPE[shape_opponent], TRANSLATION_LETTER_SHAPE[shape_player])]


def calculate_sum_scores(input):
    matches = input.split("\n")
    sum_score = 0
    for match in matches:
        shapes = match.split(" ")
        shape_player = shapes.pop()
        shape_opponent = shapes.pop()
        sum_score = sum_score + calculate_match(shape_player, shape_opponent) + calculate_shape(shape_player)
    return sum_score


def calculate_score_part_two(input):
    matches = input.split("\n")
    sum_score = 0
    for match in matches:
        shapes = match.split(" ")
        shape_desired_outcome = shapes.pop()
        shape_opponent = shapes.pop()
        sum_score = sum_score + POINTS_OUTCOME[TRANSLATION_LETTER_OUTCOME[shape_desired_outcome]] \
                    + SHAPE_SCORE[game_logic_part_two(TRANSLATION_LETTER_SHAPE[shape_opponent], TRANSLATION_LETTER_OUTCOME[shape_desired_outcome])]
    return sum_score


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text().strip()
        solution_part_one = calculate_sum_scores(input)
        solution_part_two = calculate_score_part_two(input)
        print("solution part one: " + str(solution_part_one) + " solution part two: " + str(solution_part_two))
