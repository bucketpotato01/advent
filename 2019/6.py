f = open("in.txt", "r")
f = f.read()

f = [i.split(")") for i in f.split("\n")]

orbits = {}
parents = {}
for i in f:
	if i[0] in orbits.keys():
		orbits[i[0]].append(i[1])
	else:
		orbits[i[0]] = [i[1]]

	if i[1] not in orbits.keys():
		orbits[i[1]] = []

	parents[i[1]] = i[0]

def ans(c, l, d):
	thisone = d
	for i in orbits[c]:
		if i == l:
			continue
		thisone += ans(i, c, d+1)
	return thisone


path1 = ["YOU"]
while path1[-1] != "COM":
	path1.append(parents[path1[-1]])

path2 = ["SAN"]
while path2[-1] != "COM":
	path2.append(parents[path2[-1]])

res = 0
for i in range(len(path1)):
	if path1[i] in path2:
		res = i + path2.index(path1[i])
		break

print(res - 2)
