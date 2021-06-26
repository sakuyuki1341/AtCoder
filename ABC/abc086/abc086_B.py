import math

i = int(input().replace(' ', ''))
sq = math.sqrt(i)

if sq.is_integer():
	print("Yes")
else:
	print("No")