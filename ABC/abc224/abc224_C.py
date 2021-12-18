import math
from typing import Counter

N = int(input())
#print(N)

P = [list(map(int, input().split())) for i in range(N)]
#print(A)

c = 0

for i in range(N-2):
	for j in range(i+1, N-1):
		for k in range(j+1, N):
			S = (P[j][0] - P[i][0])*(P[k][1] - P[i][1]) - (P[k][0] - P[i][0])*(P[j][1] - P[i][1])
			if S != 0:
				c += 1

print(c)