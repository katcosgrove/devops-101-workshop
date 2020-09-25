import pytest
from sample_package.app import fizz_buzz_tree, fizz_buzz


def test_fizz_buzz_tree(small_bst):
    """Test fizzbuzz tree function with all possibilities."""
    temp = fizz_buzz_tree(small_bst)
    assert temp.root.val == 'Buzz'


def test_fizz_buzz_tree_empty(empty_bst):
    """Test fizzbuzz tree function raises error properly."""
    with pytest.raises(ValueError):
        fizz_buzz_tree(empty_bst)


def test_fizz_buzz_tree_none(no_fizzbuzz):
    """Test fizzbuzz tree function with no conditions met."""
    temp = fizz_buzz_tree(no_fizzbuzz)
    assert temp.root.val == 1


def test_fizz_buzz_fizz(fizz_node):
    """Test fizzbuzz finds fizz value."""
    temp = fizz_buzz(fizz_node)
    assert temp == 'Fizz'


def test_fizz_buzz_buzz(buzz_node):
    """Test fizzbuzz finds buzz value."""
    temp = fizz_buzz(buzz_node)
    assert temp == 'Buzz'


def test_fizz_buzz_fizz(fizzbuzz_node):
    """Test fizzbuzz finds fizzbuzz value."""
    temp = fizz_buzz(fizzbuzz_node)
    assert temp == 'FizzBuzz'