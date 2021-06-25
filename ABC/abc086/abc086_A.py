i = list(map(int, input().split()))

product = i[0] * i[1]

if product % 2 == 0:
	print("Even")
else:
	print("Odd")
