class Sequence():
    '''Iterates through a sequence'''
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        for s in self.value:
            s.eval()

