f = open("in.txt", "r")
f = f.read()

f = f.split("\n\n")

p1 = [int(i) for i in f[0].split("\n")[1:]]
p2 = [int(i) for i in f[1].split("\n")[1:]]

# while len(p1) > 0 and len(p2) > 0:
# 	c1 = p1.pop(0)
# 	c2 = p2.pop(0)
# 	if c1 > c2:
# 		p1.append(c1)
# 		p1.append(c2)
# 	else:
# 		p2.append(c2)
# 		p2.append(c1)

def has(l):
	res = 0
	for i in range(len(l)):
		res += l[i] * 1000000007**i
	return res

import copy

def rec(p1, p2):
	print(p1, p2)
	prev1 = set([])
	prev2 = set([])

	while len(p1) > 0 and len(p2) > 0:

		if has(p1) in prev1 or has(p2) in prev2:
			return [1]

		
		prev1.add(has(p1))
		prev2.add(has(p2))


		c1 = p1.pop(0)
		c2 = p2.pop(0)
		print(c1, c2)

		if c1 <= len(p1) and c2 <= len(p2):
			winner = rec(copy.deepcopy(p1[:c1]), copy.deepcopy(p2[:c2]))[0]
			if winner == 1:
				p1.append(c1)
				p1.append(c2)
			else:
				p2.append(c2)
				p2.append(c1)

		else:
			if c1 > c2:
				p1.append(c1)
				p1.append(c2)
			else:
				p2.append(c2)
				p2.append(c1)

	if len(p1) == 0:
		return [2,p2]

	return [1, p1]

game = rec(p1, p2)[1]


res = 0

for i in range(0, len(game)):
	res += (i+1) * game[len(game)-1-i]


print(res)
