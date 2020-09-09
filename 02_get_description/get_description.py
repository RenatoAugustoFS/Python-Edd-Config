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

f = open("ip_get_description.txt", "r")
imp = f.readlines()
f.close()

quant = len(imp) # CONTA OS ITENS

### REPLICA A CONFIGURAÇÃO 

while i < quant:
    host = imp[i]
    ip = host.rstrip()
    
    

    """ Telnet Active """

    try:
        tn = telnetlib.Telnet(ip, 23, 10)
    except EOFError as e:
        with open('log_get_description.txt', 'a') as f:
            print("Falha de conexao com o ip: " + ip + "\n")
            f.writelines(ip + ";" + " falhou ao conectar" + "\n")
            f.closed
            i = i + 1
        continue

    """ Instrucoes """
    print("\033[1;92mAguarde um instante.... PEGANDO TODAS AS DESCRICOES\033[0;0m")

    tn.read_until(b"login:")
    tn.write(b"oi31" + b"\n")
    time.sleep(0.1)
    tn.read_until(b"Password:")
    tn.write(b"oi31" + b"\n")
    time.sleep(0.1)
    tn.write(b"show interface description\n")
    time.sleep(0.1)
    tn.write(b"exit\n")

    """ Guarda o LOG"""
    log = tn.read_all()
    f1 = open("log_get_description.txt", "a")
    f1.writelines(ip + " - " + str(log) + "\n")
    f1.close()
    tn.close() # FECHA A CONEXAO TELNET 
    i = i + 1 ### INCREMENTA "I"

print("\033[1;34mFINALIZANDO OPERACOES - - - - - AGUARDE...")    
time.sleep(10.0)
print("Operacao realizada com sucesso")
print("verifique o arquivo log_get_description.txt\033[0;0m")

