ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n\n")

  ans = 0
  for i in s:
    i = [int(x) for x in i.split("\n")]
    ans = max(ans, sum(i))

  return ans

print(solve(ex))
print(solve(f))
