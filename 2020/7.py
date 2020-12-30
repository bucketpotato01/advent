f = open("in.txt", "r").read()
f = f.split("\n")

f = [i.split(" contain ") for i in f]

typeshad = []

types = []
curr = [[1,"shiny gold bag"]]
temp = []
'''
while len(curr) > 0:
	for i in curr:
		for j in f:
			if i in j[1] and j[0] not in temp and j[0] not in types and j[0] not in curr:
				j[0] = j[0][:-5]

				temp.append(j[0])
				print(j[0])


	for i in curr:
		types.append(i)

	curr = temp
	temp = []

types = list(set(types))

print(len(types))
'''

while len(curr) > 0:
	for i in curr:
		for j in f:
			if i[1] in j[0]:
				if "no other bags" in j[1]:
					continue
				for k in j[1].split(", "):
					n = k.split(" ")
					a = int(n[0])
					print(a)
					temp.append([i[0]*a, " ".join(n[1:])[:-1]])
	for i in curr:
		types.append(i)
	curr= temp
	temp = []

tot = 0
for i in types:
	tot += i[0]

print(tot)