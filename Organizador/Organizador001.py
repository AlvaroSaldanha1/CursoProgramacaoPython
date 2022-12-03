"""
Projeto: Organizador
Você tem dentro de uma pasta os seguintes arquivos:
• DespesasCorrentes.xlsx
• DespesasCorrentes.docx
• DespesasCapital.xlss
• DespesasCapital.docx
• relatorio.docx
Sua tarefa é organizar tais arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo.
Para executar sua tarefa, escreva um programa procedural e modularizado
em Python que crie as pastas e mova os arquivos para as devidas pastas.
No GitHub, crie um repositório denominado organizador e suba seu programa
para lá.
Observações:
1. N˜ao se esqueça de deixar seu repositório público, e
2. Use os pacotes OS e SHUTIL da biblioteca padr˜ao do Python para lhe
ajudar nesta tarefa.

Autor: Álvaro André Saldanha de Souza
Data: 03/12/2022
Versão: 0.0.1

"""

# Importação de módulos

import os
import shutil


# Definição de funções

def criar_pastas():
    if os.path.exists("documentos") == False:
        os.mkdir("documentos")
    if os.path.exists("planilhas") == False:
        os.mkdir("planilhas") 
        

def selecionar_mover():    
    arquivos = os.listdir()
    for arquivo in arquivos:
        if ".xlsx" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".docx" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")

            
def main():
    criar_pastas()
    selecionar_mover()

if __name__ == "__main__":
    main()



