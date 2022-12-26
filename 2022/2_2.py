ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n")

  sscore = {"X": 0, "Y": 3, "Z": 6}

  ans = 0
  for i in s:
    i = i.split(" ")
    ans += sscore[i[1]]

    v1 = ord(i[0]) - ord('A')
    v2 = None

    if i[1] == 'X':
      v2 = (v1 + 2) % 3
    elif i[1] == 'Y':
      v2 = v1
    else:
      v2 = (v1 + 1) % 3

    ans += (v2 + 1)

  return ans


print(solve(ex))
print(solve(f))
