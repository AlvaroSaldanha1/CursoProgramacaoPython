"""
Programa soma
Requisito: Este porograma pega dois números digitados pelo
usuário e calcula o produto dele e coloca o resultado na tela,
com frase que explique o que é o resultado obtido.
Autor: Álvaro
Versão: 0.0.1
Data 26/11/2022)
"""


# Entrada
numero_1 = float ( input( "\nDigite o primeiro fator:  "))

numero_2 = float (input( "\nDigite o segundo fator:  "))


# Processamento

produto = (numero_1 * numero_2)


# Saída

print ("\nEste programa calcula o produto de dois números dados pelo usuário.")
print (f"\nO produto dos números {numero_1} e {numero_2} é igual a {produto}.")
