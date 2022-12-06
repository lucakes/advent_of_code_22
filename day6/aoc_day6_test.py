import pathlib
import pytest
import aoc_day6 as aoc

INPUT_DIR = pathlib.Path(__file__).parent


def test_number_characters_before_start_packet_5():
    assert aoc.get_number_characters_before_start_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5


def test_number_characters_before_start_packet_6():
    assert aoc.get_number_characters_before_start_packet("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6


def test_number_characters_before_start_packet_10():
    assert aoc.get_number_characters_before_start_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10


def test_number_characters_before_start_packet_11():
    assert aoc.get_number_characters_before_start_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


def test_number_characters_before_message_packet_19():
    assert aoc.get_number_characters_before_start_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19


def test_number_characters_before_message_packet_23():
    assert aoc.get_number_characters_before_start_packet("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23


def test_number_characters_before_message_packet_29():
    assert aoc.get_number_characters_before_start_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29


def test_number_characters_before_message_packet_26():
    assert aoc.get_number_characters_before_start_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
