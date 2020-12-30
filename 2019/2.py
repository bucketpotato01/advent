f = open("in.txt", "r")
f = f.read().split(",")

f = [int(i) for i in f]

def run(f):
	i = 0
	while (f[i] != 99):

		if f[i] == 1:
			a, b, pos = f[f[i+1]], f[f[i+2]], f[i+3]
			f[pos] = a+b

		elif f[i] == 2:
			a, b, pos = f[f[i+1]], f[f[i+2]], f[i+3]
			f[pos] = a*b

		else:
			print("uh oh")
			print(f)
			break
		i += 4
	return f

import copy
for i in range(100):
	for j in range(100):
		temp = copy.deepcopy(f)
		temp[1] = i
		temp[2] = j
		temp = run(temp)
		if temp[0] == 19690720:
			print(i, j, 100*i+j)