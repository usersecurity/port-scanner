#!/usr/bin/python3

from func import *
import sys

def main(args):
	usage = "Usage: " + args[0] + " -p [ports] host\n" + "options:\n" + "\t-h\t\tshow this help" + "\n\t-p [ports]\tports to scan\n"

	host = args[len(args) - 1]

	ports, v, timeout = getArgs(args, usage)

	threads = []
	open_ports = []
	closed_ports = []

	print("Starting scan at: %s" % time.ctime())

	for port in ports:
		t = threading.Thread(target=scanner, args=(host, port, v, timeout, open_ports, closed_ports))
		threads.append(t)

	for i in range((ports[len(ports) - 1] - ports[0])):
		threads[i].start()

	for port in open_ports:
		print("port %s is open" % str(port))

	if v:
		for port in closed_ports:
			print("port %s is closed" % str(port))

	print("Scan finished at: %s" % time.ctime())

if __name__ == "__main__":
	main(sys.argv)

