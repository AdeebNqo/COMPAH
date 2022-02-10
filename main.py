from sequences import *
from problem_archetypes import *
from random_problem_generator import RandomProblemGenerator
from random_template_chooser import TemplateChooser


def test():
    rg = RandomProblemGenerator()
    arch_num = 9

    p = rg.get_archetype(arch_num)
    tc = TemplateChooser(arch_num, p)

    print(tc.get_p_text())
    print(tc.get_q_text())


if __name__ == '__main__':
    test()
