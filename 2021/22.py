ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n")

	# vals = [[[0 for i in range(110)] for j in range(110)] for k in range(110)]

	# for p in s:
	# 	p = p.split(" ")
	# 	v = [[int(k) for k in j[2:].split("..")] for j in p[1].split(",")]

	# 	for i in range(max(-50, v[0][0]), min(51, v[0][1] + 1)):
	# 		for j in range(max(-50, v[1][0]), min(51, v[1][1] + 1)):
	# 			for k in range(max(-50, v[2][0]), min(51, v[2][1] + 1)):
	# 				if p[0] == 'on':
	# 					vals[i + 52][j + 52][k + 52] = 1
	# 				else:
	# 					vals[i + 52][j + 52][k + 52] = 0

	# ans = 0
	# for i in vals:
	# 	for j in i:
	# 		for k in j:
	# 			ans += k

	# return ans

	def remsort(vals):

		res = []
		for i in vals:
			if i not in res:
				res.append(i)
		res.sort()
		return res

	def intersection(cube1, cube2):

		lox = max(cube1[0][0], cube2[0][0])
		hix = min(cube1[0][1], cube2[0][1])

		loy = max(cube1[1][0], cube2[1][0])
		hiy = min(cube1[1][1], cube2[1][1])

		loz = max(cube1[2][0], cube2[2][0])
		hiz = min(cube1[2][1], cube2[2][1])

		if lox > hix or loy > hiy or loz > hiz:
			return None

		return [[lox, hix], [loy, hiy], [loz, hiz]]

	def poss(c1, c2):

		if c2[0] == c1[0] and c2[1] == c1[1]:
			return [c1]
		if c2[0] == c1[0]:
			return [[c2[1] + 1, c1[1]], [c1[0], c2[1]]]
		if c2[1] == c1[1]:
			return [[c1[0], c2[0] - 1], [c2[0], c1[1]]]

		return [[c1[0], c2[0] - 1], [c2[1] + 1, c1[1]], [c2[0], c2[1]]]

	def remove(cube, remcube):

		sgsx = poss(cube[0], remcube[0])
		sgsy = poss(cube[1], remcube[1])
		sgsz = poss(cube[2], remcube[2])

		res = []
		for i in sgsx:
			for j in sgsy:
				for k in sgsz:
					cv = [i, j, k]
					if intersection(cv, remcube) == None:
						res.append(cv)

		return res

	sofar = []

	cdone = 0
	totv = len(s)

	# very slow but at least it works

	for p in s:
		p = p.split(" ")
		v = [[int(k) for k in j[2:].split("..")] for j in p[1].split(",")]
		
		if p[0] == 'on':
			
			ccubes = [v]
			for i in sofar:
				# print("checking", len(ccubes))
				nv = []
				for j in ccubes:
					ci = intersection(i, j)
					if ci != None:
						# print("uwu", i, j)
						nv += (remove(j, ci))
					else:
						nv.append(j)
				ccubes = nv
			sofar += ccubes

		else:
			
			nv = []
			for i in sofar:
				ci = intersection(i, v)
				if ci == None:
					nv.append(i)
				else:
					# print("owo", i, v)
					nv += (remove(i, ci))
			sofar = nv

		cdone += 1
		print(100 * cdone / totv, "done")
		print(len(sofar))

	def mag(cube):
		res = 1
		for i in cube:
			res *= (i[1] - i[0] + 1)
		return res

	ans = 0
	for i in sofar:
		ans += mag(i)
	return ans


# print(solve(ex))
print(solve(f))