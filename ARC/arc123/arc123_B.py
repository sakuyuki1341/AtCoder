N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

usedA = -1
usedB = -1
usedC = -1
ret = 0

def ans():
	print(ret)
	exit()


while 1:
	if usedA == N-1 or usedB == N-1 or usedB == N-1:
		ans()

	nowA = A[usedA+1]
	nowB = B[usedB]
	nowC = C[usedC]
	
	flagB = 1
	for i in range(usedB+1, N):
		if nowA < B[i]:
			nowB = B[i]
#			print(nowB)
			usedB = i
			flagB = 0
			break
	if flagB:
		ans()

	flagC = 1
	for i in range(usedC+1, N):
		if nowB < C[i]:
			nowC = C[i]
#			print(nowC)
			usedC = i
			flagC = 0
			break
	if flagC:
		ans()

	usedA += 1

	ret += 1