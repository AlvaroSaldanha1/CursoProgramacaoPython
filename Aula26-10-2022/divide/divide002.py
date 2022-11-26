"""
Programa divide
Requisito: Crie um programa que leia dois números inteiros
do teclado, calcule a razão entre o primeiro e o segundo e
escreva na tela o resultado
Autor: Álvaro
Data: 26/10/2022
Versão: 0.0.2


"""
# Entrada

print ("Este programa calcula a razão entre dois números dados pelo usuário")

numerador = float(input ("\nDigite o numerador:"))
denominador = float(input ("\nDigite o denominador:"))


#Processamento

razao = numerador / denominador


# Saída

print (f"\nA razão entre os números {numerador} e {denominador} é igual a  {razao}.")
