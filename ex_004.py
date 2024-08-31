'''Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de 
representação que cada estado teve dentro do valor total mensal da distribuidora. '''


ESTADOS = 5

# Lista com o faturamento mensal por estado
faturamento_mensal = [['SP', 67836.43], ['RJ', 36678.66], ['MG', 29229.88], ['ES', 27165.48], ['Outros', 19849.53]]

# Calcula o total do faturamento
total_faturamento = 0    
for i in range(ESTADOS):
    total_faturamento += faturamento_mensal[i][1]

# Calcula e exibe o percentual de cada estado
for dados_estado in faturamento_mensal:
    nome_estado = dados_estado[0]
    faturamento = dados_estado[1]

    percentual = (faturamento / total_faturamento) * 100

    print(f'{nome_estado} representa {percentual:.2f}% do faturamento total')


