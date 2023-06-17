from random import randint

#Exemplo 1
n_par = 0
n_impar = 0
lista_num = []
for i in range(100):
    num_aleatorio = randint(0, 1000)
    if (num_aleatorio % 2) == 0:
        n_par += 1
    else:
        n_impar += 1
    print(f'O numero escolhido foi: {num_aleatorio}')
    lista_num.append(num_aleatorio)


print(lista_num)
print(f'Esta lista tem {n_par} números pares e '
          f'{n_impar} impares')

#Contadores
n_impar = 0
n_par = 0

for j in lista_num:
    if (j % 2) == 0:
        n_par += 1
    else:
        n_impar += 1

print(f'Esta lista tem {n_par} números pares e '
      f'{n_impar} impares')