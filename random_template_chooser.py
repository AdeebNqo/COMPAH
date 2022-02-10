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
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 2 or self.number == 3:
            chosen_template = choice(templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises[:3]]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 4 or self.number == 5:
            chosen_template = choice(templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises[:2]]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 6 or self.number == 7:
            chosen_template = choice(templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            si = self.archetype.premises[2].rhs
            seq = '{0}, {1}, ..., {2}, '.format(s1, s2, si)
            premise = chosen_template.substitute(sequence=seq).strip()
        return premise

    # Retrieves the question text
    def get_q_text(self):
        question = None
        templates = get_templates(self.template_filename)
        if self.number == 1 or self.number == 6:
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
            sol = latex(self.archetype.solution)
            question = chosen_template.safe_substitute(
                {
                    'number': 'n',
                    'sum': sol
                }
            )
        elif self.number == 4:
            chosen_template = choice(templates)
            i = self.archetype.premises[2].rhs
            question = chosen_template.safe_substitute(
                {
                    'seqItemLabel': 's_{}'.format(i),
                }
            )
        elif self.number == 5:
            chosen_template = choice(templates)
            n_val = self.archetype.premises[2].rhs
            question = chosen_template.safe_substitute(
                {
                    'number': 'n',
                    'sum': n_val
                }
            )
        elif self.number == 7:
            chosen_template = choice(templates)
            start = self.archetype.premises[3].rhs
            end = self.archetype.premises[4].rhs
            number = end - start
            alpha = self.archetype.premises[5].rhs
            question = chosen_template.substitute({
                'number': number,
                'divider': alpha
            }).strip()
        return question
