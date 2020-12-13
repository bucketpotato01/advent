f = open("in.txt", "r")
f = f.read()

f = f.split("\n")

t = int(f[0])

bus = [i for i in f[1].split(",")]

# wait = t*10000
# res = -1
# for i in bus:
# 	div = ((t//i) + 1) * i - t
# 	if div < wait:
# 		wait = div
# 		res = wait * i

# print(res)
from math import gcd

prod = 1
mods = []
rems = []

for i in range(len(bus)):
	
	if bus[i] == "x":
		continue
	prod *= int(bus[i])
	# if i == 0:
	# 	continue
	#divs.append([int(bus[i]), i])
	mods.append(int(bus[i]))
	rems.append(int(bus[i])-i)

	

#print(divs)

def extended_euclidean(a, b): 
	if a == 0: 
		return (b, 0, 1) 
	else: 
		g, y, x = extended_euclidean(b % a, a) 
		return (g, x - (b // a) * y, y) 
  
# modular inverse driver function 
def modinv(a, m): 
	g, x, y = extended_euclidean(a, m) 
	return x % m 
  
# function implementing Chinese remainder theorem 
# list m contains all the modulii 
# list x contains the remainders of the equations 
def crt(m, x): 
  
	# We run this loop while the list of 
	# remainders has length greater than 1 
	while True: 
		  
		# temp1 will contain the new value  
		# of A. which is calculated according  
		# to the equation m1' * m1 * x0 + m0' 
		# * m0 * x1 
		temp1 = modinv(m[1],m[0]) * x[0] * m[1] + modinv(m[0],m[1]) * x[1] * m[0] 
  
		# temp2 contains the value of the modulus 
		# in the new equation, which will be the  
		# product of the modulii of the two 
		# equations that we are combining 
		temp2 = m[0] * m[1] 
  
		# we then remove the first two elements 
		# from the list of remainders, and replace 
		# it with the remainder value, which will 
		# be temp1 % temp2 
		x.remove(x[0]) 
		x.remove(x[0]) 
		x = [temp1 % temp2] + x  
  
		# we then remove the first two values from 
		# the list of modulii as we no longer require 
		# them and simply replace them with the new  
		# modulii that  we calculated 
		m.remove(m[0]) 
		m.remove(m[0]) 
		m = [temp2] + m 
  
		# once the list has only one element left, 
		# we can break as it will only  contain  
		# the value of our final remainder 
		if len(x) == 1: 
			break
  
	# returns the remainder of the final equation 
	return x[0] 

print(mods, rems)
ans= (crt(mods, rems))
for i in range(len(bus)):
	if bus[i] == "x":
		continue
	if (i == 0):
		continue
	print(ans%int(bus[i]), i)


print(ans)

ans = (ans * int(bus[0])) // gcd(ans, int(bus[0]))

print(ans)

for i in range(len(bus)):
	if bus[i] == "x":
		continue

	print(ans%int(bus[i]), i)

