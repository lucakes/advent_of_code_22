import pathlib
import sys


def generate_sections_of_range(assignments):
    split_assignments = assignments.split("-")
    max_section = int(split_assignments.pop())
    min_section = int(split_assignments.pop())
    section_list = []
    for n in range(min_section, max_section+1, 1):
        section_list.append(n)
    return section_list


def check_overlap(elf_pair):
    assignments = elf_pair.split(",")
    assignment_first_elf = generate_sections_of_range(assignments.pop())
    assignment_second_elf = generate_sections_of_range(assignments.pop())
    one_contain_any = any(elem in assignment_first_elf for elem in assignment_second_elf)
    return one_contain_any


def check_full_coverage(elf_pair):
    assignments = elf_pair.split(",")
    assignment_first_elf = generate_sections_of_range(assignments.pop())
    assignment_second_elf = generate_sections_of_range(assignments.pop())
    result_one = all(elem in assignment_first_elf for elem in assignment_second_elf)
    result_two = all(elem in assignment_second_elf for elem in assignment_first_elf)
    return result_two or result_one


def calculate_pairs_containing_others(input):
    elf_pairs = input.split("\n")
    count_pairs = 0
    for elf_pair in elf_pairs:
        if check_full_coverage(elf_pair):
            count_pairs += 1
    return count_pairs


def calculate_overlaping(input):
    elf_pairs = input.split("\n")
    count_pairs = 0
    for elf_pair in elf_pairs:
        if check_overlap(elf_pair):
            count_pairs += 1
    return count_pairs


if __name__ == "__main__":
    for path in sys.argv[1:]:
        input = pathlib.Path(path).read_text().strip()
        solution_part_one = calculate_pairs_containing_others(input)
        solution_part_two = calculate_overlaping(input)
        print("solution part one: " + str(solution_part_one)+" solution part two: " + str(solution_part_two))
