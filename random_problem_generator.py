from problem_archetypes import *
from random import *
from sympy import Symbol


class RandomProblemGenerator(object):
    def get_archetype(self, number):
        archetype = None
        if number == 1:
            x_var = Symbol('x')
            f1 = randint(1, 20) * x_var + randint(-20, 20)
            f2 = randint(1, 20) * x_var + randint(-20, 20)
            f3 = randint(1, 20) * x_var + randint(-20, 20)
            archetype = ArithmeticArchetypeOne(f1, f2, f3)
        elif number == 2:
            x_var = Symbol('x')
            f1 = randint(1, 20) * x_var + randint(-20, 20)
            f2 = randint(1, 20) * x_var + randint(-20, 20)
            f3 = randint(1, 20) * x_var + randint(-20, 20)
            i = randint(4, 50)
            archetype = ArithmeticArchetypeTwo(f1, f2, f3, i)
        elif number == 3:
            x_var = Symbol('x')
            f1 = randint(1, 20) * x_var + randint(-20, 20)
            f2 = randint(1, 20) * x_var + randint(-20, 20)
            f3 = randint(1, 20) * x_var + randint(-20, 20)
            n = randint(4, 50)
            archetype = ArithmeticArchetypeTwo(f1, f2, f3, n)
        # TODO: building random problem for other archetypes
        return archetype
