from sample_package.bst import BST, Node
import pytest


@pytest.fixture
def small_bst():
    return BST([20, 15, 9, 11])


@pytest.fixture
def empty_bst():
    return BST()


@pytest.fixture
def no_fizzbuzz():
    return BST([1, 4, 7, 11])


@pytest.fixture
def fizz_node():
    return Node(3)


@pytest.fixture
def buzz_node():
    return Node(5)


@pytest.fixture
def fizzbuzz_node():
    return Node(15)