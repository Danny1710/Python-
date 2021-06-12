import pytest
import sys
from Question_8 import count_if_triple, count_if_multiple

message = "{} contains {} multiples of {} - {}. Your function returned {}."


def test_count_if_triple_simple():
    cases = [
        ([12, 7, 9, 5, 2, 1, 12], 3, [12, 9, 12]),
        ([15, 2, 2, 200, 300, 101, 96], 3, [15, 300, 96]),
        ([2, 27, 6, -15, 24, 8, -80], 4, [27, 6, -15, 24]),
    ]

    for list_of_ints, correct, output in cases:
        result = count_if_triple(list_of_ints)
        assert result == correct, message.format(list_of_ints, correct, 3, output, result)


def test_count_if_triple_edge():
    cases = [
        ([11, 7, 19, 5, 2, 1, 122], 0, []),
        ([15, 12, 12, 30, -30, -21, 96], 7, [15, 12, 12, 30, -30, -21, 96]),
        ([], 0, []),
        ([3], 1, [3]),
        ([0], 1, [0]),
    ]

    for list_of_ints, correct, output in cases:
        result = count_if_triple(list_of_ints)
        assert result == correct, message.format(list_of_ints, correct, 3, output, result)


def test_count_if_multiple_simple():
    cases = [
        ([12, 7, 9, 5, 2, 1, 12], 3, 3, [12, 9, 12]),
        ([15, 2, 2, 200, 300, 101, 96], 4, 3, [200, 300, 96]),
        ([2, 27, 6, -15, 24, 8, -80], 6, 2, [6, 24]),
    ]

    for list_of_ints, divisor, correct, output in cases:
        result = count_if_multiple(list_of_ints, divisor)
        assert result == correct, message.format(list_of_ints, correct, divisor, output, result)


def test_count_if_multiple_edge():
    cases = [
        ([11, 7, 19, 5, 2, 1, 122], 20, 0, []),
        ([15, 12, 12, 30, -30, -21, 96], 1, 7, [15, 12, 12, 30, -30, -21, 96]),
        ([], 5, 0, []),
        ([3], 2, 0, []),
        ([0], 100, 1, [0]),
    ]

    for list_of_ints, divisor, correct, output in cases:
        result = count_if_multiple(list_of_ints, divisor)
        assert result == correct, message.format(list_of_ints, correct, divisor, output, result)


if __name__ == "__main__":
    pytest.main(sys.argv)