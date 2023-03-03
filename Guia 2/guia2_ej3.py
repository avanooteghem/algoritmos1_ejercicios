lista=[3,6,9,15,30,18,45,60,21,24,27]

def fx(a,b):
	respuesta=[]
	for i in b:
		if i%3 == 0:
			if i%5!=0:
				respuesta.append(i)
	return respuesta[0:a]



print(fx(5,lista))
