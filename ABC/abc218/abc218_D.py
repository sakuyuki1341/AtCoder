N = int(input())
P = list()
for _ in range(N):
	P.append(tuple(input().split()))
P.sort()

def is_ok(mid, p):
	if mid > 0:
		return True
	else:
		return False

def binaly_search(ok, ng, p):
	while ng - ok > 1:
		mid = (ok + ng) // 2
		if is_ok(mid, p):
			ok = mid
		else:
			ng = mid
	return ok

for i in range(N):
	for j in range(i+1,N):
		p1 = (P[i][0], P[j][1])
		p2 = (P[j][0], P[i][1])
