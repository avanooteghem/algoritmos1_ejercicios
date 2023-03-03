def fx():
	a=int(input('Si es cuadrado, inserte 1. Si es círculo, inserte 2: '))
	if a==1:
		b=int(input('ingrese la base del cuadrado: '))
		c=int(input('ingrese la altura del cuadrado: '))
		d=print(f'El área del cuadrado es {b*c}')
	else:
		b=int(input('ingrese el radio del círculo: '))
		c=print(f'El área del cuadrado es {3.1416*b**2}')

fx()
