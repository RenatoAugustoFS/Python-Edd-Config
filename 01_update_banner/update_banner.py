# -*- coding: cp1252 -*-
### IMPORT LIB ###

import getpass
import sys
import time
import telnetlib
import os

###  DECLARACAO DE VARIAVEIS ###

imp = []    # IMPORTA A LISTA DE IPS
quant = []  # CONTA A QUANTIDADE DE ITENS DA LISTA
i = 0       # INCREMENTA WHILE
host = 0    # IP DE DESTINO
log = []    # Guarda o Log de configuração
ip = []




### LEITURA DA LISTA DE DADOS ###

f = open("ip.txt", "r")
imp = f.readlines()
f.close()

circuito = open("circuito.txt", "r")
circ = circuito.readlines()
circuito.close()

quant = len(imp) # CONTA OS ITENS

### REPLICA A CONFIGURAÇÃO 

while i < quant:
    host = imp[i]
    ip = host.rstrip()

    circui = circ[i]
    circname = circui.rstrip()
    
    

    """ Telnet Active """
    print("\033[1;92mAdmin - Tentando confiurar banner do IP -> "+ip)
    try:
        tn = telnetlib.Telnet(ip, 23, 10)
    except:
        with open('log.txt', 'a') as f:
            print("Falha de conexao com o ip: " + ip + "\n")
            f.writelines(ip + ";" + " falhou ao conectar" + "\n")
            f.closed
            i = i + 1
        continue

    """ Instrucoes """
    nome = bytes(circname, 'utf-8')
    tn.read_until(b"login:")
    tn.write(b"admin" + b"\n")
    time.sleep(1.0)
    tn.read_until(b"Password:")
    tn.write(b"admin" + b"\n")
    time.sleep(1.0)
    tn.write(b"configure\n")
    time.sleep(1.0)
    tn.write(nome+b"\n")
    time.sleep(1.0)
    tn.write(b"banner login\n")
    time.sleep(1.0)
    tn.write(b"~#####################################################################################\nAtencao: Equipamento monitorado pela Gerencia proativa dos EDD'S\n#####################################################################################~\n")
    tn.write(b"!\n")
    tn.write(b"clock timezone Brasilia -3\n")
    tn.write(b"!\n")
    tn.write(b"username oi31 access-level 15\n")
    time.sleep(1.0)
    tn.write(b"username oi31 password 0 oi31\n")
    time.sleep(1.0)
    tn.write(b"exit\n")
    time.sleep(1.0)
    tn.write(b"copy running-config startup-config 1\n")
    time.sleep(5.0)
    tn.write(b"exit\n")




    """ Guarda o LOG"""
    log = tn.read_all()
    f1 = open("log.txt", "a")
    f1.writelines(ip + " - " + str(log[0:18]) + "\n")
    f1.close()
    tn.close() # FECHA A CONEXAO TELNET 
    i = i + 1 ### INCREMENTA "I"


imp = []    # IMPORTA A LISTA DE IPS
quant = []  # CONTA A QUANTIDADE DE ITENS DA LISTA
i = 0       # INCREMENTA WHILE
host = 0    # IP DE DESTINO
log = []    # Guarda o Log de configuração
ip = []




### LEITURA DA LISTA DE DADOS ###

f = open("ip.txt", "r")
imp = f.readlines()
f.close()

circuito = open("circuito.txt", "r")
circ = circuito.readlines()
circuito.close()

quant = len(imp) # CONTA OS ITENS


while i < quant:
    host = imp[i]
    ip = host.rstrip()

    circui = circ[i]
    circname = circui.rstrip()
    
    

    """ Telnet Active """
    print("oi31 - Tentando confiurar banner do. IP -> "+ip)

    try:
        tn = telnetlib.Telnet(ip, 23, 10)
    except:
        with open('log.txt', 'a') as f:
            print("Falha de conexao com o ip: " + ip + "\n")
            f.writelines(ip + ";" + " falhou ao conectar" + "\n")
            f.closed
            i = i + 1
        continue

    """ Instrucoes """
    nome = bytes(circname, 'utf-8')
    tn.read_until(b"login:")
    tn.write(b"oi31" + b"\n")
    time.sleep(1.0)
    tn.read_until(b"Password:")
    tn.write(b"oi31" + b"\n")
    time.sleep(1.0)
    tn.write(b"configure\n")
    time.sleep(1.0)
    tn.write(nome+b"\n")
    time.sleep(1.0)
    tn.write(b"banner login\n")
    time.sleep(1.0)
    tn.write(b"~#####################################################################################\nAtencao: Equipamento monitorado pela Gerencia proativa dos EDD'S\n#####################################################################################~\n")
    tn.write(b"!\n")
    tn.write(b"clock timezone Brasilia -3\n")
    tn.write(b"!\n")
    tn.write(b"username oi31 access-level 15\n")
    time.sleep(1.0)
    tn.write(b"username oi31 password 0 oi31\n")
    time.sleep(1.0)
    tn.write(b"exit\n")
    time.sleep(1.0)
    tn.write(b"copy running-config startup-config 1\n")
    time.sleep(5.0)
    tn.write(b"exit\n")

    """ Guarda o LOG"""
    log = tn.read_all()
    f1 = open("log.txt", "a")
    f1.writelines(ip + " - " + str(log[0:18]) + "\n")
    f1.close()
    tn.close() # FECHA A CONEXAO TELNET 
    i = i + 1 ### INCREMENTA "I"
    
print("\033[1;34mFINALIZANDO OPERACOES - - - - - AGUARDE...")    
time.sleep(5.0)
print("Operacao realizada com sucesso")
time.sleep(0.5)
print("Verifique o arquivo log.txt\033[0;0m")


