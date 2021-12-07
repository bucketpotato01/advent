ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	
	def get(pos, crabs):
		tot = 0
		for i in crabs:
			tot += (abs(pos - i) * (abs(pos - i) + 1)) // 2
		return tot

	s = [int(i) for i in s.split(",")]


	ans = get(0, s)
	for i in range(1, 20000):
		ans = min(ans, get(i, s))
	return ans

print(solve(ex))
print(solve(f))
