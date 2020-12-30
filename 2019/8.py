f = open("in.txt", "r")
f = f.read()

W = 25
H = 6
SIZE = W*H

layers = []
for i in range(len(f)):
	if i%SIZE == 0:
		layers.append([])
	layers[-1].append(int(f[i]))


res = 9999999999
ans = 0

for i in layers:
	nz = len([j for j in i if j == 0])
	no = len([j for j in i if j == 1])
	nt = len([j for j in i if j == 2])
	if nz < res:
		ans = no * nt
		res = nz

print(ans)

res = [[2 for i in range(W)] for j in range(H)]

for i in layers:
	layer = []
	for j in range(len(i)):
		if j%W == 0:
			layer.append([])
		layer[-1].append(i[j])

	for j in range(W):
		for k in range(H):
			if res[k][j] == 2:
				res[k][j] = layer[k][j]

for i in res:
	s = ""
	for j in i:
		if j == 0:
			s += " "
		else:
			s += "O"
	print(s)