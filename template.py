import math

# 入力---------------------------------------------
"""
# 1行に1つの文字列の入力を取得し、出力する
s = input()
#print(s)
"""

"""
# 1行に1つの整数の入力を取得し、整数として出力する
i = int(input())
#print(i)
"""

"""
# 1行に複数の入力値を取得し、出力する
s = input().split()
#print(s)
"""

"""
# 1行に複数の整数の入力を取得し、整数として出力する
i = list(map(int, input().split()))
#print(i)
"""

"""
# 複数行に複数の入力値を取得し、出力する
s = [input() for i in range(n)] #nは場合に応じて定数を入れる
#print(s)
"""

"""
# 最初に入力回数、次に入力値を取得し、出力する
N = int(input())
s = [input() for i in range(N)]
#print(s)
"""

"""
# 最初に入力行数、次に入力値を複数取得し、出力する
N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
#print(s)
"""
# -------------------------------------------------


# 二部探索------------------------------------------
"""
def is_ok(mid):
	if mid > 0:
		return True
	else:
		return False

def binaly_search(ok, ng):
	while ng - ok > 1:
		mid = (ok + ng) // 2
		if is_ok(mid):
			ok = mid
		else:
			ng = mid
	return ok
"""
# -------------------------------------------------
