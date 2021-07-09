from typing import Counter


i = [int(input()) for i in range(4)]

count = 0

for num_a in range (i[0] + 1):
	for num_b in range (i[1] + 1):
		for num_c in range (i[2] + 1):
			enn = num_a*500 + num_b*100 + num_c*50
			if enn == i[3]:
				count += 1

print (count)