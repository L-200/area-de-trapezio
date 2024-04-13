B = float(input())
b = float(input())
h = float(input())
if B > 0.0 and b > 0.0 and h > 0.0:
	soma = B + b
	multiplicação = soma * h
	area = multiplicação / 2
	print(str(area))
else:
	print("Nao e possível calcular a area")