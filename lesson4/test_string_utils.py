import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("алексей", "Алексей"),
    ("alex", "Alex"),
    ("санкт-петербург", "Санкт-петербург"),])

def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("Алексей", "Алексей"),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Кирилл", "Кирилл"),
    ("  alex", "alex"),
    ("   Санкт-петербург", "Санкт-петербург"), ])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123 abc", "123 abc"),
    ("Алексей   ", "Алексей   "),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("S","S", True),
    (" Wer"," Wer", True),
    ("   Санкт-петербург","Санкт", True), ])
def test_contains_positive(input_str,symbol, expected):
    assert string_utils.contains(input_str,symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str,symbol, expected", [
    ("S", "T", False),
    (" Wer", " wer", False),
    ("   Санкт-петербург", "мос", False), ])

def test_contains_negative(input_str,symbol, expected):
    assert string_utils.contains(input_str,symbol) == expected



@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("S","S", ""),
    (" Wer"," Wer", ""),
    ("   Санкт-петербург","Санкт", "   -петербург"), ])
def test_delete_symbol_positive(input_str,symbol, expected):
    assert string_utils.delete_symbol(input_str,symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str,symbol, expected", [
    ("S", "T", "S"),
    (" Wer", " wer",  " Wer"),
    ("   Санкт-петербург", "мос", "   Санкт-петербург"), ])

def test_delete_symbol_negative(input_str,symbol, expected):
    assert string_utils.delete_symbol(input_str,symbol) == expected

