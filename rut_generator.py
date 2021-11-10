import math

f = open("rut_dictionary.txt", "a")
for x in range(1000000, 30000000):
	rut = str(x)
	inv = rut[len(rut)::-1]
	j = 2
	suma = 0
	for digit in inv:
		suma += (int(digit)*j)
		if j == 7:
			j = 2
		else:
			j += 1
	dv = str(11 - (suma - (math.trunc(suma / 11) * 11)))
	if dv == "11":
		dv = "0"
	if dv == "10":
		dv = "K"
	f.write(rut + dv + "\n")
f.close()