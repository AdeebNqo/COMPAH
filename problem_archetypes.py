from sympy import Symbol, Eq, Sum, FiniteSet, Function
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

        if i < 4:
            raise ValueError("ArithmeticArchetypeTwo only accepts i > 3. You entered i={0}".format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        prem3 = Eq(s3_symbol, s3)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(prem3)

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

        if i < 3:
            raise ValueError("ArithmeticArchetypeFour only accepts i > 2. You entered i={0}".format(i))

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        self.premises.append(prem1)
        self.premises.append(prem2)

        self.seq = ArithmeticSequence(s1, s2 - s1, 's')
        self.solution = self.seq.get_function()(i)


class ArithmeticArchetypeFive(Archetype):
    def __init__(self, s1, s2, sum):
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
            val = Sum(self.seq.get_function()(i), (i, 1, n)).doit()
            if sum == val:
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

        prem1 = Eq(s1_symbol, s1)
        prem2 = Eq(s2_symbol, s2)
        premi = Eq(si_symbol, si)
        self.premises.append(prem1)
        self.premises.append(prem2)
        self.premises.append(premi)

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

