![alt text](https://raw.githubusercontent.com/neo-jack-official/LibJack/master/vista01.png)
# LibJack (libjack.py)
# Es una Herramienta que te ayuda a instalar las librerias Python faltantes por Neo-Jack ENE/2020

## ¿Qué es LibJack?

Es una simple herramienta que te permite Intsllar cualuier libreria python que requieras.
Evita complejos codigos facil de usar, instala librerias python 2.7 y 3.x.
Solo disponible para sistemas que funcionen con "SUDO"

## Que version python utiliza?
Python 3.6

## Como se que version python tengo?
* `python -V | python3 -V`

## ¿Como funciona LibJack?
1. Te pregunta por libreria que requeires Ejemplo: colorama.
2. Luego te pregunta, para que version de Python necesitas esa libreria.
3. Solicita confirmacion de Informacion.
4. Realiza un UPDATE necesario, e instala PIP si no lo tiene instalado, es requerido para installar  las Librerias 
5. Luego procede a Instalar la Libreria.

## Como lo utiliso?

Si `libjack.py` esta en Escritorio:
1) Abra terminal, Escriba `cd Escritorio`
2) Ejecute bajo Python 3:
* `python3 libjack.py3` 

## Opciones de Configuracion

TODO es Preguntado desde el Programa
* `Libreria requerida` 
* `para que version de Python` 

## Como Instalar PYTHON 3.6 ?
## Linux con SUDO

Abrir terminal:
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Tengo problemas para instalar PYTHON 3.6
* `sudo apt-get install software-properties-common`
* `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt-get update`
* `sudo apt-get install build-essential checkinstall`
* `sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev`
* `sudo apt-get install python3.6`

## Revisamos que python esta instalado correctamente
* `python3 -V`

## Problemas comunes
## No encuentro (xxx) Modulo
xxx llamaremos a la libreria faltante  mas a bajo la llamremos SOCKS.
Tanto modo manual como LibJack instalan las librerias en las mismas carpetas descritas mas a bajo

## No encuentra la libreria SOCKS (Modo MANUAL)
Lib socks se utiliza para conoctar a TOR.
* `sudo apt-get install python-pip`
* `sudo apt-get install python3-pip`
* `sudo apt-get install socks

Por defecto se instalara en:

/usr/local/lib/

Luego copia lo que este dentro y pegas en:

/Carpeta Personal/.local/lib



