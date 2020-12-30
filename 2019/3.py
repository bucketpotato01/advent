f = open("in.txt", "r")
f = f.read().split("\n")

f = [i.split(",") for i in f]


BIGGUSDICKUS = 10**10
SMALLERBIGGUSDICKUS = 10**6

def tonum(a, b):
	return (a*BIGGUSDICKUS) + b

def fromnum(a):
	b = a%BIGGUSDICKUS
	a = a // BIGGUSDICKUS
	return [a, b]

def getpath(a):
	res = set([])
	pointtostep = {}

	cx = SMALLERBIGGUSDICKUS
	cy = SMALLERBIGGUSDICKUS
	for i in a:
		dx, dy = 0, 0
		if i[0] == "D":
			dy = -1
		elif i[0] == "U":
			dy = 1
		elif i[0] == "L":
			dx = -1
		elif i[0] == "R":
			dx = 1

		for j in range(int(i[1:])):
			cx += dx
			cy += dy
			res.add(tonum(cx,cy))
			if tonum(cx,cy) not in pointtostep.keys():
				pointtostep[tonum(cx,cy)] = len(res)

	return res, pointtostep

m, p1 = getpath(f[0])
n, p2 = getpath(f[1])

ans = BIGGUSDICKUS

for i in m:
	if i in n:
		a = p1[i] + p2[i]
		ans = min(ans, a)

print(ans)

