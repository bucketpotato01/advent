f = open("in.txt", "r")
f = f.read()


f = f.split("\n")

bounds = [i.split(": ") for i in f[:20]]

tickets = ([[int(i) for i in j.split(",")] for j in f[25:]])

#print(tickets)

finbounds = []
for i in bounds:
	#print(i)
	j = i[1].split(" or ")
	#print(j)
	j = [[int(k) for k in n.split("-")] for n in j]
	finbounds.append(j[0])
	finbounds.append(j[1])



oktickets = []
tot = 0
for i in tickets:
	thisok = True
	for j in i:
		ok = False
		for k in finbounds:
			if j >= k[0] and j <= k[1]:
				ok = True
		if ok == False:
			tot += j
			thisok = False
	if thisok:
		oktickets.append(i)

finbounds = []
for i in bounds:
	#print(i)
	j = i[1].split(" or ")
	#print(j)
	j = [[int(k) for k in n.split("-")] for n in j]
	finbounds.append(j)

poss = []
for i in range(0, 20):
	poss.append([])
	for j in range(len(oktickets[0])):
		ok = True
		for k in oktickets:
			if k[j] >= finbounds[i][0][0] and k[j] <= finbounds[i][0][1]:
				continue
			elif k[j] >= finbounds[i][1][0] and k[j] <= finbounds[i][1][1]:
				continue
			else:
				ok = False
				break
		if ok:
			poss[-1].append(j)

tick = [191,89,73,139,71,103,109,53,97,179,59,67,79,101,113,157,61,107,181,137]

done = [False for i in poss]

while True:
	ind = -1
	ok = True
	for i in range(len(poss)):
		if len(poss[i]) != 1:
			ok = False
		else:
			if done[i]:
				continue
			ind = i

	if ok:
		break

	if ind == -1:
		print("nope")
		break

	done[ind] = True
	for i in range(len(poss)):
		if poss[ind][0] in poss[i] and done[i] == False:
			poss[i].remove(poss[ind][0])

mult = 1
for i in range(0, 6):
	mult *= tick[poss[i][0]]

print(mult)