from src.collapse_number import collapse
import pytest


@pytest.mark.parametrize("number, expected_result", [(222, 6),
                                                     (51278, 5),
                                                     (4, 4),
                                                     ("", 0)])
def test_collapse_number_positive(number, expected_result):
    assert collapse(number) == expected_result


# @pytest.mark.parametrize("expected_exception, argument", [(ValueError, "BC"),
#                                                           (ValueError, " "),
#                                                           (TypeError, ())])
# def test_collapse_number_negative(expected_exception, argument):
#     with pytest.raises(expected_exception):
#         collapse(argument)


def test_collapse_number_ok_one_iteration():
    assert collapse(222) == 6


def test_collapse_number_ok_more_iterations():
    assert collapse(51278) == 5


def test_collapse_number_one_digit():
    assert collapse(4) == 4


def test_collapse_number_zero_digit():
    assert collapse("") == 0


def test_collapse_number_not_number():
    with pytest.raises(ValueError):
        collapse("BC")


def test_collapse_number_empty_input():
    with pytest.raises(TypeError):
        collapse()


def test_collapse_number_space():
    with pytest.raises(ValueError):
        collapse(" ")
