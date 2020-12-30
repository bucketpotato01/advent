f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

curr = []
prev = []

curr = [[i for i in j] for j in f]

print(curr)

while curr != prev:
	prev = curr
	curr = [[0 for i in j] for j in f]
	for i in range(len(curr)):
		for j in range(len(curr[i])):
			adj = 0

			for k in range(-1,2):
				for l in range(-1, 2):
					if k == l and k == 0:
						continue

					K = k
					L = l

					while True:
						#print(i+K, j+L)
						if i+K >= 0 and i+K < len(f) and j+L >= 0 and j+L < len(f[i]):
							if prev[i+K][j+L] == "L":
								break
							if prev[i+K][j+L] == '#':
								adj += 1
								break
						else:
							break

						K += k
						L += l

						

			if prev[i][j] == ".":
				curr[i][j] = "."

			elif prev[i][j] == "#":
				if adj >= 5:
					curr[i][j] = "L"
				else:
					curr[i][j] = "#"

			elif prev[i][j] == "L":
				if adj == 0:
					curr[i][j] = "#"
				else:
					curr[i][j] = "L"

	print("ok")

print(curr)
l = 0
for i in curr:
	for j in i:
		if j == "#":
			l += 1

print(l)
