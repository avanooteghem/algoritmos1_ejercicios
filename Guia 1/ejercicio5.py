def fx():
	a=input('Ingrese el nombre del candidato: ')
	b=int(input('Ingrese calificación del examen 1: '))
	c=int(input('Ingrese calificación del examen 2: '))
	if b>=65 and c>=65:
		print(f'El candidato {a} es aceptado')
	else:
		print(f'El candidato {a} es rechazado')	



fx()