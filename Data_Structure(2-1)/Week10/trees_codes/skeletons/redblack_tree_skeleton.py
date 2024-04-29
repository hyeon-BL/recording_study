class RedBlackTree():
    class _Node:
        RED = 0
        BLACK = 1
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right', '_color' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None, color=RED):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            self._color = color

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

        if node._right != None:
            self._display(node._right, depth+1)
        label = ''
        if node == self._root:
            label += '  <- root'

        if node._color == self._Node.RED:
            colorstr = 'R'
        else:
            colorstr = 'B'
        print(f'{"    "*depth}* {node._element}({colorstr}){label}')
        if node._left != None:
            self._display(node._left, depth+1)

