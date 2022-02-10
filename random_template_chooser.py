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
        self.seq_template_filename = 'templates/arithmetic-sequences-archetype{0}'.format(number)
        self.ser_template_filename = 'templates/arithmetic-series-archetype{0}'.format(number)
        self.seq_premise_template_filename = 'templates/arithmetic-sequences-premise'
        self.ser_premise_template_filename = 'templates/arithmetic-series-premise'

    # Retrieves the premise text
    def get_p_text(self):
        premise = None
        seq_templates = get_templates(self.seq_premise_template_filename)
        ser_templates = get_templates(self.ser_premise_template_filename)
        if self.number == 1:
            chosen_template = choice(seq_templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 2 or self.number == 3:
            chosen_template = choice(seq_templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises[:3]]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 4 or self.number == 5:
            chosen_template = choice(seq_templates)
            funcs = [latex(seq_item.rhs) for seq_item in self.archetype.premises[:2]]
            seq = ', '.join(funcs)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 6 or self.number == 7:
            chosen_template = choice(seq_templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            si = self.archetype.premises[2].rhs
            seq = '{0}, {1}, ..., {2}, '.format(s1, s2, si)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 8:
            chosen_template = choice(seq_templates[:3])
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            si = self.archetype.premises[2].rhs
            seq = '{0}, {1}, ..., {2} '.format(s1, s2, si)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 10:
            chosen_template = choice(ser_templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            si = self.archetype.premises[2].rhs
            seq = '{0} + {1} + ... + {2} '.format(s1, s2, si)
            premise = chosen_template.substitute(series=seq).strip()
        elif self.number == 11:
            chosen_template = choice(seq_templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            s3 = self.archetype.premises[2].rhs
            premiminus1 = self.archetype.premises[3].rhs
            premi = self.archetype.premises[4].rhs
            premj = self.archetype.premises[5].rhs
            seq = '{0}, {1}, {2}, ... {2}, {3}, ..., {4}'.format(s1, s2, s3, premiminus1, premi, premj)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 12 or self.number == 13:
            chosen_template = choice(seq_templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            s3 = self.archetype.premises[2].rhs
            premiminus1 = self.archetype.premises[3].rhs
            premi = self.archetype.premises[4].rhs
            seq = '{0}, {1}, {2}, ... {2}, {3}'.format(s1, s2, s3, premiminus1, premi)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 14:
            chosen_template = choice(seq_templates)
            s1 = self.archetype.premises[0].rhs
            s2 = self.archetype.premises[1].rhs
            s3 = self.archetype.premises[2].rhs
            seq = '{0}, {1}, {2}'.format(s1, s2, s3)
            premise = chosen_template.substitute(sequence=seq).strip()
        elif self.number == 15:
            chosen_template = choice(seq_templates)
            s1 = self.archetype.premises[0].rhs
            s4 = self.archetype.premises[1].rhs
            seq = 's1={0}, ...,  s4={1}'.format(s1, s4)
            premise = chosen_template.substitute(sequence=seq).strip()
        return premise

    # Retrieves the question text
    def get_q_text(self):
        question = None
        templates = get_templates(self.seq_template_filename)
        if self.number == 1 or self.number == 6 or self.number == 9 or self.number == 13:
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
        elif self.number == 8:
            chosen_template = choice(templates)
            a = self.archetype.premises[3].rhs
            question = chosen_template.substitute({
                'divider': a
            }).strip()
        elif self.number == 10:
            chosen_template = choice(templates)
            b = self.archetype.premises[3].rhs
            question = chosen_template.substitute({
                'divider': b
            }).strip()
        elif self.number == 11:
            chosen_template = choice(templates)
            b = self.archetype.premises[6].rhs
            question = chosen_template.substitute({
                'divider': b
            }).strip()
        elif self.number == 12:
            chosen_template = choice(templates)
            si = self.archetype.premises[4].rhs
            question = chosen_template.substitute({
                'value': si
            }).strip()
        elif self.number == 14:
            chosen_template = choice(templates)
            number = self.archetype.solution.rhs
            total = self.archetype.premises[3].rhs
            question = chosen_template.substitute({
                'number': number,
                'sum': total
            }).strip()
        elif self.number == 15:
            chosen_template = choice(templates)
            s2 = self.archetype.solution[0].lhs
            s3 = self.archetype.solution[1].lhs
            question = chosen_template.substitute({
                'item2': s2,
                'item3': s3
            }).strip()
        return question
