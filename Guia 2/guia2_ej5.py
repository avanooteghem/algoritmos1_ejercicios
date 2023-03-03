lista=[140,180,250,10,20,-10-20-30-40-50]

def fx(a):
	mayores=[]
	menores=[]
	ninguna=[]
	for i in lista:
		if i>100:
			mayores.append(i)
		elif i < 0:
			menores.append(i)
	print(f'el promedio de los mayores de 100 es: {sum(mayores)/len(mayores)}')
	print(f' la suma de los negativos es: {sum(menores)}')






fx(lista)