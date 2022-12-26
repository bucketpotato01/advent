ex = open("example.txt", "r").read()
f = open("in.txt", "r").read()

def priority(j):
  if ord('A') <= ord(j) and ord(j) <= ord('Z'):
    return (ord(j) - ord('A') + 27)
  else:
    return (ord(j) - ord('a') + 1)

def solve(s):
  s = s.split("\n")

  ans = 0
  for i in range(0, len(s), 3):

    s1 = s[i]
    s2 = s[i + 1]
    s3 = s[i + 2]

    for j in s1:
      if j in s2 and j in s3:
        ans += priority(j)
        break

  return ans

print(solve(ex))
print(solve(f))
