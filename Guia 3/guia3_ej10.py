import random
def fx():
	for i in range(5):
		a=random.randrange(10,1000,1)
		divisores=[]
		for b in range(1,a):
			if a%b==0:
				divisores.append(b)
		suma=0
		for c in divisores:
			suma=suma+c
		if a<suma:
			print(f'El numero {a} es abundante')
		else:
			print(f'El numero {a} no es abundante')

fx()
