#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

listaSignos = ["!", "#", "$", "%", "&", "(", ")", "=", "?", "¿", "¡", "+", "-", "*"]
i = 0
f = open ('listado-general.txt','r')
lista = f.read().split()

while i < 5:
	parteUno = ""
	parte1 = lista[random.randrange(80383)]
	 
	for letra in parte1:
		azar = random.randrange(2)
		if azar == 0:
			parteUno += letra.upper()
		else:
			parteUno += letra

	parte2 = str(random.randrange(2000))
	signo = listaSignos[random.randrange(14)]

	print("Conetraseña {}: {}{}{}".format(i, parteUno, parte2, signo))
	i += 1

f.close()