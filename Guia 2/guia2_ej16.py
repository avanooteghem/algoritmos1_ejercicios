def fx():
	a=int(input('Ingrese un número positivo: '))
	while a>0:
		suma_numeros=0
		for i in range(a+1):
			suma_numeros+=i
		print(f'La suma del 1 a dicho numero es: {suma_numeros}')
		a=int(input('Ingrese un número positivo: '))
		
fx()