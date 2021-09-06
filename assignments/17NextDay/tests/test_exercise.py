"""
Evaluating the results of a function

Using Python decorators and parametrize to add multiple independent tests
This allows each test to be evaluated independently
"""

import pytest
from src.exercise import is_leap, month_days, next_day

@pytest.mark.parametrize('year, result, message', [
                          (2021, False, "Regular year"),
                          (2020, True, "Divisible by 4"),
                          (2100, False, "Divisible by 100"),
                          (2000, True, "Divisible by 400")
                         ])
def test_is_leap(year, result, message):
    assert is_leap(year) == result, message


@pytest.mark.parametrize('month, year, result, message', [
                          (1, 2021, 31, "January"),
                          (3, 2021, 31, "March"),
                          (4, 2021, 30, "April"),
                          (2, 2021, 28, "February non leap year"),
                          (2, 2020, 29, "February leap year"),
                         ])
def test_month_days(month, year, result, message):
    assert month_days(month, year) == result, message


@pytest.mark.parametrize('day, month, year, result, message',
                         [
                          (1, 1, 1999, (2, 1, 1999), "First day of the year"),
                          (7, 6, 2020, (8, 6, 2020), "Normal day"),
                          (28, 2, 2019, (1, 3, 2019), "Non Leap year"),
                          (28, 2, 2020, (29, 2, 2020), "Leap year % 4"),
                          (28, 2, 2000, (29, 2, 2000), "Leap year % 400"),
                          (28, 2, 2100, (1, 3, 2100), "Non Leap year % 100"),
                          (31, 10, 1999, (1, 11, 1999), "Last day of the month"),
                          (31, 12, 1998, (1, 1, 1999), "Last day of the year"),
                         ])
def test_next_day(day, month, year, result, message):
    assert next_day(day, month, year) == result, message
