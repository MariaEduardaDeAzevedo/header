#!/usr/bin/python
#coding: utf-8
import sys
import os.path

def write(arg):
    header = open(arg[1], "r")
    file_ = open(arg[2], "a")

    for line in header.read():
        file_.writelines(line)
    
    header.close()
    file_.close()
    return ("Conteúdo de " + arg[1] + " importado em " + arg[2])

def write_save(arg, directory):
    header = open(directory + "/headers/" + arg[1], "r")
    file_ = open(arg[2], "a")

    for line in header.read():
        file_.writelines(line)
    
    header.close()
    file_.close()
    return ("Conteúdo de " + arg[1] + " importado em " + arg[2])

def save(arg):
    file_name = arg[1].split("/")[-1]
    os.link(arg[1], directory + "/headers/" + file_name)
    return (file_name + " salvo em sua biblioteca de cabeçalhos")

def create(arg, directory):
    open(directory + "/headers/" + arg[1], "w")
    os.system("/usr/bin/vim " + directory + "/headers/" + arg[1])

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
    print("\033[1;32mComando para importar um cabeçalho em um arquivo:\033[0;0m")
    print("python header.py w <caminho_do_cabeçalho> <caminho_do_arquivo>")
else:
    arg.pop(0)

if status and arg[0].lower() == "w":
    print(write(arg))
elif status and arg[0].lower() == "ws":
    print(write_save(arg, directory))
elif status and arg[0].lower() == "s":
    print(save(arg))
elif status and arg[0].lower() == "c":
    print(create(arg, directory))
elif not status and arg[0].lower() == "init":
    print(init())

config.close()
