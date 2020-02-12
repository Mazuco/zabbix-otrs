#!/usr/bin/env python3

"""
  Este script é executado automaticamente apos a abertura do ticket no OTRS
  
  Modificado em 12 de fevereiro de 2020
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

from zabbix_api import ZabbixAPI
import sys
 
server = "http://localhost/zabbix"
username = "Admin"             
password = "zabbix"     
 
conexao = ZabbixAPI(server = server)
conexao.login(username, password)

reconhecer_evento = conexao.event.acknowledge({"eventids": sys.argv[1], "message": "Ticket " + str(sys.argv[2]) + " criado no OTRS."})

# publicado originalmente: https://github.com/janssenlima/zabbix-otrs
