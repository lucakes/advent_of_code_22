import pathlib
import aoc_day1 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_max_calories_correct():
    input_1 = (INPUT_DIR / "aoc_day1_test_input1.txt").read_text().strip()
    assert aoc.find_maximum_calories(input_1) == 24000


def test_max_calories_incorrect():
    input_1 = (INPUT_DIR / "aoc_day1_test_input1.txt").read_text().strip()
    assert aoc.find_maximum_calories(input_1) != 26000


def test_sum_top3_correct():
    input_1 = (INPUT_DIR / "aoc_day1_test_input1.txt").read_text().strip()
    assert aoc.sum_top3_calories_per_elf(input_1) == 45000


def test_sum_top3_incorrect():
    input_1 = (INPUT_DIR / "aoc_day1_test_input1.txt").read_text().strip()
    assert aoc.sum_top3_calories_per_elf(input_1) != 5000
