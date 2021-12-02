ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = s.split("\n");
	s = [i.split(" ") for i in s]

	hor = 0
	dep = 0
	aim = 0

	for i in s:
		if i[0] == 'forward':
			hor += int(i[1])
			dep += aim * int(i[1])
		if i[0] == 'down':
			aim += int(i[1])
		if i[0] == 'up':
			aim -= int(i[1])

	return hor * dep


print(solve(ex))
print(solve(f))
