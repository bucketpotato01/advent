ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n")

  ans = 0
  for i in s:
    i = [[int(j) for j in x.split("-")] for x in i.split(",")]

    l1 = i[0][0]
    r1 = i[0][1]

    l2 = i[1][0]
    r2 = i[1][1]

    if (l2 <= l1 and r1 <= r2) or (l1 <= l2 and r2 <= r1):
      ans += 1

  return ans

print(solve(ex))
print(solve(f))
