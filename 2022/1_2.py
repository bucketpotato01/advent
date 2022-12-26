ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n\n")

  a = []
  for i in s:
    i = [int(x) for x in i.split("\n")]
    a.append(sum(i))

  a.sort()

  return a[-1] + a[-2] + a[-3]

print(solve(ex))
print(solve(f))
