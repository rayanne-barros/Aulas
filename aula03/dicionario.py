professor = {
    'nome': 'Messias',
    'idade': 36
}

aluno = {
    'nome': 'Rayanne',
    'idade': 28
}

print(professor['nome'])
print(professor['idade'])

professor['nome'] = 'Messias Batista'
print(professor)

print(aluno['nome'])
print(aluno['idade'])

# professores = {
#     1: {'nome' : 'Messias', 'idade' : 36},
#     2: {'nome' : 'Wuldson', 'idade' : 53}
# }

professores = {
    'Messias': {
        'idade': 36,
        'disciplinas': ['Introdução', 'Java']},
    'Wuldson': {
        'idade' : 53,
        'disciplinas': ['BD I', 'BD II']}
}

# print(professores)

print(f'O professor Messias tem {professores["Messias"]["idade"]}'
      f' anos, e ministra as disciplinas'
      f' de: {professores["Messias"]["disciplinas"][0]} e {professores["Messias"]["disciplinas"][1]}.')

professores['Messias']['email'] = 'mrafaelbatista@gmail.com'
professores['Messias']['cpf'] = '000.000.000-00'

print(professores['Messias'])

del professores['Messias']['cpf']
print(professores['Messias'])
