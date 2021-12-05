ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):

	def proc(cs):
		return [int(i) for i in cs.split(",")]

	s = s.split("\n")
	s = [[proc(j) for j in i.split(" -> ")] for i in s]

	grid = 1000
	res = []
	for i in range(grid):
		res.append([0 for j in range(grid)])

	for i in s:
		if i[0][0] != i[1][0] and i[0][1] != i[1][1]:
			p1 = i[0]
			p2 = i[1]
			if p1[0] > p2[0]:
				p1 = i[1]
				p2 = i[0]
			cy = p1[1]
			for j in range(p1[0], p2[0] + 1):
				res[j][cy] += 1
				if p2[1] > p1[1]:
					cy += 1
				else:
					cy -= 1
			continue


		if i[0][0] == i[1][0]:
			for j in range(min(i[0][1], i[1][1]), max(i[0][1], i[1][1]) + 1):
				res[i[0][0]][j] += 1
		else:
			for j in range(min(i[0][0], i[1][0]), max(i[0][0], i[1][0]) + 1):
				res[j][i[0][1]] += 1

	ans = 0
	for i in res:
		# print(i)
		for j in i:
			if j >= 2:
				ans += 1
	return ans







print(solve(ex))
print(solve(f))
