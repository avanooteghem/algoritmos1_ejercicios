def fx(a):
	if a%4==0 and a%100!=0:
		respuesta='Año bisiesto'
	elif a%400==0:
		respuesta='Año bisiesto'
	else:
		respuesta='Año no bisiesto'
	return respuesta

print(fx(1996))