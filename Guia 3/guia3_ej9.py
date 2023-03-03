def fx():
	for i in range(5):
		divisores=[]
		a=int(input('ingrese número a evaluar: '))
		for i in range(1,a):
			if a%i==0:
				divisores.append(i)
		suma=0
		for b in divisores:
			suma=suma+b
		if suma==a:
			print(f'el número {a} es perfecto')
		else:
			print(f'el número {a} no es perfecto')

fx()
