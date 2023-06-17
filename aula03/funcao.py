def soma(paramentro1, paramentro2):
    return(paramentro1 + paramentro2)
print(soma(2,4))

def calculadora(n1, n2):
    resultado_soma = n1 + n2
    resultado_subtracao = n1 - n2
    resultado_multplicacao = n1 * n2
    resultado_divisao = n1 / n2

    return resultado_soma, resultado_subtracao, resultado_multplicacao, resultado_divisao

# print(calculadora(20, 10))
soma, subtracao, multiplicacao, divisao = calculadora(10, 20)
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplição: {multiplicacao}')
print(f'Divisão: {divisao}')

def soma(*args):
    print(f'O tipo é {type(args)}')
    print(f'A tupla é {args}')
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)
soma(1, 2, 3, 4, 5, 6, 7, 8, 9)

def dicionario(**kwargs):
    print(f'O tipo de Kwargs é {type(kwargs)}')
    print(f'{kwargs}')

    for i in kwargs:
        print(kwargs[i])

dicionario(nome = 'Messias', idade = 36, clube = 'Vasco')


