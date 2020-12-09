f = open("in.txt", "r")
f = f.read().split("\n")


l = []
for i in f:
	lor = 0
	hir = 127
	for j in range(7):
		if i[j] == "F":
			hir = (hir + lor)//2
		else:
			lor = 1+(hir + lor)//2

	loc = 0
	hic = 7
	for j in range(7, 10):
		if i[j] == "L":
			hic = (hic + loc)//2
		else:
			loc = 1+(hic+loc)//2

	l.append(hir*8 + loc)

for i in range(0, 822):

	if i-1 in l and i+1 in l and i not in l:
		print(i)

