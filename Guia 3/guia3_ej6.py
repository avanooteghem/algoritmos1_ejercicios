def fx(dia,mes,año,dia_act,mes_act,año_act):
	a=año_act-año
	if mes_act>mes and dia_act<dia:
		a=a-1
	elif mes_act==mes and dia_act<dia:
		a=a-1
	else:
		a
	return a

print(fx(8,2,1998,7,2,2023))
