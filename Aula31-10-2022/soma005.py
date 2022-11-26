"""
Programa soma
Requisito (problema que o programa resolve):
Ler 4 números reais digitados pelo usuário, calcula a sua soma e
colocar o resultado na tela.

Autor: Álvaro
Data: 26/10/2022
Versão: 0.0.5

"""
# Entrada e Processamento de dados

i = 0 # contador
soma = 0

while i < 4:
    numero = float(input("\nDigite a parcela "))
    soma = soma + numero # acumulador
    i = i + 1



# Saída de dados

print (f"A soma dos números digitados é igual a {soma}")

