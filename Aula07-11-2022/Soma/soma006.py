"""
Programa soma
Requisito: Este programa pega dois números digitados pelo
usuário, calcula o seu produto e coloca o resultado na tela,
com uma frase que explique o que é o resultado obtido.
Autor: Álvaro
Data: 07/11/2022
Versão: 0.0.5

"""

# Definição de funções

def entrada():
    numero_1 = (input ("Digite a primeira parcela:"))
    if isinstance(float, numero_1) float):
        numero_1 = float (numero_1)
    numero_2 = (input ("Digite a segunda parcela:"))
    if isinstance(numero_2, float)
        numero_2 = float(numero_2)
    
    return [numero_1, numero_2]
    
def soma(x, y):
        return x + y

# Entrada


lista_valores = entrada()


#Processamento



valor = soma (lista_valores [0], lista_valores[1])


# Saída

print (f"A soma dos números {lista_valores [0]} e {lista_valores [1]} é igual a  {valor}")

  
    
