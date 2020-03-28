n = int(input())
S = list(map(int, input().split(' ')))
q = int(input())
T = list(map(int, input().split(' ')))

def linearSearch(key):
  i = 0
  len_pre_S = len(S)
  S.append(key)
  while S[i] != key:
    i += 1
  if i == len_pre_S:
    return 0
  return 1

count = 0
for t in T:
  count += linearSearch(t)
print(count)