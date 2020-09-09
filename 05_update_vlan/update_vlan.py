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

f = open("ip_vlan.txt", "r")
imp = f.readlines()
f.close()

circuito = open("novo_ip_vlan.txt", "r")
circ = circuito.readlines()
circuito.close()

quant = len(imp) # CONTA OS ITENS

### REPLICA A CONFIGURAÇÃO 

while i < quant:
    host = imp[i]
    ip = host.rstrip()

    circui = circ[i]
    circname = circui.rstrip()

    nome = bytes(circname, 'utf-8')
    
    

    """ Telnet Active """
    print("\033[1;92mConfigurando nova VLAN para o IP ->"+ip)
    try:
        tn = telnetlib.Telnet(ip, 23, 10)
    except:
        with open('log_vlan.txt', 'a') as f:
            print("Falha de conexao com o ip: " + ip + "\n")
            f.writelines(ip + ";" + " falhou ao conectar" + "\n")
            f.closed
            i = i + 1
        continue

    """ Instrucoes """

    tn.read_until(b"login:")
    tn.write(b"oi31" + b"\n")
    time.sleep(1.0)
    tn.read_until(b"Password:")
    tn.write(b"oi31" + b"\n")
    time.sleep(1.0)
    tn.write(b"configure\n")
    time.sleep(1.0)
    tn.write(b"interface vlan 29\n")
    time.sleep(1.0)
    tn.write(b"no set-member ethernet all\n")
    time.sleep(1.0)
    tn.write(b"exit\n")
    time.sleep(1.0)
    tn.write(b"exit\n")
    time.sleep(1.0)
    tn.write(b"copy running-config startup-config 1\n")
    time.sleep(5.0)
    tn.write(b"exit\n")




    """ Guarda o LOG"""
    log = tn.read_all()
    f1 = open("log_vlan.txt", "a")
    f1.writelines(ip + " - " + str(log) + "\n")
    f1.close()
    tn.close() # FECHA A CONEXAO TELNET 
    i = i + 1 ### INCREMENTA "I"



print("\033[1;34mFINALIZANDO OPERACOES - - - - - AGUARDE...")    
time.sleep(10.0)
print("Operacao realizada com sucesso")
print("verifique o arquivo log_vlan.txt\033[0;0m")
    



