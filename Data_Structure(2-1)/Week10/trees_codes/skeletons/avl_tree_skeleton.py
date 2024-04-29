class AVLTree():
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right', '_height' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._height = 0

        def left_height(self):
            return self._left._height if self._left != None else 0

        def right_height(self):
            return self._right._height if self._right != None else 0

        def set_height(self, new_height):
            self._height = new_height


    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def insert(self, element):
        ## IMPLEMENT HERE

    def delete(self, element):
        ## IMPLEMENT HERE

    def display(self):
        self._display(self._root, 0)

    def _display(self, node, depth):
        if node == None:
            return

        if node._right != None:
            self._display(node._right, depth+1)
        label = ''
        if node == self._root:
            label += '  <- root'
        if node == self._last:
            label += '  <- last'
        print(f'{"    "*depth}* {node._element}({node._height}){label}')
        if node._left != None:
            self._display(node._left, depth+1)