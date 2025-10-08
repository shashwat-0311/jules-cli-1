import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test that the longest of multiple streaks is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_all_positive_numbers():
    """Test a list containing only positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negative_numbers():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2

def test_no_positive_numbers():
    """Test a list with no positive numbers, which should result in a streak of 0."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_non_positive_number():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_the_beginning():
    """Test a streak that occurs at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, -1, -2]) == 3

def test_streak_at_the_end():
    """Test a streak that occurs at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4
