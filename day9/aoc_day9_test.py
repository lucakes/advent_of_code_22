import pathlib
import pytest
import aoc_day9 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_get_visited_two_knots():
    input = (INPUT_DIR / "aoc_day9_test_input.txt").read_text().strip()
    assert len(aoc.get_visited(input, [{"x": 0, "y": 0}, {"x": 0, "y": 0}])) == 13


def test_get_visited_ten_knots():
    input = (INPUT_DIR / "aoc_day9_test_input2.txt").read_text().strip()
    assert len(aoc.get_visited(input, [{"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}, {"x": 0, "y": 0}])) == 36
