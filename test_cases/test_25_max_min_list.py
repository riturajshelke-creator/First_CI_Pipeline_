import importlib
import pytest

module = importlib.import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([10, 5, 20, 3, 15]) == (20, 3)


def test_all_positive_numbers():
    assert find_max_min([2, 4, 6, 8]) == (8, 2)


def test_negative_numbers():
    assert find_max_min([-5, -2, -10, -1]) == (-1, -10)


def test_mixed_numbers():
    assert find_max_min([-5, 0, 10, -2, 7]) == (10, -5)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4, 4]) == (4, 4)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])