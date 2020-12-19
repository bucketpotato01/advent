f = open("in.txt", "r")
f = f.read()

f = f.split("\n\n")

rules = ([i.split(": ") for i in f[0].split("\n")])

strings = f[1].split("\n")



for i in range(len(rules)):
	rules[i][0] = int(rules[i][0])



rules = sorted(rules)

#print([i[0] for i in rules])
lens = [[] for i in rules]
done = [False for i in rules]


def recurse(r):


	#print(r, rules[r][1])
	if done[r] == True:
		#print(r, "is a done")
		return

	if '"' in rules[r][1]:
		#print(r, "is a '")
		lens[r] = [rules[r][1][1]]
		done[r] = True
		return

	elif "|" in rules[r][1]:
		#print(r, "is a |")
		op = rules[r][1].split(" | ")
		op1 = [int(j) for j in op[0].split(" ")]
		op2 = [int(j) for j in op[1].split(" ")]
		#print(op1, op2)

		m1 = [""]
		for i in op1:
			recurse(i)
			temp = []
			for j in m1:
				temp += [j + k for k in lens[i]]
			m1 = temp

		m2 = [""]
		for i in op2:
			recurse(i)
			temp = []
			for j in m2:
				temp += [j + k for k in lens[i]]
			m2 = temp
		#lens[r] = recurse(op1[0]) * recurse(op1[1]) + recurse(op2[0]) * recurse(op2[1])
		lens[r] = m1 + m2
		done[r] = True
		return

	else:
		m = 1
		#print(r,"is a asfd")
		#print([int(j) for j in rules[r][1].split(" ")])
		temp = [""]
		for i in [int(j) for j in rules[r][1].split(" ")]:
			recurse(i)
			temp2 = []
			for j in temp:
				temp2 += [j + k for k in lens[i]]
			temp = temp2


		lens[r] = temp
		done[r] = True
		return m


recurse(42)
recurse(31)

cnt = 0

for i in strings:
	#print(i)
	temp = i
	n31 = 0
	n42 = 0
	while len(temp) >= 8 and temp[-8:] in lens[31]:
		
		temp = temp[:-8]
		n31 += 1

	while len(temp) >= 8 and temp[-8:] in lens[42]:
		temp = temp[:-8]
		n42 += 1

	if temp == "" and n42 > n31 >= 1:
		cnt += 1



#print(ok)
print(cnt)



