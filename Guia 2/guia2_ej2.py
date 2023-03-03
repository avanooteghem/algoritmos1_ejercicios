def fx():
	a=[]
	for i in range(0,100000):
		d=int(input('Enter a number bigger than zero: '))
		if d>1:
			a.append(d)
		else:		
			for i in a:
				b=[]
				c=a[i]%3
				if c == 0:
					b.append(a[i])
					print(b)
				else:
					print(f'La cantidad de elementos en la lista múltiplos de 3 son: {len(b)}')
			break





fx()