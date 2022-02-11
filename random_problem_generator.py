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
            archetype = ArithmeticArchetypeThree(f1, f2, f3, n)
        elif number == 4:
            s1 = randint(1, 20)
            s2 = randint(1, 20)
            i = randint(3, 100)
            archetype = ArithmeticArchetypeFour(s1, s2, i)
        elif number == 5:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            sum_to_n = randint(2*s2, 5*s2)
            archetype = ArithmeticArchetypeFive(s1, s2, sum_to_n)
        elif number == 6:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2-s1)
            i = randint(3, 50)
            si = seq.get_function()(i)
            archetype = ArithmeticArchetypeSix(s1, s2, si, i)
        elif number == 7:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2-s1)
            i = randint(3, 50)
            si = seq.get_function()(i)
            arg0 = (s1, s2, si, i)

            start = 1
            end = randint(2, 50)
            mod_a = choice([2, 5, 10, 15, 20, 25])
            arg1 = (start, end, mod_a)

            archetype = ArithmeticArchetypeSeven(arg0, arg1)
        elif number == 8:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2-s1)
            i = randint(3, 50)
            si = seq.get_function()(i)
            arg0 = (s1, s2, si, i)

            x = randint(s1,4*s1)
            a = choice([2, 5, 10, 15, 20, 25])
            n = randint(5, 50)
            arg1 = (x, a, n)

            archetype = ArithmeticArchetypeSeven(arg0, arg1)
        elif number == 9:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            k = randint(5, 50)
            sk = seq.get_function()(k)
            archetype = ArithmeticArchetypeNine(s1, s2, sk, k)
        elif number == 10:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            i = randint(4, 20)
            si = seq.get_function()(i)
            arg0 = (s1, s2, si, i)

            a = randint(2, 10) # remainder
            b = randint(2, 10) # divider
            arg1 = (a, b)

            archetype = ArithmeticArchetypeTen(arg0, arg1)
        elif number == 11:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            s3 = s2 + (s2-s1)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            i = randint(4, 20)
            siminus1 = seq.get_function()(i-1)
            si = seq.get_function()(i)
            j = randint(i+1, 40)
            sj = seq.get_function()(j)
            arg0 = (s1, s2, s3, siminus1, si, sj, i, j)

            a = randint(2, 10) # remainder
            b = randint(2, 10) # divider
            arg1 = (a, b)

            archetype = ArithmeticArchetypeEleven(arg0, arg1)
        elif number == 12:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            s3 = s2 + (s2-s1)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            i = randint(4, 20)
            siminus1 = seq.get_function()(i-1)
            si = seq.get_function()(i)
            arg0 = (s1, s2, s3, siminus1, si, i)
            archetype = ArithmeticArchetypeTwelve(arg0)
        elif number == 13:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            s3 = s2 + (s2-s1)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            i = randint(4, 20)
            siminus1 = seq.get_function()(i-1)
            si = seq.get_function()(i)
            arg0 = (s1, s2, s3, siminus1, si, i)
            archetype = ArithmeticArchetypeThirteen(arg0)
        elif number == 14:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            s3 = s2 + (s2-s1)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1)
            n = randint(4, 50)
            total = s1 + s2 + s3
            index = 4
            while index <= n:
                total = total + seq.get_function()(index)
                index = index + 1
            archetype = ArithmeticArchetypeFourteen(s1, s2, s3, total)
        elif number == 15:
            s1 = randint(1, 10)
            s2 = randint(11, 20)
            from sequences import ArithmeticSequence
            seq = ArithmeticSequence(s1, s2 - s1, 's')
            s4 = seq.get_function()(4)
            archetype = ArithmeticArchetypeFifteen(s1, s4)
        # TODO: building random problem for other archetypes
        return archetype
