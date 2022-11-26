"""
Programa soma
Requisito (problema que o programa resolve):
Ler números reais digitados pelo usuário, calcular a sua soma e
colocar o resultado na tela.

Autor: Álvaro
Data: 26/10/2022
Versão: 0.0.6

"""
# Entrada e Processamento de dados


soma = 0

while True:
    numero = (input("\nDigite a parcela ou tecla X para interromper: "))
    if numero == "X":
        break
    soma = soma + float (numero) # acumulador
    



# Saída de dados

print (f"\nA soma dos números digitados é igual a {soma}")

