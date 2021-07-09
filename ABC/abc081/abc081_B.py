N = int(input())
A = list(map(int, input().split()))

minnum = 30

for i in A:
	num = 0
	while 1:
		if i % 2 == 0:
			i /= 2
			num += 1
		else:
			if num < minnum:
				minnum = num
			break

print(minnum)