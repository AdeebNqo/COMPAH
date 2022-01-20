from sympy import Function, Symbol


class InitialisableFunction(Function):
    inits = {}

    @classmethod
    def set_func_inits_at_points(cls, inits):
        InitialisableFunction.inits = inits

    @classmethod
    def eval(cls, x):
        if x.is_Number:
            if x in InitialisableFunction.inits.keys():
                return InitialisableFunction.inits[x]
            else:
                return super.eval(x)


class GeometricFunction(InitialisableFunction):
    def __init__(self, a=None, r=None):
        super().__init__()
        if a and r:
            a_internal = a
            r_internal = r
        else:
            a_internal = Symbol('a')
            r_internal = Symbol('r')
        n_internal = Symbol('n')
        self.function = a_internal * (r_internal ** n_internal)


class Sequence(object):
    def __init__(self):
        self.function = None

    def get_function(self):
        if self.function:
            return self.function
        else:
            raise NotImplementedError


class GeometricSequence(Sequence):
    def __init__(self, a=None, r=None):
        super().__init__()
        self.function = GeometricFunction(a, r)
