import math

N = int(input())
i = [list(map(int, input().split())) for i in range(N)]
pt = 0
px = 0
py = 0

for k in range(N):
	d = abs(px - i[k][1]) + abs(py - i[k][2])
	dt = i[k][0] - pt

	if dt < d:
		print("No")
		exit()

	if (dt-d)%2 == 0:
		pt = i[k][0]
		px = i[k][1]
		py = i[k][2]
		continue
	else:
		print("No")
		exit()


print("Yes")