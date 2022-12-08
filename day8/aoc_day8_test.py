import pathlib
import pytest
import aoc_day8 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_get_visible_trees():
    input_1 = (INPUT_DIR / "aoc_day8_test_input.txt").read_text().strip()
    assert len(aoc.get_visible_trees(input_1)) == 21


def test_get_scenic_scores():
    input_1 = (INPUT_DIR / "aoc_day8_test_input.txt").read_text().strip()
    assert max(aoc.get_scenic_scores(input_1)) == 8
