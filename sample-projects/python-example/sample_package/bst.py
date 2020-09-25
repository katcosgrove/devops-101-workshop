class Node:
    """Create node class."""
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return '<Node Val: {}'.format(self.val)

    def __str__(self):
        return self.val


class BST:
    """Create binary search tree class."""
    def __init__(self, iter=[]):
        self.root = None

        try:
            for item in iter:
                self.insert(item)
        except ValueError:
            print('Value error! Please insert an iterable.')

    def __repr__(self):
        if self.root:
            return '<BST Root {}>'.format(self.root.val)
        else:
            raise AttributeError('Tree is empty!')

    def __str__(self):
        if self.root:
            return self.root.val
        else:
            raise AttributeError('Tree is empty!')

    def in_order(self, operation):
        """In order traversal."""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            operation(node)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, operation):
        """Post order traversal."""
        def _walk(node=None):
            if node is None:
                return

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

            operation(node)

        _walk(self.root)

    def pre_order(self, operation):
        """Pre order traversal."""
        def _walk(node=None):
            if node is None:
                return

            operation(node)

            if node.left is not None:
                _walk(node.left)

            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def insert(self, val):
        """Insert a new node."""
        node = Node(val)
        current = self.root

        if self.root is None:
            self.root = node
            return node

        while current:
            if val >= current.val:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = node
                    break

            elif val < current.val:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = node
                    break

        return node