f = open("in.txt", "r")

f = f.read()

f = f.split("\n")

def tonum(a):
	fin = 0
	for i in range(len(a)):
		fin += (a[i] + 1000) * (1000**i)
	return fin

active = []
activehas = set([])

for i in range(len(f)):
	for j in range(len(f)):
		if f[i][j] == "#":
			active.append([i,j,0,0])
			activehas.add(tonum([i,j,0,0]))



newactive = []
cnt = []
has = {}

for i in range(6):
	#print(active, activehas)
	print(i)
	for j in active:
		for x in range(-1, 2):
			for y in range(-1, 2):
				for z in range(-1, 2):
					for w in range(-1, 2):
						if x == y == z == w == 0:
							continue
						thisone = [j[0]+x, j[1]+y, j[2]+z, j[3]+w]
						numvers = tonum(thisone)

						if numvers in has.keys():
							ind = has[numvers]
							#print(len(cnt), len(newactive), ind, has)
							cnt[ind] += 1

						else:
							has[numvers] = len(newactive)
							newactive.append([j[0]+x, j[1]+y, j[2]+z, j[3]+w])
							
							cnt.append(1)

	temp = []
	temphas = set([])

	for j in range(len(cnt)):
		if tonum(newactive[j]) in activehas:
			if 2 <= cnt[j] <= 3:
				temp.append(newactive[j])
				temphas.add(tonum(newactive[j]))

		else:
			if cnt[j] == 3:
				temp.append(newactive[j])
				temphas.add(tonum(newactive[j]))


	active = temp
	cnt = []
	newactive = []
	activehas = temphas
	has = {}

print(len(active))


