f = open("in.txt", "r")
f = f.read()

f = [int(i) for i in f.split(",")]

def run(f, putin, retonerror=True):

	def val(a, m):
		if m == 0: # position
			return f[a]
		if m == 1: # immediate
			return a

	i = 0
	currinput = 0
	output = []

	params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3}

	while True:

		operation = f[i]%100
		p1 = (f[i]//100)%10
		p2 = (f[i]//1000)%10
		p3 = (f[i]//10000)%10

		doskip = True

		#print(i)

		if operation == 1:
			a, b, pos = val(f[i+1], p1), val(f[i+2], p2), f[i+3]
			f[pos] = a+b

		elif operation == 2:
			a, b, pos = val(f[i+1], p1), val(f[i+2], p2), f[i+3]
			#print(a, b, pos)
			f[pos] = a*b

		elif operation == 3:
			pos = val(i+1,p1)
			if currinput >= len(putin) and retonerror:
				return output

			f[pos] = putin[currinput]

			currinput += 1

		elif operation == 4:
			pos = val(i+1,p1)
			output.append(f[pos])

		elif operation == 5:
			boolean = val(f[i+1], p1)
			if boolean != 0:
				pos = val(f[i+2], p2)
				i = pos
				doskip = False

		elif operation == 6:
			boolean = val(f[i+1], p1)
			if boolean == 0:
				pos = val(f[i+2], p2)
				i = pos
				doskip = False

		elif operation == 7:
			v1, v2 = val(f[i+1], p1), val(f[i+2], p2)
			v3 = f[i+3]

			if v1 < v2:
				f[v3] = 1
			else:
				f[v3] = 0

		elif operation == 8:
			v1, v2 = val(f[i+1], p1), val(f[i+2], p2)
			v3 = f[i+3]

			if v1 == v2:
				f[v3] = 1
			else:
				f[v3] = 0



		elif operation == 99:
			break


		else:
			print(operation)
			print("uh oh")
			print(f)
			if retonerror:
				return output
			break

		if doskip:
			i += params[operation] + 1

	#print(f)
	return output


import copy

perms = [[]]
for i in range(5):
	newone = []
	for k in range(5,10):
		for j in perms:
			if k not in j:
				newone.append(j + [k])
	perms = newone


ans = 0
for i in perms:
	bs = [[i[j]] for j in range(5)]
	bs[0] += [0]

	inputs = copy.deepcopy(bs)

	c = 0
	while (True):

		prev = (c - 1 + 5) % 5
		o = run(copy.deepcopy(f), inputs[c])

		

		c = (c + 1) % 5

		newoutp = bs[c] + o
		if newoutp == inputs[c]:
			break
		inputs[c] = newoutp

		#print(inputs[c], c)

	ans = max(ans, inputs[0][-1])
	
	#print(c)

print(ans)

