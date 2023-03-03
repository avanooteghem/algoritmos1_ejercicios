for i in range(3):
	def fx(nombre,dia_nac,mes_nac,año_nac,salto1,salto2,salto3):
		edad=f'{dia_nac}-{mes_nac} -{año_nac}'
		mejor_salto=0
		if salto1>salto2 and salto1>salto3:
			mejor_salto=salto1
		elif salto2>salto1 and salto2>salto3:
			mejor_salto=salto2
		elif salto3>salto1 and salto3>salto2:
			mejor_salto=salto3
		respuesta=f'el resultado de {nombre}, cuyo nacimiento es {edad} es {mejor_salto}'
		return respuesta

print(fx('alan',8,2,1998,20,30,40))



