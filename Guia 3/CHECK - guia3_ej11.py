def fx():
	for i in range(10):
		a=input('ingrese un caracter: ')
		letras=[]
		numeros=[]
		caracteres=[]
		if type(a)==str:
			letras.append(a)
		if type(a)==int:
			numeros.append(a)
		if a=='#':
			break
		else:
			caracteres.append(a)
	total=len(letras)+len(numeros)+len(caracteres)
	por_letras=len(letras)/total*100
	por_numeros=len(numeros)/total*100
	print(f'el porcentaje de letras es de {por_letras} y el de numeros es {por_numeros}')

fx()

