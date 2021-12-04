ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n\n");

	order = [int(i) for i in s[0].split(",")]
	s = s[1:]

	boards = []

	def proc(cs):
		res = cs.split(" ")
		tr = []
		# print(res)
		for i in res:
			if i == '':
				continue
			i = "".join([j for j in i if j in "1234567890"])
			tr.append(int(i))
		return tr

	for i in s:
		i = i.split("\n")
		i = [proc(j) for j in i]

		boards.append(i)

	def winning(cb):
		for i in range(len(cb)):
			cw = True
			for j in cb[i]:
				if j != -1:
					cw = False
			if cw:
				return True

		for j in range(len(cb[0])):
			cw = True
			for i in range(len(cb)):
				if cb[i][j] != -1:
					cw = False
			if cw:
				return True

		return False

	def gs(cb):
		res = 0
		for i in cb:
			for j in i:
				if j != -1:
					res += j;
		return res

	for num in order:

		nb = []

		lv = -1

		for i in range(len(boards)):
			for j in range(len(boards[i])):
				for k in range(len(boards[i][j])):
					if boards[i][j][k] == num:
						boards[i][j][k] = -1

			if winning(boards[i]):
				lv = gs(boards[i]) * num
			else:
				nb.append(boards[i])

		boards = nb
		if len(nb) == 0:
			return lv


print(solve(ex))
print(solve(f))
