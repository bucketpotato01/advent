ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n")

	gamma = 0
	epsilon = 0

	for i in range(len(s[0])):
		zero = 0
		one = 0
		for j in s:
			if j[i] == '0':
				zero += 1
			else:
				one += 1

		if zero > one:
			gamma *= 2
			epsilon += 1
			epsilon *= 2
		else:
			gamma += 1
			gamma *= 2
			epsilon *= 2

	# return (gamma // 2) * (epsilon // 2)

	def tb(bs):
		res = 0
		for i in range(len(bs)):
			if bs[i] == '1':
				res += 1
			res *= 2
		return res // 2

	def oxy(curr, bit):
		if len(curr) == 1:
			return tb(curr[0])

		one = []
		zero = []
		for i in curr:
			if i[bit] == '1':
				one.append(i)
			else:
				zero.append(i)
		if len(one) >= len(zero):
			return oxy(one, bit + 1)
		else:
			return oxy(zero, bit + 1)

	def co2(curr, bit):
		if len(curr) == 1:
			return tb(curr[0])

		one = []
		zero = []
		for i in curr:
			if i[bit] == '1':
				one.append(i)
			else:
				zero.append(i)
		if len(zero) <= len(one):
			return co2(zero, bit + 1)
		else:
			return co2(one, bit + 1)

	return oxy(s, 0) * co2(s, 0)


print(solve(ex))
print(solve(f))
