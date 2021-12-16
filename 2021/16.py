ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

ans = 0
cind = 0

def solve(s):

	global ans, cind
	ans = 0
	cind = 0

	res = [i for i in "0123456789ABCDEF"]
	ns = []
	for i in s:
		ind = -1
		for j in range(len(res)):
			if res[j] == i:
				ind = j;
		for k in range(3, -1, -1):
			cv = (1 << k) & ind
			if cv > 0:
				ns.append(1)
			else:
				ns.append(0)

	s = ns


	def proc():

		global ans, cind

		ver = 0
		for i in range(3):
			ver *= 2
			ver += s[cind]
			cind += 1

		typeid = 0
		for i in range(3):
			typeid *= 2
			typeid += s[cind]
			cind += 1

		# print(st, ver, typeid)

		if typeid == 4:
			# literal value
			ans += ver
			cv = 0
			while True:
				isend = s[cind]
				cind += 1
				for i in range(4):
					cv *= 2
					cv += s[cind]
					cind += 1
				if isend == 0:
					break

			return cv

		else:
			ans += ver

			lentypeid = s[cind]
			cind += 1

			vals = []

			if lentypeid == 0:
				numbits = 0
				for i in range(15):
					numbits *= 2
					numbits += s[cind]
					cind += 1

				# print("starting", st, "numbits", numbits)

				cadd = 0
				lind = cind
				while cadd < numbits:
					vals.append(proc())
					cadd += (cind - lind)
					lind = cind
					# print("",cadd)

			else:
				subpackets = 0
				for i in range(11):
					subpackets *= 2
					subpackets += s[cind]
					cind += 1

				for i in range(subpackets):
					vals.append(proc())

			if typeid == 0:
				return sum(vals)
			if typeid == 1:
				res = 1
				for i in vals:
					res *= i
				return res
			if typeid == 2:
				return min(vals)
			if typeid == 3:
				return max(vals)
			if typeid == 5:
				if vals[0] > vals[1]:
					return 1
				return 0
			if typeid == 6:
				if vals[0] < vals[1]:
					return 1
				return 0

			if vals[0] == vals[1]:
				return 1
			return 0



	return proc()
	return ans


print(solve(ex))
print(solve(f))
