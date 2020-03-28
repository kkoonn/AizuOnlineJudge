n = int(input())
S = list(map(int, input().split(' ')))
S.sort()
q = int(input())
T = list(map(int, input().split(' ')))

def binarySearch(key):
  left = 0
  right = n - 1
  mid = (left + right) // 2
  while S[mid] != key:
    if left == right:
      return 0
    if S[mid] > key:
      right = mid
    elif S[mid] < key:
      left = mid + 1
    mid = (left + right) // 2
  return 1
  
count = 0
for t in T:
  count += binarySearch(t)
print(count)