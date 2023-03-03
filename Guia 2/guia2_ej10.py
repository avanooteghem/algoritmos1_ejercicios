def fx():
	a=int(input('ingrese numero positivos: '))
	position=-1
	maximo=a
	while a>=0:
		position=position+1
		if a>maximo:	
			maximo=a
		a=int(input('ingrese numero positivos: '))
	print(f'El valor máximo es {maximo} y se encuentra en la posición {position}')

fx()