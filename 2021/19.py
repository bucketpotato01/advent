ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

import copy
import time

def solve(s):
	
	s = [[[int(k) for k in j.split(",")] for j in i.split("\n")[1:]] for i in s.split("\n\n")]
	
	def transform(beacons, orientation, rotation):

		# x, y, z

		perms = [[1, 2, 3], [3, 2, -1],
				 [1, 3, -2], [1, -3, 2],
				 [1, -2, -3], [-3, 2, 1]]

		res = copy.deepcopy(beacons)

		for i in range(len(res)):
			tv = copy.deepcopy(res[i])
			for j in range(3):
				ct = perms[orientation][j]
				res[i][j] = tv[abs(ct) - 1] * (abs(ct) // ct)

			for k in range(rotation):
				tv = copy.deepcopy(res[i])
				res[i][0] = tv[1]
				res[i][1] = -tv[0]

		return res

	def relative(c1, c2):
		return [c2[i] - c1[i] for i in range(len(c2))]

	def add(c1, c2):
		return [c2[i] + c1[i] for i in range(len(c2))]

	# relative to first scanner
	INF = 99999999999999
	def isect(a, b):

		minx = INF
		maxx = -INF
		miny = INF
		maxy = -INF
		minz = INF
		maxz = -INF

		for j in b:
			minx = min(minx, j[0])
			maxx = max(maxx, j[0])
			miny = min(miny, j[1])
			maxy = min(maxy, j[1])
			minz = min(minz, j[2])
			maxz = min(maxz, j[2])

		minxa = INF
		maxxa = -INF
		minya = INF
		maxya = -INF
		minza = INF
		maxza = -INF

		for j in range(len(b)):

			cc = b[j]
			ok = (minx == cc[0] or maxx == cc[0] or 
				  miny == cc[1] or maxy == cc[1] or
				  minz == cc[2] or maxz == cc[2])

			if not ok:
				continue

			resb = set([])
			for k in b:
				resb.add(tuple(relative(b[j], k)))

			for i in range(len(a)):

				resa = []
				cis = 0
				for x in a:
					if tuple(relative(a[i], x)) in resb:
						cis += 1

				if cis >= 12:
					tr = []
					for k in resb:
						tr.append(add(list(k), a[i]))
					rel = relative(b[j], a[i])
					return [tr, rel]

		return [[], []]

	nois = []
	ans = [s[0]]
	s = s[1:]
	cds = [[0, 0, 0]]

	while len(ans) > 0:
		j = ans[0]

		nobad = []

		ct1 = time.time()

		while len(s) > 0:
			i = s[0]

			found = False
			for o1 in range(6):
				if found:
					break
				for r1 in range(4):
					if found:
						break

					cv1 = transform(i, o1, r1)

					nv = isect(j, cv1)

					if len(nv[0]) != 0:
						found = True
						ans.append(nv[0])
						cds.append(nv[1])

			s.remove(i)

			if not found:
				nobad.append(i)

		

		nois.append(j)
		ans.remove(j)
		s = nobad + s

		ct2 = time.time()
		print("time elapsed,", ct2 - ct1)

	rv = []
	for i in ans + nois:
		for j in i:
			if j not in rv:
				rv.append(j)

	ans2 = 0
	for i in cds:
		for j in cds:
			ans2 = max(ans2, sum([abs(i[k] - j[k]) for k in range(3)]))

	return ans2

	return len(rv)



print(solve(ex))
print(solve(f))
