f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

def nextins(s):
	if s[0] == "s":
		return s[:2], s[2:]
	if s[0] == "n":
		return s[:2], s[2:]
	return s[0], s[1:]

def neighbors(x, y):
	return [[x+1,y-1],[x,y-1],[x+1,y],[x-1,y],[x,y+1],[x-1,y+1]]


c = {}

for i in f:
	x, y = 0, 0
	while i != "":
		ins, i = nextins(i)
		if ins == "se":
			x += 1
			y -= 1
		elif ins == "sw":
			y -= 1
		elif ins == "e":
			x += 1
		elif ins == "w":
			x -= 1
		elif ins == "ne":
			y += 1
		else:
			y += 1
			x -= 1
	if x not in c:
		c[x] = {}
	if y not in c[x]:
		c[x][y] = 1
	else:
		c[x][y] += 1

ans = 0
black = []
for i in c.keys():
	m = c[i]
	for j in m.keys():
		if m[j] % 2 == 1:
			black.append([i, j])


for i in range(100):

	temp = {}
	for j in black:
		for k in neighbors(j[0], j[1]):
			if k[0] not in temp:
				temp[k[0]] = {}
			if k[1] not in temp[k[0]]:
				temp[k[0]][k[1]] = 0
			temp[k[0]][k[1]] += 1

	newblack = []
	for x in temp.keys():
		j = temp[x]
		for y in j.keys():
			v = j[y]
			if [x,y] in black:
				if 0 < v <= 2:
					newblack.append([x,y])
			else:
				if v == 2:
					newblack.append([x,y])

	black = newblack

	print(len(black))

				





