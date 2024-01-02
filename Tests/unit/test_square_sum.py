from src.square_sum import square_sum
import pytest


@pytest.mark.parametrize("a, b, c, expected_result", [(4, 7, 1, 65),
                                                      (1, 4, 7, 65),
                                                      (1, 1, 1, 2),
                                                      (0, 0, 0, 0),
                                                      (-3, -9, -4, 25)])
def test_square_sum_positive(a, b, c, expected_result):
    assert square_sum(a, b, c) == expected_result


def test_square_sum_wrong_type():
    with pytest.raises(TypeError):
        square_sum("1", 2, 3)


def test_square_sum_lack_of_args():
    with pytest.raises(TypeError):
        square_sum(2, 3)


def test_square_sum_too_much_args():
    with pytest.raises(TypeError):
        square_sum(2, 3, 5, 1)


# def test_square_sum_normal():
#     assert square_sum(4, 7, 1) == 65
#
#
# def test_square_sum_sorted():
#     assert square_sum(1, 4, 7) == 65
#
#
# def test_square_sum_ones():
#     assert square_sum(1, 1, 1) == 2
#
#
# def test_square_sum_zeroes():
#     assert square_sum(0, 0, 0) == 0
#
#
# def test_square_sum_all_below_zero():
#     assert square_sum(-3, -9, -4) == 25
