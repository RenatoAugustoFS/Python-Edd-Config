# -*- coding: cp1252 -*-
### IMPORT LIB ###

import getpass
import sys
import time
import telnetlib
import os

###  DECLARACAO DE VARIAVEIS ###

imp = []  # IMPORTA A LISTA DE IPS
quant = []  # CONTA A QUANTIDADE DE ITENS DA LISTA
i = 0  # INCREMENTA WHILE
host = 0  # IP DE DESTINO
log = []  # Guarda o Log de configuração
ip = []

### LEITURA DA LISTA DE DADOS ###

f = open("ip_switch.txt", "r")
imp = f.readlines()
f.close()

circuito = open("circuito_switch.txt", "r")
circ = circuito.readlines()
circuito.close()

quant = len(imp)  # CONTA OS ITENS

### REPLICA A CONFIGURAÇÃO

while i < quant:
    host = imp[i]
    ip = host.rstrip()

    c = 24
    c = c * i
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    print("\033[1;92mConfigurando porta 1/1 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)

    """ Telnet Active """

    try:
        tn = telnetlib.Telnet(ip, 23, 10)
    except EOFError as e:
        with open('log_switch.txt', 'a') as f:
            print("Falha de conexao com o ip: " + ip + "\n")
            f.writelines(ip + ";" + " falhou ao conectar" + "\n")
            f.closed
            i = i + 1
        continue

    """ Instrucoes """
    tn.read_until(b"login:")
    tn.write(b"admin" + b"\n")
    time.sleep(0.1)
    tn.read_until(b"Password:")
    tn.write(b"admin" + b"\n")
    time.sleep(0.1)
    tn.write(b"configure\n")
    time.sleep(0.1)
    tn.write(b"interface ethernet 1/1\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/2 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/2\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/3 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/3\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/4 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/4\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/5 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/5\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/6 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/6\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/7 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/7\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/8 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/8\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/9 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/9\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/10 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/10\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/11 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/11\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/12 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/12\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/13 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/13\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/14 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/14\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/15 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/15\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/16 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/16\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/17 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/17\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/18 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/18\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/19 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/19\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/20 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/20\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/21 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/21\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/22 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/22\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/23 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname)
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/23\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    c = c + 1
    print("Configurando porta 1/24 do ip -> " + ip)
    print("Nova descricao adicionada -> " + circname + "\033[0;0m")
    circui = circ[c]
    circname = circui.rstrip()
    nome = bytes(circname, 'utf-8')
    tn.write(b"interface ethernet 1/24\n")
    time.sleep(0.1)
    tn.write(nome+b"\n")

    time.sleep(0.1)
    tn.write(b"exit\n")
    time.sleep(0.1)
    tn.write(b"exit\n")
    time.sleep(0.1)
    tn.write(b"copy running-config startup-config 1\n")
    time.sleep(2.0)
    tn.write(b"exit\n")


    """ Guarda o LOG"""
    log = tn.read_all()
    f1 = open("log_switch.txt", "a")
    f1.writelines(ip + str(log) + "\n")
    f1.close()
    tn.close() # FECHA A CONEXAO TELNET 
    i = i + 1 ### INCREMENTA "I"

print("\033[1;34mFINALIZANDO OPERACOES - - - - - AGUARDE...")    
time.sleep(10.0)
print("Operacao realizada com sucesso")
print("verifique o arquivo log_update_switch.txt\033[0;0m")
    
