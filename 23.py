f = open("in.txt", "r")
f = f.read()


f = [int(i) for i in f]

print(f)

ind = 0

totnums = 1000000

a = max(f)
for i in range(a+1, totnums+1):
	f.append(i)

sq = int(totnums**0.5)

currind = {}

def redistribute():
	global f, currind
	currind = {}
	newf = []
	for i in f:
		if type(i) == int:
			newf.append(i)
			continue
		for j in i:
			newf.append(j)

	f = []
	for j in range(len(newf)):
		if j % sq == 0:
			f.append([])
		f[-1].append(newf[j])
		currind[newf[j]] = len(f)-1


def get(ind):
	global f, currind
	curr = 0
	cind = 0
	while True:
		if curr + len(f[cind]) > ind:
			break
		curr += len(f[cind])
		cind += 1
	temp = ind - curr
	return f[cind][temp]

def rem(ind):
	global f, currind
	curr = 0
	cind = 0
	while True:
		if curr + len(f[cind]) > ind:
			break
		curr += len(f[cind])
		cind += 1
	temp = ind - curr
	f[cind].pop(temp)

def getind(elem):
	global f, currind
	a = currind[elem]
	previ = 0
	for i in range(a):
		previ += len(f[i])
	return previ + f[a].index(elem)

def putin(ind, elem):
	global f, currind
	curr = 0
	cind = 0
	while True:
		#print(cind, curr)
		if curr + len(f[cind]) > ind or cind == len(f)-1:
			break
		curr += len(f[cind])
		cind += 1
	temp = ind - curr
	f[cind].insert(temp, elem)
	currind[elem] = cind






moves = 10000000
redistribute()
for i in range(moves):
	#print()
	if i%sq == 0:
		redistribute()
		print("itearation",i)
	#print(f)
	#print(ind)
	#print(f)
	thiscup = get(ind)
	#print("chose",thiscup)

	l = []
	d = 0
	for j in range(ind+1, ind+4):
		l.append(j%totnums)
		
	
	l = l[::-1]

	picked = []
	for j in l:
		picked = [get(j)] + picked
	l = sorted(l)[::-1]

	#print(picked)
	ind += d

	for j in l:
		rem(j)

	#print(picked)


	lab = thiscup - 1
	while lab in picked or lab == 0:
		#print("temp:",lab)
		lab = (lab - 1 + totnums + 1) % (totnums + 1)

	#print("lab", lab)

	newind = getind(lab)

	for j in range(len(picked)):
		putin(newind+j+1,picked[j])

	#f = f[:newind+1] + picked + f[newind+1:]

	#print("thiscup", thiscup)
	ind = getind(thiscup)
	ind = (ind + 1) % totnums
	#print(f)


'''
ans = ""
for i in range(ind,len(f)):
	ans = ans + str(f[i])
for i in range(ind):
	ans = ans + str(f[i])

print(ans)
'''

fin = []
for i in f:
	for j in i:
		fin.append(j)

a = open("save.txt", "w")
a.write(str(fin))
a.close()

