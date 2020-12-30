f = open("in.txt", "r")
f = f.read()

f = f.split(",")
f = [int(i) for i in f]

lastspoken = {}

for i in range(len(f)-1):
	lastspoken[f[i]] = i;

while (len(f) <= 30000000):
	ind = len(f) - 1
	if f[ind] not in lastspoken.keys():
		f.append(0)
	else:
		f.append(ind - lastspoken[f[ind]])
	
	lastspoken[f[ind]] = ind


print(f[29999999])