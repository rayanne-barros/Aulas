from random import randint

#Exemplo 2
while True:
    nome = input('Digite seu nome: ')
    if nome.upper() == 'seu nome'.upper():
        break

#Exemplo 3

lista_num = []
controle = 0

while controle < 100:
    numero_aleatorio = randint(0, 1000)
    print(f'O número escolhido foi: {numero_aleatorio}')
    lista_num.append(numero_aleatorio)
    controle += 1
print(lista_num)

