'''Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json
from random import uniform, randint

# Define constantes
CAMINHO_JSON = 'dados.json'

# Inicializa variaveis
total_faturamento = 0
dias_com_faturamento = 0
menor_valor = None
maior_valor = None
qnt_dias_maior_media = 0

def escrever_json_faturamento():
    '''Cria um arquivo JSON com os dados de faturamento. '''
    lista_dias = []
    for i in range(randint(28,31)): 
        dia = {'dia': f'{i+1}', 'valor': round(uniform(0, 1500.99), 2)}
        lista_dias.append(dia)

    with open('dados.json', 'w') as file:
        json.dump(lista_dias, file, indent=4)

def ler_json(arquivo):  
    '''Lê o arquivo JSON e retorna o conteudo dele'''
    with open('dados.json') as arquivo:
        return json.load(arquivo)

def verifica_se_faturou(valor):
    '''Verifica a quantidade de dias com faturamento e calcula o faturamento total'''
    global total_faturamento, dias_com_faturamento
    if valor != 0:
        total_faturamento += valor
        dias_com_faturamento += 1

def verifica_menor_valor(valor):
    '''Identifica o menor faturamento do mes'''        
    global menor_valor    
    if menor_valor is None or valor < menor_valor:
        menor_valor = valor

def verifica_maior_valor(valor): 
    '''Identifica o maior faturamento do mes'''     
    global maior_valor    
    if maior_valor is None or valor > maior_valor:
        maior_valor = valor

def contar_dias_maior_media():
    '''Identifica a quantidade de dias com faturamento maior que a média'''
    global qnt_dias_maior_media
    for dados_dia in lista_faturamento:
        if dados_dia['valor'] > media:
            qnt_dias_maior_media += 1


# Lista com faturamento baseado no arquivo JSON
lista_faturamento = ler_json(CAMINHO_JSON)

# Calcula o total de faturamento, menor valor e maior valor
for i in range(len(lista_faturamento)):
    valor = lista_faturamento[i]['valor']

    verifica_se_faturou(valor)
    verifica_menor_valor(valor)
    verifica_maior_valor(valor)

# Calcula a média dos dias com faturamento
media = total_faturamento / dias_com_faturamento

contar_dias_maior_media()

# Exibe os resultados
print(f'Menor valor de faturamento: R${menor_valor:.2f}')
print(f'Maior valor de faturamento: R${maior_valor:.2f}')
print(f'Número de dias com faturamento superior à média: {qnt_dias_maior_media}')

        


