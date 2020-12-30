f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

f = [[i[0], int(i[1:])] for i in f]

x = 0
y = 0
di = 0

wx = 10
wy = 1

for i in f:
	if (i[0] == "N"):
		wy += i[1]

	if i[0] == "E":
		wx += i[1]
	if i[0] == "W":
		wx -= i[1]
	if i[0] == "S":
		wy -= i[1]
		
	if i[0] == "L":
		d = (360 - i[1])%360
		if d == 90:
			wx, wy = wy, -wx
		elif d == 180:
			wx, wy = -wx, -wy
		elif d == 270:
			wx, wy = -wy, wx
		else:
			continue

		

	if i[0] == "R":
		d = i[1]


		if d == 90:
			wx, wy = wy, -wx
		elif d == 180:
			wx, wy = -wx, -wy
		elif d == 270:
			wx, wy = -wy, wx
		else:
			continue

		

	if i[0] == "F":

		x += i[1] * wx
		y += i[1] * wy



print(abs(x)+abs(y))
print(x,y)

