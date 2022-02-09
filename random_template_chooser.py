from string import Template
from random import *
from sympy.printing import latex


def get_templates(filename):
    lines = open(filename, 'r').readlines()
    templates = [
        Template(line) for line in lines
    ]
    return templates


# Source: https://stackoverflow.com/a/50992575
def get_ordinal(n):
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


class TemplateChooser(object):
    def __init__(self, number, archetype):
        self.archetype = archetype
        self.number = number
        self.template_filename = 'templates/arithmetic-sequences-archetype{0}'.format(number)
        self.premise_template_filename = 'templates/arithmetic-sequences-premise'

    # Retrieves the premise text
    def get_p_text(self):
        premise = None
        templates = get_templates(self.premise_template_filename)
        if self.number == 1:
            chosen_template = choice(templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq)
        elif self.number == 2:
            chosen_template = choice(templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises[:3]]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq)
        return premise.strip()

    # Retrieves the question text
    def get_q_text(self):
        question = None
        templates = get_templates(self.template_filename)
        if self.number == 1:
            question = choice(templates).substitute()
        elif self.number == 2:
            chosen_template = choice(templates)
            i = self.archetype.premises[3].rhs
            question = chosen_template.safe_substitute(
                {
                    'seqItemLabel': 's_{}'.format(i),
                    'ordinal': get_ordinal(i)
                }
            )
        elif self.number == 3:
            chosen_template = choice(templates)
            # i = self.archetype.premises[3].rhs
            # question = chosen_template.safe_substitute(
            #     {
            #         'number': 's_{}'.format(i),
            #         'sum': get_ordinal(i)
            #     }
            # )
        return question
