import pytest

from homework import (
    task_11_separate_num_to_hours_and_minutes,
    task_12_largest_word_in_string,
    task_13_print_back_string,
    task_14_fibonnaci_numbers,
    task_15_generate_list_even_num,
    task_16_add_numbers_from_1_to_input,
    task_17_factorial_of_num,
    task_18_replace_letter_and_capitalize_vowel,
    task_19_letters_in_alphabetical_order,
    task_20_compare_two_num
)

@pytest.mark.parametrize('input_data, expected_result',
                         [(63, '1:3'), (85, '1:25')])
def test_task_11_separate_num_to_hours_and_minutes(input_data, expected_result):
    assert task_11_separate_num_to_hours_and_minutes(input_data) == expected_result


@pytest.mark.parametrize('input_data, expected_result',
                         [('fun&!! time', 'time'), ('I love dogs', 'love')])
def test_task_12_largest_word_in_string(input_data, expected_result):
    assert task_12_largest_word_in_string(input_data) == expected_result


def test_task_13_print_back_string(monkeypatch):
    input_string = "My name is Michele"
    expected_string = 'Michele is name My'
    monkeypatch.setattr('builtins.input', lambda: input_string)
    assert task_13_print_back_string() == expected_string


def test_task_14_fibonnaci_numbers(monkeypatch):
    fib = [1, 1, 2, 3, 5, 8, 13, 21]
    monkeypatch.setattr('builtins.input', lambda: 8)
    assert task_14_fibonnaci_numbers() == fib


def test_task_15_generate_list_even_num():
    input_data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    expected_result = [4, 16, 36, 64, 100]
    assert task_15_generate_list_even_num(input_data) == expected_result


def test_task_16_add_numbers_from_1_to_input(monkeypatch):
    expected_result = 10
    monkeypatch.setattr('builtins.input', lambda: 4)
    assert task_16_add_numbers_from_1_to_input() == expected_result


def test_task_17_factorial_of_num():
    input_data = 4
    expected_result = 24
    assert task_17_factorial_of_num(input_data) == expected_result


@pytest.mark.parametrize('input_string, expected_string',
                         [('abcd', 'bcdE'), ('efgh', 'fghI')])
def test_task_18_replace_letter_and_capitalize_vowel(input_string, expected_string):
    assert task_18_replace_letter_and_capitalize_vowel(input_string) == expected_string


@pytest.mark.parametrize('input_data, expected', [('edcba', 'abcde'), ('fncrdz', 'cdfnrz')])
def test_task_19_letters_in_alphabetical_order(input_data, expected):
    assert task_19_letters_in_alphabetical_order(input_data) == expected


@pytest.mark.parametrize('input_data, test_input2, expected_result',
                          [(5, 8, True), (9, 4, False), (5, 5, -1)])
def test_task_20_compare_two_num(input_data, test_input2, expected_result):
    assert task_20_compare_two_num(input_data, test_input2) == expected_result