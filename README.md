	# Computer Assistant for High School Mathematics (COMPAH)

	This is the collection of resources created in order to build the computer assistant for generating mathematics problems

# How to use current python code to generate problem

The `main.py` file shows how to generate a problem. Suppose you wanted to generate problem that abides by the archetype identifier 10. Then you would write code that looks like the following:


```
def generate_problem(archetype_id):
    rg = RandomProblemGenerator()
    

    p = rg.get_archetype(arch_num)
    tc = TemplateChooser(arch_num, p)

    return tc.get_p_text(), tc.get_q_text()


if __name__ == '__main__':
	arch_num = 10
    premise, question = generate(arch_num)
    print (premise)
    print (question)
```

# Citation

Related paper with the theory, design and evaluation of the current prototype: Mahlaza, Z. Towards an automated assistant for generating mathematics problems. Proceedings of the 51st Annual Conference of the Southern African Computer Lecturers’ Association (SACLA 2022). Springer (in print). July 21-22, 2022, Cape Town, South Africa.
