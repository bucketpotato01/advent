f = open("in.txt", "r")
f = f.read().split("\n")

f = [int(i) for i in f]

def fuel(a):
	tf = (a//3) - 2
	print(a)
	if tf <= 0:
		return 0
	return tf + fuel(tf)

ans = sum([fuel(i) for i in f])
print(ans)