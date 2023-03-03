def fx():
	lista=[]
	for i in range(10000):
		a=int(input('Ingrese numeros: '))
		if a == 0:
			break
		else:
			lista.append(a)
	minimo_positivo=0
	for i in lista:
		if i>0:
			minimo_positivo=i
		for b in lista:
			if 0<b<minimo_positivo:
				minimo_positivo=b
	return minimo_positivo



def jaja():
	numero_ingresado=int(input('Ingrese numero positivo: '))
	minimo_positivo_encontrado_hasta_ahora=numero_ingresado
	print(minimo_positivo_encontrado_hasta_ahora)
	while numero_ingresado!=0 :	
		if 0 < numero_ingresado < minimo_positivo_encontrado_hasta_ahora:
			minimo_positivo_encontrado_hasta_ahora=numero_ingresado
		numero_ingresado=int(input('Ingrese numeros: '))
	return minimo_positivo_encontrado_hasta_ahora


print('el minimo valor ingresado es', jaja())

#Patrones: input inicial e input para rebuclear - permite tener la variable definida previamente a evaluarla en el while.
#Encontrar valor con propiedades-condiciones según valor de respuesta esperado, como punto de partida.

