# Definição de funções

def entrada():
    """Entrada de dados"""
    soma = 0
    i = 0
    x = [1,7,15,31]
    return [soma, i, x]

# Processamento  de  dados

def calcula_media (soma, i, x):
    """Processamento de dados"""
    while i < len(x):
        soma = soma + x [i]
        i+=1
        media = soma/len(x)
    return media
    x=media


def saida():
    """Saida  de  dados"""
    
    print(f'A media dos números é igual a {x}.')

def main():
    valores = entrada()
    calcula_media(valores[0], valores[1], valores[2])
    saida()

# Execução da função principal

main()
