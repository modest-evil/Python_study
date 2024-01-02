from src.transform_text import transform
import pytest


@pytest.mark.parametrize("text, expected_result", [("a3b2c1", "aaabbc"),
                                                   ("d4", "dddd"),
                                                   ("2473", "2222777"),
                                                   ("@3#2!4", "@@@##!!!!")])
def test_transform_text_positive(text, expected_result):
    assert transform(text) == expected_result


@pytest.mark.parametrize("expected_exception, text", [(ValueError, "abcd"),
                                                      (ValueError, "@#!"),
                                                      (IndexError, " "),
                                                      (IndexError, "a2b3j"),
                                                      (IndexError, "a")])
def test_transform_text_negative(expected_exception, text):
    with pytest.raises(expected_exception):
        transform(text)


# def test_transform_text_normal():
#     assert transform("a3b2c1") == "aaabbc"
#
#
# def test_transform_text_short_text():
#     assert transform("d4") == "dddd"
#
#
# def test_transform_text_numbers():
#     assert transform("2473") == "2222777"
#
#
# def test_transform_text_no_numbers():
#     with pytest.raises(ValueError):
#         transform("abcd")
#
#
# def test_transform_empty_value():
#     with pytest.raises(IndexError):
#         transform(" ")
