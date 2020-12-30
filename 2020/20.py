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

def crop(img):
	img = img[1:-1]
	for i in range(len(img)):
		img[i].pop(-1)
		img[i].pop(0)
	return img

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
		#print(adj[i])
		ans *= int(f[i][0].split(" ")[1])
		corner = i


fin = [[[] for i in range(40)] for i in range(40)]
done = [False for i in f]
fin[20][20] = f[corner][1]
done[corner] = True
#print(fin[20][20])



q = adj[corner]

while len(q) > 0:
	thisone = q.pop(0)
	matched = False
	done[thisone] = True
	for i in range(len(fin)):
		if matched:
			break
		for j in range(len(fin)):
			if matched:
				break
			if fin[i][j] == []:
				continue


			for rot in range(0, 4):
				if matched:
					break
				for fh in range(0, 2):
					if matched:
						break
					for fv in range(0, 2):
						if matched:
							break
						temp = f[thisone][1]
						for k in range(rot):
							temp = d90(temp)
						if fh == 1:
							temp = fliph(temp)
						if fv == 1:
							temp = flipv(temp)

						if temp[0] == fin[i][j][-1]:
							fin[i+1][j] = temp
							matched = True

						elif [k[0] for k in (temp)] == [k[-1] for k in fin[i][j]]:
							fin[i][j+1] = temp
							matched = True

						elif [k[-1] for k in (temp)] == [k[0] for k in fin[i][j]]:
							fin[i][j-1] = temp
							matched = True

						elif temp[-1] == fin[i][j][0]:
							fin[i-1][j] = temp
							matched = True
	#print(thisone, matched)
	for i in adj[thisone]:
		if i not in q and not done[i]:
			q.append(i)

image = []

for i in range(40):
	thisrow = []
	for j in range(40):
		if fin[i][j] != []:
			thisrow.append(crop(fin[i][j]))

	if thisrow == []:
		continue

	for j in range(len(thisrow[0])):
		image.append([])
		for k in range(len(thisrow)):
			image[-1] = image[-1] + thisrow[k][j]


seamonster = [[j for j in i] for i in "                  # \n#    ##    ##    ###\n #  #  #  #  #  #   ".split("\n")]
print(seamonster)
def matchmonster(grid, i, j, seamonster):

	
	for x in range(len(seamonster)):
		for y in range(len(seamonster[x])):
			if seamonster[x][y] != "#":
				continue

			#print(x,y)
			if i+x >= len(grid) or j+y >= len(grid[i+x]):
				return False
			if grid[i+x][j+y] != "#":
				return False

	return True

seasize = sum([len([i for i in j if i == "#"]) for j in seamonster])
print(seasize)

for j in range(4):
	for k in range(2):
		for l in range(2):
			temp = image
			for n in range(j):
				temp = d90(temp)
			if k == 1:
				temp = fliph(temp)
			if l == 1:
				temp = flipv(temp)

			seamonsters = 0
			spaces = 0
			for i in range(len(image)):
				for j in range(len(image)):
					if matchmonster(temp, i, j, seamonster):
						seamonsters += 1
					if temp[i][j] == "#":
						spaces += 1

			print(spaces - seasize * seamonsters)






#print(f[0][1])

#print(d90(f[0][1]))




