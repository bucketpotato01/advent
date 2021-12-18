ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

cind = 0

import copy

def solve(s):
		
	s = s.split("\n")

	def proc(num):

		res = []
		cdep = 0
		for i in num:
			if i == '[':
				cdep += 1
				res.append(-1)
				continue
			if i == ']':
				cdep -= 1
				res.append(-2)
				continue
			if i == ',':
				continue
			cv = int(i)
			res.append(cv)
		return res

	def add(tn1, tn2):
		num1 = copy.deepcopy(tn1)
		num2 = copy.deepcopy(tn2)

		res = [-1] + num1 + num2 + [-2]

		while True:

			changed = False

			cd = 0
			for i in range(len(res)):
				if res[i] == -1:
					cd += 1
					continue
				if res[i] == -2:
					cd -= 1
					continue

				if cd > 4:
					
					cdep = cd
					v1 = res.pop(i)
					v2 = res.pop(i)
					res.pop(i - 1)
					res.pop(i - 1)

					res.insert(i - 1, 0)

					for j in range(i, len(res)):
						if res[j] >= 0:
							res[j] += v2
							break

					for j in range(i - 2, -1, -1):
						if res[j] >= 0:
							res[j] += v1
							break

					changed = True
					break


			if changed:
				continue

			for i in range(len(res)):

				if res[i] == -1:
					cd += 1
					continue
				if res[i] == -2:
					cd -= 1
					continue

				if res[i] > 9:
					
					cv = res.pop(i)
					cdep = cd

					v1 = cv // 2
					v2 = cv - v1
					res.insert(i, -2)
					res.insert(i, v2)
					res.insert(i, v1)
					res.insert(i, -1)

					changed = True
					break

			if not changed:
				break

		return res

	cv = []

	def get(l, r):

		if r - l + 1 == 5:
			return 3 * cv[l + 1] + 2 * cv[l + 2]
		if r - l + 1 == 2:
			return cv[l]

		sp = -1
		cd = 0
		for i in range(l + 1, r):
			if cv[i] == -1:
				cd += 1
			if cv[i] == -2:
				cd -= 1
			if cd == 0:
				sp = i + 1
				break

		return get(l + 1, sp) * 3 + get(sp, r - 1) * 2

	nums = [proc(i) for i in s]

	ans = 0
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i == j:
				continue
			cv = add(nums[i], nums[j])

			ans = max(ans, get(0, len(cv)))

	return ans




print(solve(ex))
print(solve(f))
