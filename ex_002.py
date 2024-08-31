'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

# Solicita uma entrada ao usuário
entrada = int(input('Informe um número para verificação: '))

# Inicializa os dois primeiros termos da sequência
termo1, termo2 = 0, 1

# Lista para armazenar os termos da sequência
lista_numeros_fibonacci = [termo1, termo2]

# Laço while para gerar termos da sequência até que exceda o valor de entrada
while termo2 <= entrada:
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    
    lista_numeros_fibonacci.append(termo2)

# Condição que informa se o número está ou não na sequência
if entrada in lista_numeros_fibonacci:
    print(f'O número {entrada} pertence à sequência de Fibonacci.')
else:
    print(f'O número {entrada} não pertence à sequência de Fibonacci.')

# Exibe a sequência completa
print('\nSequência de Fibonacci:')
print(lista_numeros_fibonacci)
 