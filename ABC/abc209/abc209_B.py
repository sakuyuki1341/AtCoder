NX = list(map(int, input().split()))
A = list(map(int, input().split()))

prise = sum(A) - NX[0]/2

if prise > NX[1]:
	print("No")
else:
	print("Yes")