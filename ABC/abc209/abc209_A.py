i = list(map(int, input().split()))

if i[1] - i[0] < 0:
	print(0)
else:
	print(i[1] - i[0] + 1)