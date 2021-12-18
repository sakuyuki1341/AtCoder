import math

i = list(map(int, input().split()))
#print(i)
H = i[0]
W = i[1]

A = [list(map(int, input().split())) for i in range(H)]
#print(A)
#print(A[0][1])

flag = True

for i2 in range(H):
	for i1 in range(i2):
		for j2 in range(W):
			for j1 in range(j2):
				if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
					flag = False
					break

if flag == True:
	print("Yes")
else:
	print("No")