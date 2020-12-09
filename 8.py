f = open("in.txt", "r").read()

f = f.split("\n")



f = [i.split(" ") for i in f]



print(f)

for p in range(len(f)):

	if f[p][0] == "acc":
		continue

	if f[p][0] == "jmp":
		f[p][0] = "nop"
	else:
		f[p][0] = "jmp"


	loop = True

	visited = []
	curr = 0
	val = 0
	while (curr not in visited):
		visited.append(curr)
		#print(curr, visited)
		if f[curr][0] == "nop":
			curr += 1
		elif f[curr][0] == "jmp":
			curr += eval(f[curr][1])
		else:
			val += eval(f[curr][1])
			curr += 1

		#print(curr)

		if curr == len(f):
			loop = False
			break


	if f[p][0] == "jmp":
		f[p][0] = "nop"
	else:
		f[p][0] = "jmp"

	if loop == True:
		continue
	else:
		print(val)

