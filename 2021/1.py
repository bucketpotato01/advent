f = open("in.txt", "r")
f = f.read().split("\n")
f = [int(i) for i in f]

ans = 0

for i in range(1, len(f)):
	if f[i] > f[i - 1]:
		ans += 1

print(ans);

a = []
for i in range(2, len(f)):
	a.append(f[i - 2] + f[i - 1] + f[i])

res = 0
for j in range(1, len(a)):
	if a[j] > a[j - 1]:
		res += 1

print(res)