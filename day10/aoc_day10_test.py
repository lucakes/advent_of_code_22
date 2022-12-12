import pathlib
import pytest
import aoc_day10 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_get_signal_strength():
    input = (INPUT_DIR / "aoc_day10_test_input.txt").read_text().strip()
    assert sum(aoc.get_signal_strength(input, [20, 60, 100, 140, 180, 220])) == 13140
