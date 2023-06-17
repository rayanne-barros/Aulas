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

print(professores)