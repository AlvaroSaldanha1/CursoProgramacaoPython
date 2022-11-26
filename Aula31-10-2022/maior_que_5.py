"""

Requisito: ler qualquer número e dizer se é maior que 5.

Autor: Álvaro
Data: 26/10/2022
Versão: 0.0.1
"""

# Entrada

numero = float(input("\nDigite um número real: "))



# Processamento

if numero > 5:
    frase = f"O número {numero} é maior que 5."
elif numero == 5:
    frase = f"O número {numero} é igual a 5."
else:
    frase = f"O número {numero} é menor que 5."
    
    


# Saída

print(frase)
