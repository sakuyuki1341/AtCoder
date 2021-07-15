from typing import Counter


n = int(input())
d = [int(input()) for i in range(n)]

d.sort()

count_mochi = 0
upper_mochi = 0

for i in range(n):
	if upper_mochi < d[i]:
		count_mochi += 1
		upper_mochi = d[i]

print(count_mochi)