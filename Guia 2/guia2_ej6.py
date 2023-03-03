sueldo=0
for _ in range (3):

	a=input('Inserte Nombre: ')
	b=int(input('Inserte sueldo básico: '))
	c=int(input('Inserte antiguedad: '))
	d=int(input('Inserte cantidad de hijos: '))
	potenciador_hijos=(0.05*d)*b
	potenciador_antiguedad=0

	if 2<c<5:
		potenciador_antiguedad=0.2
	elif 4<c<9:
		potenciador_antiguedad=0.4
	elif 9<c:
		potenciador_antiguedad=0.7

	sueldo_nuevo=b+potenciador_hijos+(potenciador_antiguedad*b)
	sueldo+=sueldo_nuevo

print(f'la suma de los sueldos nuevos es {suma}')


