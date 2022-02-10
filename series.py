class Series(object):
    def __init__(self):
        self.sequence = None


class ArithmeticSSeries(Series):
    def __init__(self, arithmetic_seq):
        super().__init__()
        self.function = arithmetic_seq
