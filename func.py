from socket import *
import threading
import sys
import time

def getArgs(args, usage):
	'''
	pega os argumentos passados na linha de comando
	e retorna uma lista com as opcoes fornecidas
	'''

	host = args[len(args) - 1]

	#valores padroes
	#-----------------------------------
False
	n = 0
	timeout = 2
	ports = False

	#-----------------------------------

	while n < len(args):
		if args[n] == "-p":
			try:
				ports = getPorts(args[n + 1])
				if ports == False:
					print(usage)
					exit(0)
			except:
				print(usage)
				exit(0)

		elif args[n] == "-h":
				print(usage)
				exit(0)
		elif args[n] == "-v":
			v = True

		elif args[n] == "-t":
			timeout = int(args[n + 1])
		n += 1

	if ports == False:
		print(usage)
		exit(0)

	return [ports, v, timeout]

def getPorts(range_ports):

	'''
	---------------------------------------------------------------
	retorna as portas a serem escaneadas
	caso o usuario nao forneça uma porta ou range de portas valido,
	retorna false
	---------------------------------------------------------------
	'''

	ports = []

	if "-" in range_ports:
		p = range_ports.split("-")

		if len(p) == 2:
			nport, final_port = [int(p[0]), int(p[1])]

			while nport <= final_port: #adiciona as portas na lista ports
				ports.append(nport)
				nport += 1
			return ports

		else:
			return False

	else:
		''' caso seja informada apenas uma porta, ela é adicionada a lista '''
		try:
			ports.append(int(range_ports))
			return ports
		except:
			return False;

def scanner(host, port, v, timeout, open_ports, closed_ports): #funcao que verifica se a porta está aberta

	s = socket(AF_INET, SOCK_STREAM)
	s.settimeout(timeout)

	addr = (host, port)

	if s.connect_ex(addr) == False:
		open_ports.append(port)

	else:
		closed_ports.append(port)

	s.close()
