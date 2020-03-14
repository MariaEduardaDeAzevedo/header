#!/usr/bin/python3
#coding: utf-8

"""
Header


Pessione q para sair

O Header é uma aplicação desenvolvida em Python para 
ser utilizada na linha de comando. Sua finalidade é 
importar um cabeçalho, previamente salvo em um arquivo,
em um outro arquivo de destino.
Esta aplicação foi pensada para facilitar a escrita de 
cabeçalhos padronizados em programas ou até em outros 
arquivos. Nos comandos abaixo, os arquivos estão dados
como .txt, mas podem ser outras extensões desejadas.

1. Iniciando no Header.

    1.1 Para utilizar esta ferramenta, clone este repositório!
    Após isso, vá até o diretório clonado no seu computador e 
    execute o arquivo header.py:

    python3 header.py 

    1.2 Se você acabou de iniciar verá a seguinte mensagem:

    Olá! Bem-vindo ao Header!
    Status do Header: não iniciado
    Comando para importar um cabeçalho em um arquivo:
    python header.py w < caminho_do_cabeçalho > < caminho_do_arquivo >

    1.3 Então execute o comando:

    python3 header.py init

    1.4 Pronto! O Header está pronto para ser utilizado!

2. Comandos

    2.1 Importar qualquer arquivo:

    python3 header.py w < caminho_do_cabeçalho > < caminho_do_arquivo >

    2.2 Salvar um arquivo de cabeçalho na sua biblioteca de cabeçalhos:

    python3 header.py s < caminho_do_cabeçalho >

    2.3 Criar um arquivo de cabeçalho direto na sua biblioteca de cabeçalhos:

    python3 header.py c nome_do_arquivo.txt

    2.4 Importar um cabeçalho de sua biblioteca em um arquivo:

    python3 header.py ws nome_do_cabecalho_.txt < caminho_do_arquivo >

    2.5 Listar os arquivos salvos em sua biblioteca:

    python3 header.py list

    2.6 Editar um arquivo salvo em sua biblioteca:

    python3 header.py e nome_do_arquivo.txt

    2.7 Obter ajuda para utilizar a ferramenta:

    python3 header.py help 
"""

import sys
import os.path
import shutil
import functions

__author__ = "Maria Eduarda de Azevedo"
__version__ = "1.0"
__maintainer__ = "Maria Eduarda de Azevedo"
__email__ = "maria.silva@ccc.ufcg.edu.br"

arg = sys.argv
directory = os.path.dirname(os.path.realpath(__file__))
config = open(".config.txt", "r")
status = True if config.readlines()[0] == "init" else False

if len(arg) == 1:
    print("\033[1;33mOlá! Bem-vindo ao Header!\033[0;0m")
    print("\033[1;32mStatus do Header: iniciado\033[0;0m" if status == True else "\033[1;31mStatus do Header: não iniciado\033[0;0m")
    print("\033[1;32mPara obter ajuda no uso da ferramenta, digite:\033[0;0m")
    print("python3 header.py help")
else:
    arg.pop(0)

if status and arg[0].lower() == "w":
    print(functions.write(arg))
elif status and arg[0].lower() == "ws":
    print(functions.write_save(arg, directory))
elif status and arg[0].lower() == "s":
    print(functions.save(arg, directory))
elif status and arg[0].lower() == "c":
    print(functions.create(arg, directory))
elif not status and arg[0].lower() == "init":
    print(functions.init())
elif status and arg[0].lower() == "list":
    list_ws(functions.directory)
elif status and arg[0].lower() == "e":
    print(functions.edit(arg, directory))
elif arg[0].lower() == "help":
    help("header")

config.close()
