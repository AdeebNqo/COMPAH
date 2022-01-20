from sympy import Function, Symbol, Eq
from sympy.printing import latex


class CompahFunction:
    def __init__(self, name):
        self.inits = {}
        self.default_function = None
        self.name = name

    def set_func_inits_at_points(self, inits):
        self.inits = inits

    def set_default_func(self, some_function):
        self.default_function.inits = some_function

    def __call__(self, pos):
        if pos in self.inits.keys():
            return self.inits[pos]
        else:
            return self.default_function.subs(self.n, pos)

    def __str__(self):
        from sympy.abc import n
        k = Function('s')
        func = Eq(k(n), self.default_function)

        return '{0}(n) = {1}'.format(self.name,
                                     latex(func))  # TODO: print the declarations of s_i = pi if they are found in inits as well.


class GeometricFunction(CompahFunction):
    def __init__(self, name, a=None, r=None):
        super().__init__(name)
        self.n = Symbol('n')
        if not a:
            a = Symbol('a')
        if not r:
            r = Symbol('r')
        self.default_function = a * (r ** self.n)


class QuadraticFunction(CompahFunction):
    def __init__(self, name, a=None, b=None, c=None):
        super().__init__(name)
        self.n = Symbol('n')
        if not a:
            a = Symbol('a')
        if not b:
            b = Symbol('b')
        if not c:
            c = Symbol('c')
        self.default_function = a * (self.n ** 2) + b * (self.n) + c


class ArithmeticFunction(CompahFunction):
    def __init__(self, name, s1=None, d=None):
        super().__init__(name)
        self.n = Symbol('n')
        if not s1:
            s1 = Symbol('s1')
        if not d:
            d = Symbol('d')
        self.default_function = s1 + d * (self.n - 1)


class Sequence(object):
    def __init__(self):
        self.function = None

    def get_function(self):
        if self.function:
            return self.function
        else:
            raise NotImplementedError


class GeometricSequence(Sequence):
    def __init__(self, a=None, r=None, name='f'):
        super().__init__()
        self.function = GeometricFunction(name, a, r)


class ArithmeticSequence(Sequence):
    def __init__(self, a1=None, d=None, name='f'):
        super().__init__()
        self.function = ArithmeticFunction(name, a1, d)


class QuadraticSequence(Sequence):
    def __init__(self, a=None, b=None, c=None, name='f'):
        super().__init__()
        self.function = QuadraticFunction(name, a, b, c)


class ConstantInterleavingSequence(Sequence):
    def __init__(self, k, sequence, name='f'):
        super().__init__()
        self.name = name
        self.constant = k
        self.function = sequence.get_function()

    def __str__(self):
        return '{0}(n) == {1} and {2}'.format(self.name, self.constant,
                                              self.function)  # TODO: print the declarations of s_i = pi if they are found in inits as well.


class SequenceInterleavingSequence(Sequence):
    def __init__(self, sequence1, sequence2, name='f'):
        super().__init__(name)
        self.first_seq = sequence1.get_function()
        self.sec_seq = sequence2.get_function()

    def __str__(self):
        return '{0}(n) == {1} and {2}'.format(self.name, self.constant,
                                              self.function)  # TODO: print the declarations of s_i = pi if they are found in inits as well.
