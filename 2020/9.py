f = open("in.txt", "r").read()

f = f.split("\n")
f = [int(i) for i in f]

print(f)

for i in range(1, 503):
	for j in range(i-1, 503):
		s = 0
		lo = 9999999999
		hi = -1
		for k in range(j-i, j):
			s += f[k]
			hi = max(hi, f[k])
			lo = min(lo, f[k])
		if s == 26134589:
			print(hi, lo)

