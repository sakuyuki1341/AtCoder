A = list(map(int, input().split()))

num = 0

while 1:
	dif = [A[1]-A[0], A[2]-A[1]]
#		   増(デメ)+減  増+減(デメ)

	if dif[0] == dif[1]:
		print(int(num))
		exit()

	if dif[0] < dif[1]:
		if (dif[1] - dif[0])%2 == 1:
			num += (dif[1] - dif[0] + 1)/2
			A[1] += (dif[1] - dif[0] + 1)/2
		else:
			num += (dif[1] - dif[0])/2
			A[1] += (dif[1] - dif[0])/2
		continue

	if dif[0] > dif[1]:
		num += dif[0] - dif[1]
		A[2] += dif[0] - dif[1]
		continue