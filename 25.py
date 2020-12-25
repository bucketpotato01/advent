f = open("in.txt", "r")
f = f.read()

f = f.split("\n")
f = [int(i) for i in f]

val = 1
cardloop = 0
doorloop = 0

while val != f[0]:
	val *= 7
	val %= 20201227
	cardloop += 1

val = 1
while val != f[1]:
	val *= 7
	val %= 20201227
	doorloop += 1

print(cardloop, doorloop)

import copy
g = copy.deepcopy(f)
f = [1,1]

for i in range(cardloop):
	f[1] *= g[1]
	f[1] %= 20201227

for i in range(doorloop):
	f[0] *= g[0]
	f[0] %= 20201227

print(f)

v = 1
for i in range(8):
	v *= 17807724
	v %= 20201227

print(v)