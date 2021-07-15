I = list(map(int, input().split()))
N = I[0]
Y = I[1]

for x in range(0,N+1):
	for y in range(0,N+1-x):
		z = N-x-y
		total = x*10000 + y*5000 + z*1000
		if total == Y:
			print(x,y,z)
			exit()

print("-1 -1 -1")