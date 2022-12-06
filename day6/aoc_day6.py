import pathlib
import sys


def get_number_characters_before_start_packet(input, quantity_distinct_characters):
    for n in range(quantity_distinct_characters, len(input), 1):
        relevant_chars = input[n-quantity_distinct_characters:n]
        unique_chars = set(relevant_chars)
        if len(unique_chars) == quantity_distinct_characters:
            return n


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text()
        solution_part_one = get_number_characters_before_start_packet(input, 4)
        solution_part_two = get_number_characters_before_start_packet(input, 14)
        print("solution part one: " + str(solution_part_one) + " solution part two: " + str(solution_part_two))
