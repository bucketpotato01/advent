ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def solve(s):
  s = s.split("\n")

  ans = 0
  for i in s:
    n = len(i) // 2
    fv = i[:n]
    sv = i[n:]

    for j in fv:
      if j in sv:
        if ord('A') <= ord(j) and ord(j) <= ord('Z'):
          ans += (ord(j) - ord('A') + 27)
        else:
          ans += (ord(j) - ord('a') + 1)
        break

  return ans

print(solve(ex))
print(solve(f))
