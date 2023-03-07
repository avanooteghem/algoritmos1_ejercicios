def fx(a,b,c):
	if c>a>b:
		print(f'Orden menor a mayor: {b} , {a} , {c}')
		print(f'Orden mayor a menor: {c} , {a} , {b}')
	elif c>b>a:
		print(f'Orden: {a} , {b} , {c}')
		print(f'Orden mayor a menor: {c} , {b} , {a}')
	elif a>c>b:
		print(f'Orden: {b} , {c} , {a}')
		print(f'Orden mayor a menor: {a} , {c} , {b}')
	elif a>b>c:
		print(f'Orden: {c} , {b} , {a}')
		print(f'Orden mayor a menor: {a} , {b} , {c}')
	elif b>a>c:
		print(f'Orden: {c} , {a} , {b}')
		print(f'Orden mayor a menor: {b} , {a} , {c}')
	elif b>c>a:
		print(f'Orden: {a} , {c} , {b}')
		print(f'Orden mayor a menor: {b} , {c} , {a}')
	else:
		print('Error')

fx(10,11,23)