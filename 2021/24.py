ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):

	s = s.split("inp w\n")

	def op(ty, a, b):
		# print("trying", ty, a, b)

		if ty == "add":
			return a + b

		if ty == "mul":
			return a * b

		if ty == "div":
			if b == 0:
				# print("nope")
				return None
			if a == 0:
				return 0
			return (abs(a) // b) * (abs(a) // a)

		if ty == "mod":
			if a < 0 or b <= 0:
				# print("nono")
				return None
			return a % b

		if a == b:
			return 1
		return 0

	s = [i.split("\n")[:-1] for i in s][1:]

	print(s[0])
	curr = {0 : 0}
	curro = {}
	for i in s:

		# print(curr)
		v2 = int(i[3].split(" ")[2])
		v1 = int(i[4].split(" ")[2])
		v3 = int(i[-3].split(" ")[2])

		if v2 == 1:
			nc = {}
			nco = {}
			for j in curr.keys():
				for w in range(1, 10):
					nz = 26 * j + (w + v3)
					if nz in nc.keys():
						nc[nz] = min(nc[nz], curr[j] * 10 + w)
					else:
						nc[nz] = curr[j] * 10 + w

			for j in curro.keys():
				for w in range(1, 10):
					nz = 26 * j + (w + v3)
					if nz in nco.keys():
						nco[nz] = min(nco[nz], curro[j] * 10 + w)
					else:
						nco[nz] = curro[j] * 10 + w

			curr = nc
			curro = nco

		else:
			nc = {}
			nco = {}
			for j in curr.keys():
				cvv = (j % 26) + v1

				for w in range(1, 10):
					if w != cvv:
						nz = (j + w + v3)
						nj = curr[j] * 10 + w
						if nz in nco.keys():
							nco[nz] = min(nco[nz], nj)
						else:
							nco[nz] = nj


				if cvv > 9 or cvv <= 0:
					continue
				nz = j // 26
				if nz in nc.keys():
					nc[nz] = min(nc[nz], curr[j] * 10 + cvv)
				else:
					nc[nz] = curr[j] * 10 + cvv

			for j in curro.keys():
				cvv = (j % 26) + v1

				if cvv > 9 or cvv <= 0:
					continue
				nz = j // 26
				if nz in nco.keys():
					nco[nz] = min(nco[nz], curro[j] * 10 + cvv)
				else:
					nco[nz] = curro[j] * 10 + cvv



			curr = nc
			curro = nco



		# print(curr)
		# print("!")
		# nv = {}
		# for j in curr.keys():

		# 	for k in range(1, 10):
		# 		cvals = [k, 0, 0, j]

		# 		cok = True
		
		# 		for ins in i:

		# 			# print(ins)
		# 			ins = ins.split(" ")
		# 			b = ins[2]
		# 			if b in "wxyz":
		# 				b = cvals["wxyz".index(b)]
		# 			else:
		# 				b = int(b)
		# 			a = ins[1]
		# 			a = "wxyz".index(a)
		# 			cvals[a] = op(ins[0], cvals[a], b)
		# 			# print(cvals[a])

		# 			if cvals[a] == None:
		# 				# print("bad")
		# 				cok = False
		# 				break

		# 		cval = j * 10 + k
		# 		cz = cvals[3]
		# 		if cz in nv.keys():
		# 			nv[cz] = min(nv[cz], cval)
		# 		else:
		# 			nv[cz] = cval
		# curr = nv
	print(curro)

	ans = 10**100
	if 0 in curr.keys():
		ans = curr[0]
	if 0 in curro.keys():
		ans = min(ans, curro[0])

	return ans



# print(solve(ex))
print(solve(f))
