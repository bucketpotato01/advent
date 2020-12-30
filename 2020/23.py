f = open("in.txt", "r")
f = f.read()


f = [int(i) for i in f]


ind = 0

totnums = 1000000

a = max(f)

ptrs = [0] + [(i+2) for i in range(totnums)]
ptrs[-1] = f[0]

for i in range(1, len(f)):
	ptrs[f[i-1]] = f[i]

ptrs[f[-1]] = a+1

moves = 10000000

curr = f[0]
for i in range(moves):
	picked = []
	temp = curr

	for j in range(3):
		temp = ptrs[temp]
		picked.append(temp)

	nextcup = curr - 1
	while nextcup in picked or nextcup == 0:
		nextcup = (nextcup - 1 + totnums+1) % (totnums+1)

	#print(ptrs, picked, nextcup)

	ptrs[curr] = ptrs[temp]
	picked = picked[::-1]

	temp = ptrs[nextcup]
	for j in picked:
		ptrs[j] = temp
		temp = j
	ptrs[nextcup] = temp

	curr = ptrs[curr]

	if i % 10000 == 0:
		print(i)


n1 = ptrs[1]
n2 = ptrs[n1]
print(n1, n2, n1*n2)


	


