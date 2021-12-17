ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	s = [int(i) for i in s.split(" ")]

	def ok(dx, dy):
		cx = 0
		cy = 0

		while cy >= s[2]:
			cx += dx
			cy += dy
			dy -= 1
			dx = max(0, dx - 1)
			if cx >= s[0] and cx <= s[1] and cy >= s[2] and cy <= s[3]:
				return True
		return False

	def sumfrom(a, b):
		if b < a:
			return sumfrom(b, a)
		res = 0
		for i in range(a, b + 1):
			res += i
		return res

	ans = 0
	for dx in range(1, 1000):
		steps = 0
		dist = 0
		while dist < s[0]:
			if steps >= dx:
				break

			dist += (dx - steps)
			steps += 1

		if dist < s[0] or dist > s[1]:
			continue

		minsteps = steps

		while dist <= s[1]:
			if steps >= dx:
				steps = 9999999999999
				break

			dist += (dx - steps)
			steps += 1

		maxsteps = steps

		print(dx, minsteps, maxsteps)

		for j in range(-500, 500):
			
			for k in range(minsteps, maxsteps):
				
				nv = sumfrom(j, j - k + 1)

				if nv < s[2]:
					break
				if nv > s[3]:
					continue
				print(" ",dx, j, "->", nv)
				ans += 1
				break


	return ans

# print(solve(ex))
print(solve(f))
