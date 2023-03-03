valores=[1,5,120,4,5,6,120,8,14,15,-1,-17.4,-25,-20]

def fx(a):
	maximo_negativo=0
	minimo_positivo=0
	minimo_rango=0
	for i in valores:
		if i<0:
			maximo_negativo=i
			for b in valores:
				if 0>b>maximo_negativo:
					maximo_negativo=b
		if -17.3<i<26.9:
			minimo_rango=i
			for b in valores:
			 	if b<minimo_rango:
			 		minimo_rango=b
		if i>0:
			minimo_positivo=i
			for b in valores:
				if 0<b<minimo_positivo:
					minimo_positivo=b

	print(f'El Máximo negativo es {maximo_negativo}, el minimo positivo es {minimo_positivo} y el mínimo en el rango 17.3 - 26.9 es {minimo_rango}')


fx(valores)