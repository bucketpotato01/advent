ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

import copy

# ans = 0

def solve(s):
	
	def capital(l):
		return l == l.upper()

	caves = []
	s = [i.split("-") for i in s.split("\n")]
	for i in s:
		if i[0] not in caves:
			caves.append(i[0])
		if i[1] not in caves:
			caves.append(i[1])

	caves.remove("start")
	caves.remove("end")
	caves = ["start"] + caves + ["end"]

	n = len(caves)

	def getind(cs):
		for i in range(len(caves)):
			if caves[i] == cs:
				return i

	graph = [[0 for j in range(n)] for i in range(n)]
	for i in s:
		a = getind(i[0])
		b = getind(i[1])
		graph[a][b] = 1
		graph[b][a] = 1

	# global ans
	ans = 0

	dp = [[0 for i in range(len(caves))] for j in range(1 << (n + 1))]
	dp[1][0] = 1
	ans = 0

	for i in range(0, (1 << (n + 1))):

		for j in range(n):

			if (i & (1 << j)) == 0:
				continue
			if capital(caves[j]):
				continue

			for k in range(n):
				if not capital(caves[k]):
					continue
				if graph[j][k] == 0:
					continue
				if (i & (1 << k)) == 0:
					continue
				dp[i][k] += dp[i][j];

		for j in range(n):
			for k in range(n):
				if graph[j][k] == 0:
					continue
				if (not capital(caves[k])):
					if ((i & (1 << k)) != 0):
						# already visited
						if k == 0 or k == n - 1:
							continue
						if (i & (1 << n)) == 0:
							dp[i + (1 << n)][k] += dp[i][j]
						continue

				if (i & (1 << k) == 0):
					dp[i | (1 << k)][k] += dp[i][j]

		ans += dp[i][n - 1]

	return ans



print(solve(ex))
print(solve(f))
