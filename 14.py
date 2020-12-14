f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

mem = {}
currmask = ""

for i in f:
	i = i.split(" = ")
	if "mem[" in i[0]:
		memmask = bin(int(i[0][4:-1]))[2:]
		val = bin(int(i[1]))[2:]
		
		while len(val) != len(currmask):
			val = "0" + val
		while len(memmask) != len(currmask):
			memmask = "0" + memmask

		memlocs = [0]
		#print(val)
		#temp = ""
		'''
		finval = 0
		
		for j in range(1,len(val)+1):
			c = val[len(val)-j]

			if currmask[len(currmask)-j] != "X":
				c = currmask[len(currmask)-j]
			#temp = c + temp

			finval += int(c) * 2**(j-1)
		'''
		#print(temp)
		#print(finval)

		for j in range(1, len(memmask) + 1):
			if currmask[len(currmask)-j] == "0":
				memlocs = [2**(j-1) * int(memmask[len(memmask)-j]) + k for k in memlocs]
			elif currmask[len(currmask)-j] == "1":
				memlocs = [2**(j-1) + k for k in memlocs]
			else:
				memlocs = memlocs + [2**(j-1) + k for k in memlocs]


		for j in memlocs:
			print(j)
			mem[j] = int(i[1])

		print("-")


	elif "mask" in i[0]:
		currmask = i[1]
	
tot = 0	

for i in mem.values():
	tot += i

print(tot)