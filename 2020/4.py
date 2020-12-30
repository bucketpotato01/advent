f = open("in.txt", "r")
f = f.read().split("\n")


for i in range(len(f)):
	if f[i] == "":
		f[i] = "\n"
	else:
		f[i] = f[i] + " "
f = "".join(f).split("\n")
res = 0


for i in f:
	if "byr:" in i and "iyr:" in i and "eyr:" in i and "hgt:" in i and "hcl:" in i and "ecl:" in i and "pid:" in i:
		res += 1
	else:
		continue
	
	i = i.split(" ")

	ok = True
	for j in i:
		if "byr:" in j:
			yr = int(j[4:])
			
			if yr < 1920 or yr > 2002:
				ok = False
		elif "iyr:" in j:
			yr = int(j[4:])

			if yr < 2010 or yr > 2020:
				ok = False

		elif "eyr:" in j:
			yr = int(j[4:])
			if yr < 2020 or yr > 2030:
				ok = False
		elif "hgt:" in j:

			if len(j) <= 6:
				ok = False
				continue
			ty = j[-2:]
			#print(ty)
			num = int(j[4:-2])
			if ty == "cm":
				if num < 150 or num > 193:
					ok = False
			elif ty == "in":
				if num < 59 or num > 76:
					ok = False
			else:
				ok = False

		elif "hcl:" in j:
			t = j[4:]
			if t[0] != "#" or [p for p in t[1:] if p not in "1234567890abcdef"] != []:
				ok = False

		elif "ecl:" in j:
			t = j[4:]
			if t not in "amb blu brn gry grn hzl oth".split(" "):
				ok = False

		elif "pid:" in j:
			t = j[4:]
			if len(t) != 9:
				ok = False
			for p in t:
				if p not in "1234567890":
					ok = False

	if ok == False:
		res -= 1


print(res)