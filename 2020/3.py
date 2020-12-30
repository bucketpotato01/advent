f = open('in.txt', "r")
f = f.read().split("\n")
f = [[i for i in j] for j in f]

curr = 0
x = 0
t = 0
while curr < len(f):
	if (f[curr][x] == '#'):
		t += 1
	curr += 2
	x = (x + 1) % len(f[0])

print(t)

