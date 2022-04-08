P = list(map(int, input().split()))
s = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
	print(s[P[i]-1], end='')