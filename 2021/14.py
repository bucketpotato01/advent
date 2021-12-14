ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

import copy

def solve(s):
	s = s.split("\n\n")

	curr = s[0]
	ins = [i.split(" -> ") for i in s[1].split("\n")]

	cntp = [[0 for i in range(26)] for j in range(26)]
	

	for i in range(1, len(curr)):
		v1 = ord(curr[i - 1]) - ord("A")
		v2 = ord(curr[i]) - ord("A")
		cntp[v1][v2] += 1

	def dostep(cf, ins):
		nf = [[0 for i in range(26)] for j in range(26)]
		
		nins = []

		for i in ins:
			r = ord(i[0][0]) - ord("A")
			c = ord(i[0][1]) - ord("A")
			fv = ord(i[1]) - ord("A")
			nins.append([[r, c], fv])

		for i in range(26):
			for j in range(26):
				if cf[i][j] == 0:
					continue
				ik = -1
				for k in range(len(nins)):
					if nins[k][0] == [i, j]:
						ik = k
						break
				if ik == -1:
					nf[i][j] += cf[i][j]
				else:
					# print(ins[ik])
					ov = nins[k][1]
					nf[i][ov] += cf[i][j]
					nf[ov][j] += cf[i][j]

		# cv = 0
		# for i in nf:
		# 	for j in i:
		# 		print(j, end="")
		# 		cv += j
		# 	print()

		# print(cv)

		return nf


	for i in range(40):
		cntp = dostep(cntp, ins)


	cnt = [0 for i in range(26)]
	for i in range(26):
		for j in range(26):
			cnt[i] += cntp[i][j]
			cnt[j] += cntp[i][j]

	iv1 = ord(curr[0]) - ord("A")
	iv2 = ord(curr[-1]) - ord("A")

	cnt[iv1] += 1
	cnt[iv2] += 1

	# print(cnt)

	maxv = -1
	minv = 10 ** 20
	for j in cnt:
		if j == 0:
			continue
		maxv = max(maxv, j // 2)
		minv = min(minv, j // 2)

	return maxv - minv


print(solve(ex))
print(solve(f))
