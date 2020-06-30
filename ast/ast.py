"""ast - Abstract syntax tree for pseudoexe.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  TODO

"""

class BinaryOp():
    """binary operations super class."""
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    """Sum left and right"""
    def eval(self):
        return self.left.eval() + self.right.eval()


class Display():
    """Output to the standard output."""
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())