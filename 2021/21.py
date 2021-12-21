ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	board = 10
	s1 = 0
	s2 = 0
	
	s = [int(i) for i in s.split("\n")]
	v1 = s[0] - 1
	v2 = s[1] - 1

	dp = [[[[0 for i in range(22)] for j in range(22)] for k in range(10)] for l in range(10)]

	dp[v1][v2][0][0] = 1

	def trans(cd, ot):
		
		res = [[[[0 for i in range(22)] for j in range(22)] for k in range(10)] for l in range(10)]

		distrib = [0 for i in range(10)]

		for a in range(1, 4):
			for b in range(1, 4):
				for c in range(1, 4):
					distrib[a + b + c] += 1

		for i in range(10): # ones position
			for j in range(10): # twos position
				for k in range(21): # ones score
					for l in range(21): # twos score

						for x in range(3, 10):

							ni = i
							nj = j
							nk = k
							nl = l

							if ot:
								ni += (x)
								ni %= 10
								nk += (ni + 1)
								nk = min(nk, 21)

							else:
								nj += (x)
								nj %= 10
								nl += (nj + 1)
								nl = min(nl, 21)

							res[ni][nj][nk][nl] += distrib[x] * cd[i][j][k][l]

		return res



	onew = 0
	twow = 0

	oneturn = True
	while True:

		ctot = 0
		for i in range(10):
			for j in range(10):
				for k in range(21):
					onew += dp[i][j][21][k]
					twow += dp[i][j][k][21]

		for i in dp:
			for j in i:
				for k in j:
					for l in k:
						ctot += l

		if ctot == 0:
			break

		print(ctot, onew, twow)

		dp = trans(dp, oneturn)
		oneturn = not oneturn

	return max(onew, twow)


	# cd = 1

	# t1 = True
	# rolls = 0

	# while True:
	# 	if t1:
	# 		for j in range(3):
	# 			rolls += 1
	# 			v1 += cd
	# 			cd += 1
	# 			if cd > 100:
	# 				cd = 1
	# 		v1 %= 10

	# 		s1 += (v1 + 1)
	# 		if s1 >= 1000:
	# 			return s2 * rolls
	# 	else:
	# 		for j in range(3):
	# 			rolls += 1
	# 			v2 += cd
	# 			cd += 1
	# 			if cd > 100:
	# 				cd = 1
	# 		v2 %= 10

	# 		s2 += (v2 + 1)
	# 		if s2 >= 1000:
	# 			return s1 * rolls

	# 	t1 = not t1


# print(solve(ex))
print(solve(f))
