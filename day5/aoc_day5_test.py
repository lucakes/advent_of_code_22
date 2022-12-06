import pathlib
import pytest
import aoc_day5 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_top_of_stacks():
    input_1 = (INPUT_DIR / "aoc_day5_test_input1.txt").read_text().strip()
    assert aoc.get_top_of_stacks(input_1) == "CMZ"


def test_top_of_stacks_different_crane():
    input_1 = (INPUT_DIR / "aoc_day5_test_input1.txt").read_text().strip()
    assert aoc.get_top_of_stacks_different_crane(input_1) == "MCD"
