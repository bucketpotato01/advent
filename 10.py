f = open("in.txt", "r")
f = f.read().split("\n")


f = sorted([int(i) for i in f])

f.append(f[-1]+3)
f.append(0)
f = sorted(f)
print(f)

dif = [0,0,0]
ways = [0 for i in f]
ways[0] = 1
for i in range(1,len(f)):

	for j in range(i, -1, -1):
		if f[i]-f[j] <= 3:
			ways[i] += ways[j]
		else:
			break

dif[2]+=1
dif[0]+=1

print(dif[0]*(dif[2]))

print(ways)