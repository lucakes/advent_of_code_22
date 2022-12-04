import pathlib
import pytest
import aoc_day4 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_generate_section():
    assert aoc.generate_sections_of_range("5-7") == [5, 6, 7]


def check_overlap():
    assert aoc.generate_sections_of_range("5-7,7-7")


def check_no_overlap():
    assert not aoc.generate_sections_of_range("5-7,9-10")


def check_full_coverage():
    assert aoc.generate_sections_of_range("5-7,2-10")


def check_not_full_coverage():
    assert not aoc.generate_sections_of_range("5-7,6-10")


def test_pairs_containing_others():
    input_1 = (INPUT_DIR / "aoc_day4_test_input1.txt").read_text().strip()
    assert aoc.calculate_pairs_containing_others(input_1) == 2


def test_pairs_overlaping():
    input_1 = (INPUT_DIR / "aoc_day4_test_input1.txt").read_text().strip()
    assert aoc.calculate_overlaping(input_1) == 4
