ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):

	s = [[j for j in i] for i in s.split("\n")]

	def printf(cs):
		for i in cs:
			for j in i:
				print(j, end="")
			print()

	printf(s)
	print()
	
	def step(cs):

		ns = [['.' for i in range(len(cs[0]))] for j in range(len(cs))]

		tr = []

		for i in range(len(s)):
			for j in range(len(s[i])):
				if s[i][j] == 'v':
					ns[i][j] = 'v'
				if s[i][j] != '>':
					continue
				nc = (j + 1) % len(s[i])
				nr = i

				if cs[nr][nc] != '.':
					tr.append([i, j])
				else:
					tr.append([nr, nc])

		for i in tr:
			ns[i[0]][i[1]] = '>'

		tr = []

		for i in range(len(s)):
			for j in range(len(s[i])):
				if s[i][j] != 'v':
					continue

				nc = j
				nr = (i + 1) % len(s)

				if ns[nr][nc] != '.':
					tr.append([i, j])
				else:
					tr.append([nr, nc])

		for i in range(len(s)):
			for j in range(len(s[i])):
				if ns[i][j] == 'v':
					ns[i][j] = '.'

		for i in tr:
			ns[i[0]][i[1]] = 'v'

		return ns

	cs = 0
	while True:
		ns = step(s)
		if ns == s:
			break
		s = ns
		cs += 1
		# break

	printf(s)

	return cs


# print(solve(ex))
print(solve(f))
