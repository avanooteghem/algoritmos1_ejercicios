def fx():
	a=int(input('Ingrese factorial: '))
	factorial=a+1
	b=1
	for i in range(1,factorial):
		b=b*i
	print(b)

fx()