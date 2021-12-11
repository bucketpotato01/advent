ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

import copy

def solve(s, steps = 1000000):
	s = [[int(j) for j in i] for i in s.split("\n")]

	ans = 0
	for t in range(steps):

		ns = copy.deepcopy(s)
		flash = [[0 for i in range(10)] for j in range(10)]

		for i in range(10):
			for j in range(10):
				ns[i][j] += 1

		while True:
			
			# print("this step")
			ca = []
			for i in range(10):
				for j in range(10):
					if flash[i][j] != 0:
						continue

					if ns[i][j] > 9:
						flash[i][j] = 1
						ans += 1
						# print(i, j)
						ca.append([i, j])

			if len(ca) == 0:
				break

			for p in ca:
				for i in range(-1, 2):
					for j in range(-1, 2):
						if i == 0 and j == 0:
							continue

						r = i + p[0]
						c = j + p[1]

						# if p[0] == 0 and p[1] == 2:
						# 	print("e",r, c)

						if r < 0 or c < 0 or c >= 10 or r >= 10:
							continue
						if flash[r][c] == 1:
							continue


						
						ns[r][c] += 1


		cf = 0
		for i in range(10):
			for j in range(10):
				if flash[i][j] == 1:
					ns[i][j] = 0
					cf += 1

		# for i in ns:
		# 	for j in i:
		# 		print(j,end="")
		# 	print()
		# print("-")

		if cf == 100:
			return t + 1

		s = ns

	return ans
					



print(solve(ex))
print(solve(f))
