from sequences import *
from problem_archetypes import *

def test():
    x_sym = Symbol('x')
    s1 = 10
    s2 = 6
    s3 = 2

    templ = ArithmeticArchetypeFourteen(s1, s2, s3, -560)
    print(templ)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
