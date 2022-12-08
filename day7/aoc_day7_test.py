import pathlib
import pytest
import aoc_day7 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_get_total_size_directories_above_100000():
    input_1 = (INPUT_DIR / "aoc_day7_test_input.txt").read_text().strip()
    assert aoc.get_total_size_directories_above_100000(input_1) == 95437


def test_free_space():
    input_1 = (INPUT_DIR / "aoc_day7_test_input.txt").read_text().strip()
    assert aoc.free_space(input_1) == 24933642
