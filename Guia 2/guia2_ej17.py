def fx():
	mejor_promedio=0
	alumno=''
	for i in range(3):
		nombre=input('Ingrese nombre: ')
		materia1=int(input('Ingrese nota 1: '))
		materia2=int(input('Ingrese nota 2: '))
		materia3=int(input('Ingrese nota 3: '))
		promedio=(materia1+materia2+materia3)/3
		if promedio>mejor_promedio:
			mejor_promedio=promedio
			alumno=nombre
	print(f'El alumno {alumno} obtuvo el mejor promedio: {mejor_promedio}')

fx()
