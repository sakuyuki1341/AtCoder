i = list(map(int, input().split()))

n = i[0]
a = i[1]
b = i[2]

s = 0

for k in range(1,n+1):
	count = 0
	tmp_k = k
#	print(k, ":", end=" ")
	for l in range(5):
		count += tmp_k//(10**(4-l))
		tmp_k %= 10**(4-l)
#		print(tmp_k, end=",")

#	print("")
	if (a <= count) and (count <= b):
		s += k

print (s)