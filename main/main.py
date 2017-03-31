#!/usr/bin/env python 
#! -*- coding:utf-8 -*-

from time import sleep as slp
try:
	import requests
except:
	print "\n\n Zainstaluj bibliotekę requests : sudo pip install requests\n\n"
import json
try:
	import pygame
except:
	print "\n\n Zainstaluj bibliotekę requests : sudo pip install pygame\n\n"
try:
	from terminaltables import AsciiTable, SingleTable
except:
	 print "\n\n Zainstaluj bibliotekę terminaltables : sudo pip install terminaltables\n\n"
import os




while 1:
	try:
		UPdelay = open('.time', 'r').read()
	except:
		UPdelay = 5
	slp(float(UPdelay))
#BitBay.net https://bitbay.net/API/Public/BTCPLN/ticker.json BBdict["bid"] BBdict["ask"]
	try:
		BBticker = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json").text
	except:
		print "BŁĄD POŁĄCZENIA"
	BBdict = json.loads(BBticker)

#BitMarket.pl  https://www.bitmarket.pl/json/BTCPLN/ticker.json"
	try:
		BMticker = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json").text
	except:
		print "BŁĄD POŁĄCZENIA"	
	BMdict = json.loads(BMticker)
#Alarm
	try:
		drop = open('.drop', 'r').read()
		dropval = drop.strip()
		if float(dropval) > float(BBdict["ask"]):
			pygame.init()
			pygame.mixer.init()
			snd = pygame.mixer.Sound(".al.wav")
			snd.play()
			os.system("clear")
			print "\n\n\n\nKURS OSIĄGNĄŁ GRANICZNĄ WARTOŚĆ!"
			slp(2)
		elif float(dropval) > float(BMdict["ask"]):
			pygame.init()
			pygame.mixer.init()
			snd = pygame.mixer.Sound(".al.wav")
			snd.play()
			os.system("clear")
			print "\n\n\n\nKURS OSIĄGNĄŁ GRANICZNĄ WARTOŚĆ!"
			slp(2)
		else:
			pass
	except:
		slp(1)
		
		
	try:
		raiser = open('.raise', 'r').read()
		raiserval = raiser.strip()
		if float(raiserval) < float(BBdict["ask"]):
			pygame.init()
			pygame.mixer.init()
			snd = pygame.mixer.Sound(".al.wav")
			snd.play()
			os.system("clear")
			print "\n\n\n\nKURS OSIĄGNĄŁ GRANICZNĄ WARTOŚĆ!"
			slp(2)
		elif float(raiserval) < float(BMdict["ask"]):
			pygame.init()
			pygame.mixer.init()
			snd = pygame.mixer.Sound(".al.wav")
			snd.play()
			os.system("clear")
			print "\n\n\n\nKURS OSIĄGNĄŁ GRANICZNĄ WARTOŚĆ!"
			slp(2)
		else:
			pass
	except:
		slp(1)
	try:
		table_data = [
			["BID","ASK", "Najwyższa", "Najniższa", "Obrót"],
			[BBdict["bid"],BBdict["ask"], BBdict["max"],BBdict["min"],BBdict["volume"]],

		]

		table = SingleTable(table_data, "BitBay.net")
		table.justify_columns = {0: 'center', 1: 'center', 2: 'center',3: 'center', 4: 'center'}
		table.inner_row_border = True
	except:
		pass
		
	try:
		table1_data = [
			["BID","ASK", "Najwyższa", "Najniższa","Obrót"],
			[BMdict["bid"],BMdict["ask"], BMdict["high"],BMdict["low"],BMdict["volume"]],

		]

		table1 = SingleTable(table1_data, "BitMarket.pl")
		table1.justify_columns = {0: 'center', 1: 'center', 2: 'center',3: 'center', 4: 'center'}
		table1.inner_row_border = True
	except:
		pass
	try:
		os.system("clear")
	except:
		pass
	print table.table
	print "\n\n"
	print table1.table
	
	try:
		bye = open('.q', 'r').read()
	except:
		pass
	if bye == "1":
		plik = open('.q', 'w')
		plik.write("0")
		plik.close()
		os.system("clear")
		print "\n\nOTRZYMANO SYGNAŁ WYŁĄCZENIA PROGRAMU\n\n"
		slp(1)
		exit()
	else:
		pass

		



