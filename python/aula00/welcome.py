message = """
Caro {},
Bem -vindo á disciplina de FP e ao curso {}

Cumprimentos,

Os Profes de FP
"""

name = input("Como te chamas?")
course = input("Qual é o teu curso?")

print(message.format(name,course))