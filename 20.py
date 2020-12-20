f = open("in.txt", "r")
f = f.read()

f = f.split("\n\n")


for i in range(len(f)):
	f[i] = f[i].split(":\n")
	f[i][1] = [[i for i in j] for j in f[i][1].split("\n")]
	

edges = [[] for i in f]
adj = [[] for i in f]

def d90(a):
	final = []
	for i in range(len(a)-1,-1,-1):
		final.append([])
		for j in range(0, len(a)):
			final[-1].append(a[j][i])
	return final

def sharedge(a, b):

	r, l, u, d = True, True, True, True
	for i in range(len(a)):
		if a[0][i] != b[-1][i]:
			u = False
		if a[-1][i] != b[0][i]:
			d = False
		if a[i][-1] != b[i][0]:
			r = False
		if a[i][0] != b[-1][0]:
			l = False

	return (r or l or d or u)

def fliph(a):
	final = []
	for i in a:
		final.append(i[::-1])
	return final

def flipv(a):
	final = []
	for i in range(len(a)-1,-1,-1):
		final.append(a[i])
	return final

def m(c, p):
	if c == ".":
		return 0
	return 2**p

def borders(a):
	fin = [0 for i in range(4)]
	for i in range(0, len(a)):
		ind = len(a)-1-i
		#print(a)
		#print(ind, len(a), len(a[0]))
		fin[0] += m(a[0][ind], i)
		fin[1] += m(a[ind][-1], i)
		fin[2] += m(a[-1][ind], i)
		fin[3] += m(a[ind][0], i)
	return fin

for i in range(len(f)):
	edges[i] += borders(f[i][1])
	edges[i] += borders(fliph(flipv(f[i][1])))

	#print(edges[i])

ans = 1
corner = -1
for i in range(len(f)):
	for k in edges[i]:
		for j in range(len(f)):
			if j == i:
				continue
			if k in edges[j] and j not in adj[i]:
				adj[i].append(j)
				break

	if len(adj[i]) > 4 or len(adj[i]) <= 2:
		print(adj[i])
		ans *= int(f[i][0].split(" ")[1])
		corner = i








#print(f[0][1])

#print(d90(f[0][1]))




