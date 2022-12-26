ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n")

  sscore = {"X": 1, "Y": 2, "Z": 3}

  ans = 0
  for i in s:
    i = i.split(" ")
    ans += sscore[i[1]]

    v1 = ord(i[0]) - ord('A')
    v2 = ord(i[1]) - ord('X')

    if v1 == v2:
      ans += 3
    elif (v1 + 1) % 3 == v2:
      ans += 6

  return ans


print(solve(ex))
print(solve(f))
