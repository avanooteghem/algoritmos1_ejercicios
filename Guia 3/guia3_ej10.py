import random
def fx():
	for i in range(5):
		a=random.randrange(10,1000,1)
		suma=0
		for b in range(1,a):
			if a%b==0:
				suma+=b
		if a<suma:
			print(f'El numero {a} es abundante')
		else:
			print(f'El numero {a} no es abundante')

fx()
