ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = [[int(j) for j in i] for i in s.split("\n")]

	rows = len(s)
	cols = len(s[0])

	ns = [[0 for i in range(5 * cols)] for j in range(5 * rows)]

	for i in range(len(ns)):
		for j in range(len(ns[i])):
			ns[i][j] = s[i % rows][j % cols] + ((i // rows) + (j // cols))
			if ns[i][j] > 9:
				ns[i][j] -= 9

	# s = ns
	INF = 99999999999999
	dp = [[INF for i in range(len(ns[0]))] for j in range(len(ns))]
	dp[0][0] = 0
	fin = [[False for i in range(len(ns[0]))] for j in range(len(ns))]

	while True:

		minv = INF + 1
		r = -1
		c = -1
		for i in range(len(dp)):
			for j in range(len(dp[i])):
				if fin[i][j]:
					continue
				if dp[i][j] < minv:
					minv = dp[i][j]
					r = i
					c = j

		# print(r, c)

		if r == -1 and c == -1:
			break

		fin[r][c] = True
		d = dp[r][c]

		if r > 0:
			dp[r - 1][c] = min(dp[r - 1][c], d + ns[r - 1][c])
		if c > 0:
			dp[r][c - 1] = min(dp[r][c - 1], d + ns[r][c - 1])
		if r + 1 < rows * 5:
			dp[r + 1][c] = min(dp[r + 1][c], d + ns[r + 1][c])
		if c + 1 < cols * 5:
			dp[r][c + 1] = min(dp[r][c + 1], d + ns[r][c + 1])

	# for i in dp:
	# 	for j in i:
	# 		print(j, end="")
	# 	print()
	return dp[-1][-1]


	# for i in s:
	# 	for j in i:
	# 		print(j, end="")
	# 	print()

	# for i in range(len(dp)):
	# 	for j in range(len(dp[i])):
	# 		if j == 0 and i == 0:
	# 			continue
	# 		dp[i][j] = 99999999999999999
	# 		if i > 0:
	# 			dp[i][j] = min(dp[i][j], dp[i - 1][j])
	# 		if j > 0:
	# 			dp[i][j] = min(dp[i][j], dp[i][j - 1])
	# 		dp[i][j] += ns[i][j]

	# for i in dp:
	# 	for j in i:
	# 		print(j, end =" ")
	# 	print()

	# return dp[-1][-1]

print(solve(ex))
print(solve(f))
