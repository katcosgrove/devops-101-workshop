def fizz_buzz(node):
    """Helper function for fizzbuzz conditionals."""
    if node.val % 5 == 0 and node.val % 3 == 0:
        node.val = 'FizzBuzz'
        return node.val
    elif node.val % 3 == 0:
        node.val = 'Fizz'
        return node.val
    elif node.val % 5 == 0:
        node.val = 'Buzz'
        return node.val
    else:
        return node.val


def fizz_buzz_tree(tree):
    """Traverses a tree and executes fizzbuzz helper at each node."""
    if tree.root is None:
        raise ValueError('This tree is empty!')

    def _walk(node=None):
        if node is None:
            return

        fizz_buzz(node)

        if node.left is not None:
            _walk(node.left)

        if node.right is not None:
            _walk(node.right)

    _walk(tree.root)
    return tree