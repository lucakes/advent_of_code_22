import pathlib
import pytest
import aoc_day2 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_first_input_correct():
    input_1 = (INPUT_DIR / "aoc_day2_test_input1.txt").read_text().strip()
    assert aoc.calculate_sum_scores(input_1) == 45000


def test_first_input_incorrect():
    input_1 = (INPUT_DIR / "aoc_day2_test_input1.txt").read_text().strip()
    assert aoc.calculate_sum_scores(input_1) != 4
