#!/usr/bin/env python
#-*- coding: utf-8 -*-

print """INSTRUKCJA UŻYTKOWANIA: 

Podaj komendę a następnie jej parametr.
Komendy:

Spadek - ustaw dolną granicę kursu uruchamiającą alarm dźwiękowy,
Wzrost - ustaw górną granicę kursu uruchamiającą alarm dźwiękowy,
Czas - odstęp między aktualizacjami,
Koniec - kończy program.

"""
while 1: 
	cmdw = raw_input(": ").lower().strip()
	if cmdw == "czas":
		invar = raw_input("Podaj wartość: ")
		if invar.isdigit() == True:
			plik = open('.time', 'w')
			plik.write(invar.strip())
			plik.close()
		else:
			print "Niepoprawna wartość"
	
	elif cmdw == "koniec":
		plik = open('.q', 'w')
		plik.write("1")
		plik.close()
		print "Wysyłanie sygnału zakończenia ..." 
		exit()
	elif cmdw == "spadek":
		invar = raw_input("Podaj wartość: ")
		if invar.isdigit() == True:
			plik = open('.drop', 'w') 
			plik.write(invar.strip())
		else:
			print "Niepoprawna wartość"
	elif cmdw == "wzrost":
		invar = raw_input("Podaj wartość: ")
		if invar.isdigit() == True:
			plik = open('.raise', 'w') 
			plik.write(invar.strip())
		else:
			print "Niepoprawna wartość"
	else:
		print "Niepoprawna komenda ! \n"
