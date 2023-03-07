def fx(a,b,c):
	if c>a>b:
		print(f'Orden: {b} , {a} , {c}')
	elif c>b>a:
		print(f'Orden: {a} , {b} , {c}')
	elif a>c>b:
		print(f'Orden: {b} , {c} , {a}')
	elif a>b>c:
		print(f'Orden: {c} , {b} , {a}')
	elif b>a>c:
		print(f'Orden: {c} , {a} , {b}')
	elif b>c>a:
		print(f'Orden: {a} , {c} , {b}')
	else:
		print('Error')

fx(8,7,9)