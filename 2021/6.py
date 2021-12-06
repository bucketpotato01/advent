ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s, days = 256):
	res = [int(i) for i in s.split(",")]
	cnt = [0 for i in range(10)]

	for i in res:
		cnt[i] += 1

	for i in range(days):
		nv = [0 for i in range(10)]
		for j in range(1, len(cnt)):
			nv[j - 1] += cnt[j]
		nv[6] += cnt[0]
		nv[8] += cnt[0]
		cnt = nv

	return sum(cnt)

print(solve(ex))
print(solve(f))
