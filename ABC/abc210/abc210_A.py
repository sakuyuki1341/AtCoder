i = list(map(int, input().split()))

N = i[0]
A = i[1]
X = i[2]
Y = i[3]

if N <= A:
	print(X*N)
else:
	print(X*A + Y*(N-A))