ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()


def notin(s1, s2): # character in s2 not in s1

	for i in s2:
		if i not in s1:
			return i

def contains(s1, s2): # s2 contains s1?
	for i in s1:
		if i not in s2:
			return False
	return True

def intersection(s1, s2): # character shared between s1, s2
	for i in s1:
		if i in s2:
			return i
	return None

def proc(s):
	nums = [sorted(i) for i in s[0].split(" ")]
	res = [sorted(i) for i in s[1].split(" ")]

	bylen = [[] for i in range(8)]

	for i in nums:
		bylen[len(i)].append(i)

	four = bylen[4][0]
	one = bylen[2][0]
	eight = bylen[7][0]
	seven = bylen[3][0]

	top = notin(one, seven)

	six = -1
	temp = bylen[6]
	for i in temp:
		if contains(one, i):
			continue
		six = i
		bylen[6].remove(i)
		break

	nine = -1
	for i in temp:
		if contains(four, i):
			nine = i
			bylen[6].remove(i)
			break

	zero = bylen[6][0]

	two = -1
	temp = bylen[5]

	for i in temp:
		if contains(i, nine):
			continue
		two = i
		bylen[5].remove(i)
		break

	five = -1
	for i in temp:
		if contains(i, six):
			five = i
			bylen[5].remove(i)
			break

	three = bylen[5][0]

	cn = [sorted(i) for i in [zero, one, two, three, four, five, six, seven, eight, nine]]

	cans = 0
	for i in res:
		print(i)
		cv = -1
		for j in range(len(cn)):
			if cn[j] == i:
				cv = j

		if cv == -1:
			return False
		cans *= 10
		cans += cv

	return cans


def solve(s):
	a = [i.split(" | ") for i in s.split("\n")]

	ans = 0

	for i in a:
		cv = proc(i)
		# print("",cv)
		ans += cv

	return ans

	# unval = [2, 3, 7, 4]

	# for i in a:

	# 	j = i[1].split(" ")
	# 	for k in j:
	# 		if len(k) in unval:
	# 			ans += 1

	# return ans


print(solve(ex))
print(solve(f))
