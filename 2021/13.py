ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

dots = []

def solve(s):
	global dots
	s = s.split("\n\n")
	dots = [[int(j) for j in i.split(",")] for i in s[0].split("\n")]

	SIZE = 1500
	cv = [[0 for i in range(SIZE)] for j in range(SIZE)]

	def foldx(coord):
		newdots = []
		global dots
		for i in dots:
			x = i[0]
			y = i[1]
			if x < coord:
				if [x, y] not in newdots:
					newdots.append([x, y])
			else:
				nv = [coord - (x - coord), y]
				if nv not in newdots:
					newdots.append(nv)
		dots = newdots

	def foldy(coord):
		newdots = []
		global dots
		for i in dots:
			x = i[0]
			y = i[1]
			if y < coord:
				if [x, y] not in newdots:
					newdots.append([x, y])
			else:
				nv = [x, coord - (y - coord)]
				if nv not in newdots:
					newdots.append(nv)
		dots = newdots

	ins = [i.split(" ")[2].split("=") for i in s[1].split("\n")]
	
	for i in ins:
		if i[0] == 'y':
			foldy(int(i[1]))
		else:
			foldx(int(i[1]))

	message = [[' ' for i in range(50)] for j in range(50)]

	for j in dots:
		message[j[0]][j[1]] = '*'

	for j in range(50):
		for i in range(50):
			print(message[i][j], end="")
		print()

	return len(dots)



print(solve(ex))
print(solve(f))
