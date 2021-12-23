ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

import copy
import sys
sys.setrecursionlimit(100000)

goal = """#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########""".split("\n")



def h(cs):
	res = 0
	cp = 1
	for i in cs:
		for j in i:
			if j in ".ABCD":
				cv = 0
				if j == 'A':
					cv = 1
				if j == 'B':
					cv = 2
				if j == 'C':
					cv = 3
				if j == 'D':
					cv = 4
				res += (cv * cp)
				cp *= 5
	return res

def solve(s):
	s = [[j for j in i] for i in s.split("\n")]

	ass = {h(s) : 0}

	posshall = [[1, 1], [1, 2], [1, 4], [1, 6], [1, 8], [1, 10], [1, 11]]
	rooms = [3, 5, 7, 9]

	def canmove(cs, r1, c1, r2, c2):

		o = [[-1 for i in range(len(cs[0]))] for j in range(len(cs))]

		def dfs(r, c, cd):
			dr = [0, 1, 0, -1]
			dc = [1, 0, -1, 0]
			o[r][c] = cd
			for i in range(4):
				nr = r + dr[i]
				nc = c + dc[i]
				if nr < 0 or nc < 0:
					continue
				if nr >= len(o) or nc >= len(o[0]):
					continue
				if cs[nr][nc] != '.':
					continue
				if o[nr][nc] != -1:
					continue
				dfs(nr, nc, cd + 1)

		dfs(r1, c1, 0)
		return (o[r2][c2])

	def printf(s):
		for i in s:
			for j in i:
				print(j, end="")
			print()

	
	def ndfs(cs, cd):
		
		# amphipod moves from room into hall

		printf(cs)

		for c1 in rooms:
			
			for r1 in range(2, len(cs) - 1):

				if cs[r1][c1] == '.':
					continue

				cok = False
				ci = ((c1 - 1) // 2) - 1
				for j in range(r1 + 1, len(cs) - 1):
					if cs[j][c1] == '.':
						continue
					if cs[j][c1] != cs[r1][c1]:
						cok = True
				if ci != ord(cs[r1][c1]) - ord('A'):
					cok = True

				if not cok:
					continue

				for j in posshall:
					r2 = j[0]
					c2 = j[1]
					if cs[r2][c2] != '.':
						continue
					nd = canmove(cs, r1, c1, r2, c2)
					if nd == -1:
						continue

					newstate = copy.deepcopy(cs)
					newstate[r1][c1] = '.'
					newstate[r2][c2] = cs[r1][c1]

					nh = h(newstate)
					ccost = cd + nd * (10 ** (ord(cs[r1][c1]) - ord('A')))

					if nh not in ass.keys() or ccost < ass[nh]:
						ass[nh] = ccost
						ndfs(newstate, ccost)

		# amphipod moves from hall into room

		for i in posshall:
			r1 = i[0]
			c1 = i[1]
			if cs[r1][c1] == '.':
				continue
			
			j = ord(cs[r1][c1]) - ord('A')

			req = -1
			he = True

			for k in range(2, len(cs) - 1):
				if cs[k][rooms[j]] == '.':
					continue
				if ord(cs[k][rooms[j]]) - ord('A') != j:
					he = False
					break

			if not he:
				continue

			for k in range(2, len(cs) - 1):
				if cs[k][rooms[j]] != '.':
					break
				req = k

			if req == -1:
				continue

			r2 = req
			c2 = rooms[j]

			
			nd = canmove(cs, r1, c1, r2, c2)

			if nd != -1:
			
				newstate = copy.deepcopy(cs)
				newstate[r1][c1] = '.'
				newstate[r2][c2] = cs[r1][c1]
				nh = h(newstate)
				ccost = cd + nd * (10 ** (ord(cs[r1][c1]) - ord('A')))

				if nh not in ass.keys() or ccost < ass[nh]:
					ass[nh] = ccost
					ndfs(newstate, ccost)



	ndfs(s, 0)

	print(ass, len(ass))

	return ass[h(goal)]



# print(solve(ex))
print(solve(f))
