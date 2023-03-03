def fx():
	a=[]
	for i in range(0,100000):
		d=int(input('Enter a number bigger than zero: '))
		if d>0:
			a.append(d)
		else:
			print(f'La cantidad de elementos en la lista es {len(a)}')
			break

fx()

