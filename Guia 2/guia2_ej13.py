def fx():
	for i in range(38):
		a=input('Ingrese nombre del alumno: ')
		notas=0
		for i in range(5):
			b=int(input('nota materia: '))
			notas=notas+b
		promedio=notas/5

		print(f'el promedio del alumno {a} es {promedio}')
fx()
