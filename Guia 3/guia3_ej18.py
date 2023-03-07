def basket(a):
	viejos=0
	for i in range(a):
		nombre=input('Ingrese nombre: ')
		nacimiento=input('Ingrese fecha de nacimiento en formato aaaammdd: ')
		dia=nacimiento[-2:]
		mes=nacimiento[5:6]
		año=int(nacimiento[:4])
		print (f'El atleta {nombre} nació en la fecha: {dia}/{mes}/{año}')
		if año<1995:
			viejos+=1
	print(f'La cantidad de atletas nacidos antes de 1995 son {viejos}')


basket(3)