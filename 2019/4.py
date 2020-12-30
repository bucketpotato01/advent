f = open("in.txt", "r")
f = f.read()

f = [int(i) for i in f.split("-")]
print(f)
res = 0

for i in range(f[0], f[1]+1):
	s = str(i)
	ok = True
	hasdoub = False

	msofar = 0
	for j in s:
		if int(j) < msofar:
			ok = False
			break
		msofar = max(msofar, int(j))

	# for j in range(1,len(s)):
	# 	if s[j] == s[j-1]:
	# 		hasdoub = True

	for j in range(10):
		if str(j)*2 in s and str(j)*3 not in s:
			hasdoub = True


	if not hasdoub:
		ok = False

	if ok:
		res += 1

print(res)