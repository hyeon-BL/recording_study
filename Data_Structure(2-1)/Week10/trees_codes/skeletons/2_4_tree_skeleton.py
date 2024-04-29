class TwoFourTree():
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_parent', '_keys', '_children' # streamline memory usage

        def __init__(self, parent=None, keys=[], children=[]):
            self._parent = parent
            self._keys = keys
            self._children = children

    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def search(self, element):
        ## IMPLEMENT HERE

    def insert(self, element):
        ## IMPLEMENT HERE

    def delete(self, element):
        ## IMPLEMENT HERE

    def display(self):
        self._display(self._root, 0)

    def _display(self, node, depth):
        if node == None:
            return
        # try to impelement a recursive traversal that is displaying the tree content

            