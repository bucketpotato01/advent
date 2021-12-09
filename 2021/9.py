ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n")

	dr = [-1, 0, 1, 0]
	dc = [0, 1, 0, -1]

	vis = []
	for i in s:
		vis.append([False for i in range(len(s[0]))])

	def dfs(r, c):
		cs = 1
		# print(r, c)
		vis[r][c] = True
		for k in range(4):
			nr = r + dr[k]
			nc = c + dc[k]

			if nr < 0 or nc < 0:
				continue
			if nr >= len(s) or nc >= len(s[0]):
				continue

			# print("considering", nr, nc)
			if vis[nr][nc]:
				# print("visited")
				continue

			if int(s[nr][nc]) < int(s[r][c]) or int(s[nr][nc]) == 9:
				# print("bad")
				continue

			cs += dfs(nr, nc)

		return cs

	def pr(b):
		for i in b:
			for j in i:
				if j:
					print("1", end="")
				else:
					print("0", end="")
			print()

	ans = 0
	basins = []
	for i in range(len(s)):
		for j in range(len(s[i])):
			if vis[i][j] or int(s[i][j]) == 9:
				continue

			clo = 0
			for k in range(4):
				nr = i + dr[k]
				nc = j + dc[k]
				if nr < 0 or nc < 0:
					continue
				if nr >= len(s) or nc >= len(s[i]):
					continue
				if s[nr][nc] <= s[i][j]:
					clo += 1

			if clo != 0:
				continue

			basins.append(dfs(i, j))

			# pr(vis)

			# print("-")

	basins.sort()
	basins = basins[::-1]

	# print(basins)

	return basins[0] * basins[1] * basins[2]

			

	return ans

print(solve(ex))
print(solve(f))
