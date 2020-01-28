#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  LibJack by Neo-Jack Ene/2020 #
import sys 
from os import system, name 

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
iniciando = "... Iniciando LibJack ..."
ini_pro = iniciando.center(50)
python3 = "LibJack corre bajo Python 3"
ini_py3 = python3.center(50)
uso = "Manera de usar: 'python3 libjack.py'"
ini_uso = uso.center(50)
print("....................................................")
print(ini_pro)
print("....................................................")
print("")
print(ini_py3)
print(ini_uso)
print("")
print("SI USTED UTILIZA PYTHON 2, EL PROGRAMA MOSTRARA (Error) ")
print("")
print("NOTA: Con LibJack, usted podra installar LIBRERIAS para python 2.7 y Python 3.x." )
print("")
print("....................................................")
print("Por favor escriba el nombre de la Libreria faltante.")
print("Ej: os")
print("Ej: colorama")
print("Ej: sys")
print("Ej: socks\n")
lib = input("Que Libreria le falta? \n")
if lib == "":
    lib = "ERROR"
while (lib):
    try:
        if lib == "ERROR":
            print("Libreria invalido, Reintente...\n")
            lib = input("Que Libreria te falta? Ej: socks\n")
        if lib == "":
            print("Libreria invalido, Reintente...\n")
            lib = input("Que Libreria te falta? Ej: socks\n")
        if lib != "":
            break
        else:
            lib = input("Que Libreria te falta? Ej: socks\n")
            if lib == "":
                lib = "ERROR"
    except:
        print("Libreria invalido, Reintente...\n")
        lib = input("Que Libreria te falta? Ej: socks\n")
if lib == "ERROR":
    print("Eror --> Inexistente LIBRERIA")
    print("Demasiados intentos. ADIOS")
    sys.exit()

clear()
print("................................................")
print("Para que version de Python necesitas la Libreria")
print("................................................")
print("Respuestas validas: 2 o 3\n")
print("Ej: 2 --> Python 2.7")
print("Ej: 3 --> Python 3.x\n")
py = input("Para que version Python? Ej: 2 o 3\n")
if py == "":
    py = "2"
while (py):
    try:
        if py == "2":
            py = "2"
            break
        if py == "3":
            py = "3"
            break
        if py == "":
            py = "2"
            break
        else:
            py = "2"
    except:
        py = ("2")
if py == "3":
    py_r = "3.x"
else:
    py_r = "2.7"

clear()
print(".................................")
print("Usted esta a punto de instalar...")
print(".................................\n")
print("Libreria:        " + lib + "\nPara Python:     " + py_r)
print("")
confirmar = input("Es Correcta la Informacion? Ej: 's' o 'n'\n ")
if confirmar == "":
    confirmar = "n"
while (confirmar):
    try:
        if confirmar == "s":
            confirmar = "Si"
            clear()
            break
        if confirmar == "n":            
            sys.exit()
        if not confirmar == "s":            
            sys.exit()
        if confirmar == "":            
            sys.exit()
    except:        
        sys.exit()

def python2o3():
    if py == '2':
        _ = system('sudo apt-get install python-pip')
        clear()
        print("\nNOTA:Ahora Instalaremos la Libreria " + lib + " para Python " + py_r)
        _ = system('sudo pip install ' + lib)
    else:
        _ = system('sudo apt-get install python3-pip')
        clear()
        print("\nNOTA: Ahora Instalaremos la Libreria " + lib + " para Python " + py_r)
        _ = system('sudo pip3 install ' + lib)

clear()
print("")
print("NOTA: Tendremos que realizar una Actualizacion de los Repositorios:")
system('sudo apt-get update')
clear()
print("")
print("NOTA: Instalaremos PIP, si ya esta instalado no se preocupe:")
python2o3()
print("")
print("Ya Terminamos...")
print("Gracias por usar LibJack. By Neo-Jack ENE/2020")
print("")
sys.exit()
