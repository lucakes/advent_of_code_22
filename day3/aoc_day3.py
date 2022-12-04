import pathlib
import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def find_difference_letter(compartment_two, compartment_first):
    for letter in compartment_two:
        result_find = compartment_first.find(letter)
        if result_find != -1:
            return letter

    for letter in compartment_first:
        result_find = compartment_two.find(letter)
        if result_find != -1:
            return letter


def calculate_score_letter(difference_letter):
    return ALPHABET.find(difference_letter)+1


def calculate_sum_priorities(input):
    rucksacks = input.split("\n")
    sum_score = 0
    for rucksack in rucksacks:
        compartment_first = rucksack[:len(rucksack) // 2]
        compartment_two = rucksack[len(rucksack) // 2:]
        difference_letter = find_difference_letter(compartment_two, compartment_first)
        sum_score = sum_score + calculate_score_letter(difference_letter)
    return sum_score


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text().strip()
        solution_part_one = calculate_sum_priorities(input)
        print("solution part one: " + str(solution_part_one))
