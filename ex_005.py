'''Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse'''

# Solicita ao usuário uma entrada
string = input('Informe uma palavra ou frase: ').lower().strip()

# Inicializa uma variável vazia para armazenar a string invertida
string_invertida = ''

# Loop para percorrer cada caractere da string original do final para o início
for caractere in string:
    string_invertida = caractere + string_invertida

# Exibe o resultado
print(f'Sua palavra / frase de trás para frente é: {string_invertida}')

