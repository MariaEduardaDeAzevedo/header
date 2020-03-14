#!/usr/bin/python3
#coding: utf-8
import sys
import os.path
import shutil

def write(arg):
    
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
    file_ = os.path.expanduser("~/") + "/" + arg[1]
    open(directory + "/headers/" + file_.split("/")[-1], "w")
    shutil.copyfile(os.path.expanduser("~/") + arg[1], directory + "/headers/" + file_.split("/")[-1])
    return (file_.split("/")[-1] + " salvo em sua biblioteca de cabeçalhos")

def create(arg, directory):
    if arg[1] in os.listdir(directory + "/headers"):
        return "Já existe um cabeçalho salvo com esse nome!"
    open(directory + "/headers/" + arg[1], "w")
    os.system("/usr/bin/vim " + directory + "/headers/" + arg[1])
    return arg[1] + "criado e salvo na sua biblioteca de cabeçalhos."

def list_ws(directory):
    for f in os.listdir(directory + "/headers"):
        print("\033[1;34m" + f + "\033[0;0m")

def edit(arg, directory):
    if arg[1] not in os.listdir(directory + "/headers"):
        return arg[1] + " não existe na sua biblioteca de cabeçalhos."
    
    open(directory + "/headers/" + arg[1], "w")
    os.system("/usr/bin/vim " + directory + "/headers/" + arg[1])
    
    return arg[1] + " editado e salvo na sua biblioteca de cabeçalhos."

def init():
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

#Programa Principal    
arg = sys.argv
directory = os.path.dirname(os.path.realpath(__file__))
config = open(".config.txt", "r")
status = True if config.readlines()[0] == "init" else False

if len(arg) == 1:
    print("\033[1;33mOlá! Bem-vindo ao Header!\033[0;0m")
    print("\033[1;32mStatus do Header: iniciado\033[0;0m" if status == True else "\033[1;31mStatus do Header: não iniciado\033[0;0m")
    print("\033[1;32mLista de comandos no link abaixo:\033[0;0m")
    print("https://github.com/MariaEduardaDeAzevedo/header")
else:
    arg.pop(0)

if status and arg[0].lower() == "w":
    print(write(arg))
elif status and arg[0].lower() == "ws":
    print(write_save(arg, directory))
elif status and arg[0].lower() == "s":
    print(save(arg, directory))
elif status and arg[0].lower() == "c":
    print(create(arg, directory))
elif not status and arg[0].lower() == "init":
    print(init())
elif status and arg[0].lower() == "list":
    list_ws(directory)
elif status and arg[0].lower() == "e":
    print(edit(arg, directory))

config.close()
