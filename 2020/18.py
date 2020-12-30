f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

def op(val1, val2, op):
	if op == "*":
		return val1 * val2
	
	return val1 + val2



def collapse(s, lo, hi):
	
	cval = 0
	print(lo, hi)
	i = lo
	while (i <= hi):
		print(s)
		#print(i)
		if s[i] == "(":
			j = i
			bal = 1
			for k in range(j+1, hi+1):
				if s[k] == "(":
					bal += 1
				elif s[k] == ")":
					bal -= 1

				if bal == 0:
					bal = k
					break

			numcollapsed = k - i
			thisval = collapse(s, j+1, bal-1)

			s.pop(j+2)
			s.pop(j)

			#cval = op(cval, thisval, s[i-1])

			i += 1
			hi -= numcollapsed

		#elif s[i] in "1234567890":
		#	cval = op(cval, int(s[i]), s[i-1])
		#	i += 1

		else:
			i += 1

	#return cval
	print("removed par")
	i = lo
	while (i <= hi):
		if s[i] == "+":
			newv = int(s[i-1]) + int(s[i+1])
			s.pop(i+1)
			s.pop(i)
			s[i-1] = newv
			i -= 1
			hi -= 2
		else:
			i += 1

	i = lo
	while i <= hi:
		if s[i] == "*":
			newv = int(s[i-1]) * int(s[i+1])
			s.pop(i+1)
			s.pop(i)
			s[i-1] = newv
			i -= 1
			hi -= 2
		else:
			i += 1




	



		
tot = 0

for i in f:
	i = [j for j in "0+"+i if j != " "]
	print(i)
	collapse(i, 0, len(i)-1)
	#print(i)
	tot += int(i[0])

print(tot)