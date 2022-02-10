from sympy import Symbol, Eq, Sum, FiniteSet, Function, oo
from sequences import ArithmeticSequence
from sympy.printing import latex

class Archetype:
    def __init__(self):
        self.premises = []
        self.solution = []
        self.seq = None

    def __str__(self):
        templ = """
(debug)
==Premises==
{0}
==Solution==
{1}\n
        """
        premises_str = "\n".join([latex(item) for item in self.premises])
        solution_str = self.solution.__str__()
        return templ.format(premises_str, solution_str)


class ArithmeticArchetypeOne(Archetype):
    def __init__(self, s1, s2, s3):
        super().__init__()
        # TODO: Make sure that s1, s2, and s3 are functions
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)

        self.seq = ArithmeticSequence(s1, s3 - s2, 's')
        self.solution = self.seq.get_function()


class ArithmeticArchetypeTwo(Archetype):
    def __init__(self, s1, s2, s3, i):
        super().__init__()
        # TODO: Make sure that s1, s2, and s3 are functions
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')
        i_symbol = Symbol('i')

        if i < 4:
            raise ValueError("ArithmeticArchetypeTwo only accepts i > 3. You entered i={0}".format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        prem4 = Eq(i_symbol, i)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)
        self.premises.append(prem4)

        self.seq = ArithmeticSequence(s1, s3 - s2, 's')
        self.solution = self.seq.get_function()(i)


class ArithmeticArchetypeThree(Archetype):
    def __init__(self, s1, s2, s3, n):
        super().__init__()
        # TODO: Make sure that s1, s2, and s3 are functions
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')

        if n < 4:
            raise ValueError("ArithmeticArchetypeThree only accepts n > 3. You entered n={0}".format(n))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)

        self.seq = ArithmeticSequence(s1, s3 - s2, 's')
        from sympy.abc import i
        self.solution = Sum(self.seq.get_function()(i), (i, 1, n)).doit()


