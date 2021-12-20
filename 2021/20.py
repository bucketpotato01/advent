ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n\n")

	en = s[0]
	s = s[1].split("\n")
	n = len(s)
	m = len(s[0])

	curr = s

	def step(cg, bb):

		cn = len(cg)
		cm = len(cg[0])

		ex = 1

		res = [['' for i in range(cm + ex * 2)] for j in range(cn + ex * 2)]
		for i in range(cn + ex * 2):
			for j in range(cm + ex * 2):

				r = i - ex
				c = j - ex

				cv = 0
				for dx in range(-1, 2):
					for dy in range(-1, 2):
						cr = r + dx
						cc = c + dy
						cv *= 2
						if cr < 0 or cc < 0 or cr >= cn or cc >= cm:
							if cb:
								cv += 1
							continue
						if cg[cr][cc] == '#':
							cv += 1

				res[i][j] = en[cv]

		return res


	cb = False
	for i in range(50):
		print(i)
		curr = step(curr, cb)
		cb = not cb

	ans = 0
	for i in curr:
		for j in i:
			if j == '#':
				ans += 1
	return ans

					



# print(solve(ex))
print(solve(f))
