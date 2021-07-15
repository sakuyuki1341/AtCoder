n = int(input())
a = list(map(int, input().split()))

a.sort()
#print(a)

score_alice = 0
score_bob = 0

for i in range(n):
	if i%2 == 0:
		score_alice += a[n-i-1]
	else:
		score_bob += a[n-i-1]

print(score_alice-score_bob)