class ArithmeticArchetypeFour(Archetype):
    def __init__(self, s1, s2, i):
        super().__init__()
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        i_symbol = Symbol('i')

        if i < 3:
            raise ValueError("ArithmeticArchetypeFour only accepts i > 2. You entered i={0}".format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(i_symbol, i)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        self.solution = self.seq.get_function()(i)


class ArithmeticArchetypeFive(Archetype):
    def __init__(self, s1, s2, sum_limit):
        super().__init__()
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        self.premises.append(prem1)
        self.premises.append(prem2)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        from sympy.abc import i
        n = 3
        while True:
            sum_eq = Sum(self.seq.get_function()(i), (i, 1, n))
            val = sum_eq.doit()
            if val > sum_limit:
                eq_eval = Eq(sum_eq, val)
                self.premises.append(eq_eval)
                break
            else:
                n = n + 1
        self.solution = Eq(Symbol('n'), n)


class ArithmeticArchetypeSix(Archetype):
    def __init__(self, s1, s2, si, i):
        super().__init__()
        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        si_symbol = Symbol('s{0}'.format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        premi = Eq(si_symbol, si)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(premi)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        self.solution = self.seq.get_function()


class ArithmeticArchetypeSeven(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        si = arg0[2]
        i = arg0[3]

        start = arg1[0]
        end = arg1[1]
        a = arg1[2]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        si_symbol = Symbol('s{0}'.format(i))
        start_symbol = Symbol('start')
        end_symbol = Symbol('end')
        alpha_symbol = Symbol('alpha')

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        premi = Eq(si_symbol, si)
        prem4 = Eq(start_symbol, start)
        prem5 = Eq(end_symbol, end)
        prem6 = Eq(alpha_symbol, a)

        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(premi)
        self.premises.append(prem4)
        self.premises.append(prem5)
        self.premises.append(prem6)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        x_s = []
        for i in range(start, end):
            x = self.seq.get_function()(i) % a
            x_s.append(x)
        self.solution = FiniteSet(*x_s)


class ArithmeticArchetypeEight(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        si = arg0[2]
        i = arg0[3]

        x = arg1[0]
        a = arg1[1]
        n = arg1[2]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        si_symbol = Symbol('s{0}'.format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        premi = Eq(si_symbol, si)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(premi)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')

        s_is = []
        index = 1
        while len(s_is) < n:
            if x == self.seq.get_function()(index) % a:
                s_is.append(x)
            index = index + 1

        from sympy.abc import i
        f = Function('s')
        s = Sum(f(i), (i, 1, n))
        self.solution = Eq(s, sum(s_is[:n]))


class ArithmeticArchetypeTen(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        si = arg0[2]
        i = arg0[3]

        a = arg1[0]
        b = arg1[1]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        si_symbol = Symbol('s{0}'.format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        premi = Eq(si_symbol, si)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(premi)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')

        indices = []
        index = 1
        while index <= i:
            # s_i % b == a |||||||   s_i == a (mod b)
            if a == self.seq.get_function()(index) % b:
                indices.append(index)
            index = index + 1
        l_sym = Symbol('l')
        self.solution = Eq(l_sym, len(indices))


class ArithmeticArchetypeEleven(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        s3 = arg0[2]
        siminus1 = arg0[3]
        si = arg0[4]
        sj = arg0[5]
        i = arg0[6]
        j = arg0[7]

        a = arg1[0]
        b = arg1[1]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')
        siminus1_symbol = Symbol('s{0}'.format(i-1))
        si_symbol = Symbol('s{0}'.format(i))
        sj_symbol = Symbol('s{0}'.format(j))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        premiminus1 = Eq(siminus1_symbol, siminus1)
        premi = Eq(si_symbol, si)
        premj = Eq(sj_symbol, sj)

        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)
        self.premises.append(premiminus1)
        self.premises.append(premi)
        self.premises.append(premj)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')

        indices = []
        index = 1
        while index <= j:
            # s_i % b == a |||||||   s_i == a (mod b)
            if a == self.seq.get_function()(index) % b:
                indices.append(index)
            index = index + 1
        l_sym = Symbol('l')
        self.solution = Eq(l_sym, len(indices))


class ArithmeticArchetypeTwelve(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        s3 = arg0[2]
        siminus1 = arg0[3]
        si = arg0[4]
        i = arg0[5]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')
        siminus1_symbol = Symbol('s{0}'.format(i-1))
        si_symbol = Symbol('s{0}'.format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        premiminus1 = Eq(siminus1_symbol, siminus1)
        premi = Eq(si_symbol, si)

        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)
        self.premises.append(premiminus1)
        self.premises.append(premi)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')

        l_sym = Symbol('i')
        self.solution = Eq(l_sym, i)


class ArithmeticArchetypeThirteen(Archetype):
    def __init__(self, arg0, arg1):
        super().__init__()
        s1 = arg0[0]
        s2 = arg0[1]
        s3 = arg0[2]
        siminus1 = arg0[3]
        si = arg0[4]
        i = arg0[5]

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')
        siminus1_symbol = Symbol('s{0}'.format(i-1))
        si_symbol = Symbol('s{0}'.format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        premiminus1 = Eq(siminus1_symbol, siminus1)
        premi = Eq(si_symbol, si)

        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)
        self.premises.append(premiminus1)
        self.premises.append(premi)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')

        from sympy.abc import k
        sum_eq = Sum(self.seq.get_function()(k), (k, 1, i))
        neg_vals = []
        for i in range(1, i+1):
            if self.seq.get_function()(i) < 0:
                neg_vals.append(self.seq.get_function()(i))
        self.solution = Eq(sum_eq, sum(neg_vals))


class ArithmeticArchetypeFourteen(Archetype):
    def __init__(self, s1, s2, s3, total):
        super().__init__()

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)

        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        n = 2
        from sympy.abc import i
        while True:
            sum_eq = Sum(self.seq.get_function()(i), (i, 1, n))
            print('Testing ', n, sum_eq.doit())
            if sum_eq.doit() == total:
                break
            elif abs(sum_eq.doit()) > abs(total):
                raise ValueError('Arithmetic sequence {0}, {1}, {2}, ... cannot be summed up, starting at index 1, '
                                 'to produce total = {3}'.format(s1, s2, s3, total))
            n = n + 1

        self.solution = Eq(Symbol('n'), n)


class ArithmeticArchetypeFifteen(Archetype):
    def __init__(self, s1, s4):
        super().__init__()

        s1_symbol = Symbol('s1')
        s2_symbol = Symbol('s2')
        s3_symbol = Symbol('s3')
        s4_symbol = Symbol('s4')

        eq1 = Eq(s4-s3_symbol - (s3_symbol-s2_symbol), 0)
        eq2 = Eq(s3_symbol-s2_symbol - (s2_symbol-s1), 0)

        from sympy import solve
        answer = solve([eq1, eq2], (s2_symbol, s3_symbol))
        s2 = answer[s2_symbol]
        s3 = answer[s3_symbol]

        prem1 = Eq(s1_symbol, s1)
        prem4 = Eq(s4_symbol, s4)

        self.premises.append(prem1)
        self.premises.append(prem4)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        self.solution = [Eq(s2_symbol, s2), Eq(s3_symbol, s3)]

