S = input()

while 1:
	if S == "":
		print("YES")
		exit()
	if S.endswith("dream"):
		S = S[:-len("dream")]
		continue
	if S.endswith("dreamer"):
		S = S[:-len("dreamer")]
		continue
	if S.endswith("erase"):
		S = S[:-len("erase")]
		continue
	if S.endswith("eraser"):
		S = S[:-len("eraser")]
		continue

	print("NO")
	exit()