#!/usr/bin/python
 
# python_ping.py - Hace ping a ciertos elementos de la red.
# ---------------------------------------------------------
# Este programa es software libre. Puede redistribuirlo y/o
# modificarlo bajo los términos de la Licencia Pública General
# de GNU según es publicada por la Free Software Foundation,
# bien de la versión 2 de dicha Licencia o bien (según su
# elección) de cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea
# útil, pero SIN NINGUNA GARANTÍA, incluso sin la garantía
# MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN
# PROPÓSITO PARTICULAR. Para más detalles, véase la Licencia
# Pública General de GNU.
#
# Autor: LinuxmanR4 http://linuxmanr4.com
# versión 1.0
#
 
import os
import csv
from colorama import Fore
import time
import datetime
 
 
def check_ping(hostname):
    response = os.system("fping -r 10 -q " + hostname + " >/dev/null")
    if response == 0:
        check_ping = "[OK]"
    else:
        check_ping = "[Error]"
 
    return check_ping
 
 
#def sonido_alerta():
    #os.system("play -q ent_communicator1.mp3")
 
# Lee los datos del archivo y los guarda en una variable.
archivo_servidores = open('servidores.csv')
servidores_reader = csv.reader(archivo_servidores)
datos_servidores = list(servidores_reader)
 
# Prueba si hay conexión en todos los servidores
contador = 0
 
while True:
    for i in range(len(datos_servidores)):
        servidorTexto = datos_servidores[i][0]
        servidorIP = datos_servidores[i][1]
        resultado = check_ping(datos_servidores[i][1])
 
        if resultado == "[Error]":
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.RED + resultado))
            #sonido_alerta()
        else:
            print("{0:30} {1:17} {2:7}".format(
                Fore.WHITE + servidorTexto, servidorIP, Fore.GREEN + resultado))
 
    contador += 1
    print(Fore.BLUE)
    print('{0} {1:%H:%M:%S} {2}'.format(contador, datetime.datetime.now(),
                                    "________________________________________"))
    print()
 
    # Pausa de 10 minutos.
    time.sleep(60)