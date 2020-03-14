#coding: utf-8
import sys
import os.path
import shutil

'''
Módulo com as funcionalidades do Header.

Este módulo apresenta todas as funcionalidades da
ferramenta Header.
'''

__author__ = "Maria Eduarda de Azevedo"
__version__ = "1.0"
__maintainer__ = "Maria Eduarda de Azevedo"
__email__ = "maria.silva@ccc.ufcg.edu.br"

def write(arg):
    '''
    Função que importa o conteúdo de um arquivo fonte para
    um arquivo de destino partindo dos caminhos dos mesmos.
    '''
    path_in = arg[1].split("/")
    file_name_in = path_in.pop(-1)
    path_out = arg[2].split("/")
    file_name_out = path_out.pop(-1)

    if file_name_in not in os.listdir(os.path.expanduser("~/") + "/" + "/".join(path_in)):
        return arg[1] + " não é um caminho válido ou " + file_name_in + " não existe no diretório."
    elif file_name_out not in os.listdir(os.path.expanduser("~/") + "/" + "/".join(path_out)):
        choice = input(arg[1] + " não é um caminho válido ou " + file_name_in + " não existe no diretório. Deseja criá-lo? [S/N]")
        if choice.lower() == "n":
            return "Tente novamente passando um caminho válido."

    header = open(os.path.expanduser("~/") + arg[1], "r")
    file_ = open(os.path.expanduser("~/") + arg[2], "a")

    for line in header.read():
        file_.writelines(line)
    
    header.close()
    file_.close()
    return "Conteúdo de " + arg[1] + " importado em " + arg[2]

def write_save(arg, directory):
    '''
    Função que importa o conteúdo de um arquivo fonte salvo
    em na biblioteca de cabeçalhos para um arquivo de destino 
    no qual é informado o caminho.
    '''
    if arg[2].split("/")[-1] not in os.listdir(os.path.expanduser("~/") + arg[2].split("/").pop(-1).join("/")):
        choice = input(arg[2].split("/")[-1] + " não existe no diretório informado, deseja criar? [S/N] ")
        if choice.lower() == "n":
            return "Tente novamente passando um caminho válido."

    header = open(directory + "/headers/" + arg[1], "r")
    file_ = open(os.path.expanduser("~/") + arg[2], "a")

    for line in header.read():
        file_.writelines(line)
    
    header.close()
    file_.close()
    return ("Conteúdo de " + arg[1] + " importado em " + arg[2])

def save(arg, directory):
    '''
    Salva um arquivo do sistema como um arquivo de sua biblioteca
    partindo do caminho do mesmo.
    '''
    file_ = os.path.expanduser("~/") + "/" + arg[1]
    open(directory + "/headers/" + file_.split("/")[-1], "w")
    shutil.copyfile(os.path.expanduser("~/") + arg[1], directory + "/headers/" + file_.split("/")[-1])
    return (file_.split("/")[-1] + " salvo em sua biblioteca de cabeçalhos")

def create(arg, directory):
    '''
    Cria um arquivo de cabeçalho diretamente na sua biblioteca.
    Ao criar o arquivo, abre-se o editor VIM para a edição de
    seu conteúdo.
    '''
    if arg[1] in os.listdir(directory + "/headers"):
        return "Já existe um cabeçalho salvo com esse nome!"
    open(directory + "/headers/" + arg[1], "w")
    os.system("/usr/bin/vim " + directory + "/headers/" + arg[1])
    return arg[1] + "criado e salvo na sua biblioteca de cabeçalhos."

def list_ws(directory):
    '''
    Lista todos os arquivos de cabeçalho da biblioteca.
    '''
    for f in os.listdir(directory + "/headers"):
        print("\033[1;34m" + f + "\033[0;0m")

def edit(arg, directory):
    '''
    Edita um arquivo da biblioteca indicado pelo nome.
    '''
    if arg[1] not in os.listdir(directory + "/headers"):
        return arg[1] + " não existe na sua biblioteca de cabeçalhos."
    
    open(directory + "/headers/" + arg[1], "w")
    os.system("/usr/bin/vim " + directory + "/headers/" + arg[1])
    
    return arg[1] + " editado e salvo na sua biblioteca de cabeçalhos."

def init():
    '''
    Inicia a aplicação para que crie a biblioteca de cabeçalhos
    na máquina do usuário.
    '''
    config_read = open(".config.txt", "r")
    if config_read.readlines()[0] == "!init":
        config_write = open(".config.txt", "w")
        config_write.write("init")
        config_write.close()
        os.mkdir("headers")
        config_read.close()
        return("Header iniciado e pronto para utilizar!")

    config_read.close()
    return("Seu Header já foi iniciado!")