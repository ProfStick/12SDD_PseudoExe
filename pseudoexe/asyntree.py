'''PseudoExe abstract syntax tree.
'''         

class Sequence():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        for s in self.value:
            s.eval()

class Number():
    '''Evaluates an integer'''
    def __init__(self, value):
        self.value = value

    def eval(self):
        return eval(self.value)


class Display():
    '''Output to the standard output.'''
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())