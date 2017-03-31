#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os 
import threading

cwd = os.getcwd()
def worker0():
	os.system("xterm -T Podgląd -geometry 90x34+0+0 "+cwd+"/main/main.py")

def worker1():
	os.system("xterm -T Komendy -geometry 90x34+550+0 "+cwd+"/main/command.py")


threads = []

t0 = threading.Thread(target=worker0)
threads.append(t0)
t0.start()

t1 = threading.Thread(target=worker1)
threads.append(t1)
t1.start()
