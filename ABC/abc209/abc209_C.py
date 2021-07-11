from typing import Counter


n = int(input())
c = list(map(int, input().split()))
sorted_c = sorted(c)

count = 1

for i in range(n):
	count = count * (sorted_c[i] - i)
	count %= 1000000007

print(count)