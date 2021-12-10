ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
	
	def get(cs):
		cv = []
		opening = "([{<"

		for i in cs:
			if i in opening:
				cv.append(i)
				continue
			if i == ')':
				if len(cv) == 0 or cv[-1] != '(':
					return 3
				cv = cv[:-1]
			if i == ']':
				if len(cv) == 0 or cv[-1] != '[':
					return 57
				cv = cv[:-1]
			if i == '}':
				if len(cv) == 0 or cv[-1] != '{':
					return 1197
				cv = cv[:-1]
			if i == '>':
				if len(cv) == 0 or cv[-1] != '<':
					return 25137
				cv = cv[:-1]


		return 0

	def get2(cs):
		cv = []
		opening = "([{<"

		for i in cs:
			if i in opening:
				cv.append(i)
				continue
			if i == ')':
				if len(cv) == 0 or cv[-1] != '(':
					return 3
				cv = cv[:-1]
			if i == ']':
				if len(cv) == 0 or cv[-1] != '[':
					return 57
				cv = cv[:-1]
			if i == '}':
				if len(cv) == 0 or cv[-1] != '{':
					return 1197
				cv = cv[:-1]
			if i == '>':
				if len(cv) == 0 or cv[-1] != '<':
					return 25137
				cv = cv[:-1]

		cv = cv[::-1]

		score = 0
		for i in cv:
			score *= 5
			if i == '(':
				score += 1
			if i == '[':
				score += 2
			if i == '{':
				score += 3
			if i == '<':
				score += 4

		return score

	s = s.split("\n")
	ans1 = 0
	ok = []
	for i in s:
		ans1 += get(i)
		if get(i) == 0:
			ok.append(i)

	ans = []
	for i in ok:
		ans.append(get2(i))
	ans.sort()

	return ans[len(ans) // 2]

	

print(solve(ex))
print(solve(f))
