
import importlib

module = importlib.import_module("24_merge_sorted_lists")
merge_sorted_lists = module.merge_sorted_lists


def test_normal_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]


def test_first_list_empty():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]


def test_second_list_empty():
    assert merge_sorted_lists([1, 2, 3], []) == [1, 2, 3]


def test_both_lists_empty():
    assert merge_sorted_lists([], []) == []


def test_lists_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]


def test_different_lengths():
    assert merge_sorted_lists([1, 5], [2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_single_element_lists():
    assert merge_sorted_lists([3], [1]) == [1, 3]


def test_original_lists_unchanged():
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    merge_sorted_lists(list1, list2)

    assert list1 == [1, 3, 5]
    assert list2 == [2, 4, 6]