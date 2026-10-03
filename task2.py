def second_max_element(list):
	bez_povtora = list(set(list))
	spisok = sorted(list, reverse = 1)
	print(spisok[1])