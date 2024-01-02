from src.search_pairs import search_pairs
import pytest


@pytest.mark.parametrize("given, target, expected_result", [([1, 4, 6, 3, 2], 8, [2, 4]),
                                                            ([1, 7, 3, 11, 4, 6, 2], 8, [0, 1]),
                                                            ([1, 4, 5, 1], 8, None),
                                                            (["abcd"], 5, None),
                                                            ([], 5, None),
                                                            ([[1, 2], [5, 6]], 8, None)])
def test_search_pairs_positive(given, target, expected_result):
    assert search_pairs(given, target) == expected_result


# def test_search_pairs_one_pair():
#     assert search_pairs([1, 4, 6, 3, 2], 8) == [2, 4]
#
#
# def test_search_pairs_two_pairs():
#     assert search_pairs([1, 7, 3, 11, 4, 6, 2], 8) == [0, 1]
#
#
# def test_search_pairs_no_pairs():
#     assert search_pairs([1, 4, 5, 1], 8) is None


def test_search_pairs_negative():
    with pytest.raises(TypeError):
        search_pairs(None, 4)

