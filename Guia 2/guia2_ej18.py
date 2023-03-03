import numpy as np
def fx(): 
	for i in np.arange(1,2.1,0.1):
		rodenado_i=round(i,3)
		y=4*i**2-16*i+15
		redondeado=round(y,3)
		positivo='positivo'
		if y<0:
			positivo='no positivo'
		print(f'El valor de X es {rodenado_i}. El valor de y es {redondeado}, que es {positivo}')
fx()