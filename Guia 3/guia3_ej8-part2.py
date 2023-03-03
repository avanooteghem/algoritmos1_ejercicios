def fx():
	nombres=[]
	saltos_buenos=[]
	saltos_malos=[]
	for i in range(3):
		nombre=input('Ingrese nombre del atleta: ')
		dia_nac=int(input('Ingrese día de nacimiento: '))
		mes_nac=int(input('Ingrese mes de nacimiento: '))
		año_nac=int(input('Ingrese año de nacimiento: '))
		salto1=int(input('Ingrese distancia salto1: '))
		salto2=int(input('Ingrese distancia salto2: '))
		salto3=int(input('Ingrese distancia salto3: '))
		edad=f'{dia_nac}-{mes_nac} -{año_nac}'
		if salto1>salto2 and salto1>salto3:
			mejor_salto=salto1
		elif salto2>salto1 and salto2>salto3:
			mejor_salto=salto2
		elif salto3>salto1 and salto3>salto2:
			mejor_salto=salto3
		if salto1<salto2 and salto1<salto3:
			peor_salto=salto1
		elif salto2<salto1 and salto2<salto3:
			peor_salto=salto2
		elif salto3<salto1 and salto3<salto2:
			peor_salto=salto3
		print(f'el mejor salto de {nombre}, cuyo nacimiento es {edad} es {mejor_salto}')
		saltos_buenos.append(mejor_salto)
		saltos_malos.append(peor_salto)
		nombres.append(nombre)
	nombre_mejor_salto=nombres[saltos_buenos.index(max(saltos_buenos))]
	nombre_peor_salto=nombres[saltos_malos.index(min(saltos_malos))]


	respuesta=f'El mejor salto fue de {nombre_mejor_salto} y el peor salto fue de {nombre_peor_salto}'	
	return respuesta

print(fx())
