f = open("in.txt", "r").read()

f = [i.split("\n") for i in f.split("\n\n")]

tot = 0

for i in f:
	a = [m for m in "abcdefghijklmnopqrstuvwxyz"]
	for j in i:
		for k in [m for m in "abcdefghijklmnopqrstuvwxyz"]:
			if k not in j and k in a:
				a.remove(k)

	tot += len(a)
	print(a)

print(tot)