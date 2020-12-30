f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

ing = []
allerg = []

for i in range(len(f)):
	f[i] = f[i].split("(")
	f[i][0] = [k for k in f[i][0].split(" ") if k != ""]
	
	f[i][-1] = [k for k in f[i][-1][9:-1].split(", ") if k != ""]
	allerg += f[i][1]


	#print(f[i][-1])
	for j in f[i][0]:
		if j not in ing:
			ing.append(j)

allerg = list(set(allerg))

assoc = {}

posscause = []

import copy
for i in allerg:
	poss = []
	fi = True
	for j in f:
		if i in j[1]:
			if fi:
				poss = copy.deepcopy(j[0])
				fi = False
			else:
				tr = []
				for k in poss:
					if k not in j[0] and k not in tr:
						tr.append(k)
				for k in tr:
					poss.remove(k)

	posscause += poss
	assoc[i] = poss


tot = 0


for i in f:
	for j in i[0]:
		
		if j not in posscause:
			tot += 1

print(tot)

ingtoall = {}
for i in assoc.keys():
	for j in assoc[i]:
		if j in ingtoall.keys():
			ingtoall[j].append(i)
		else:
			ingtoall[j] = [i]


done = {}
for i in ingtoall.keys():
	done[i] = False
	ingtoall[i] = list(set(ingtoall[i]))

while max([len(i) for i in ingtoall.values()]) != 1:
	#print(ingtoall)
	thising = ""
	for k in ingtoall.keys():
		if not done[k] and len(ingtoall[k]) == 1:
			thising = k

	done[thising] = True

	call = ingtoall[thising][0]
	#print(thising, call)

	for i in ingtoall.keys():
		if done[i]:
			continue

		if call in ingtoall[i]:
			ingtoall[i].remove(call)


l = []
for i in ingtoall.keys():
	l.append([ingtoall[i][0], i])

l = sorted(l,key=lambda x: x[0])
s = ""
for i in l:
	s = s + i[1] + ","

print(s)


