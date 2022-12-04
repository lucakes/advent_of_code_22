import pathlib
import pytest
import aoc_day3 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_letter_P_score_42():
    assert aoc.calculate_score_letter("P") == 42


def test_sum_score_157():
    input_1 = (INPUT_DIR / "aoc_day3_test_input1.txt").read_text().strip()
    assert aoc.calculate_sum_priorities(input_1) == 157


def test_difference():
    assert aoc.find_difference_letter('vJrwpWtwJgWr', 'hcsFMMfFFhFp') == "p"


def test_common_letter():
    assert aoc.find_common_letter(["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]) == "r"


def test_score_part_two_70():
    input_1 = (INPUT_DIR / "aoc_day3_test_input1.txt").read_text().strip()
    assert aoc.calculate_part_two(input_1) == 70
