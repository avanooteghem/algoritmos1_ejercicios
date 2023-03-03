def fx():
	ventas_dto=[]
	print('Código 1: Descuento obra social. Código 2: Sin descuento OS.')
	for i in range(1000):
		a=int(input('Ingrese código: '))
		if a==1:
			b=int(input('Monto total de la venta: '))
			ventas_dto.append(b)
		else: 
			print('Fin de las ventas')
			suma_ventas=0
			ventas_mayores=0
			for i in ventas_dto:
				suma_ventas=suma_ventas+i
				if i >200:
					ventas_mayores=ventas_mayores+1

			porcentaje=ventas_mayores/len(ventas_dto)
			print(f'La suma total de las ventas con descuento fue: {suma_ventas}')
			print(f'El procentaje de ventas con descuento fue: {porcentaje}')


			break





fx()