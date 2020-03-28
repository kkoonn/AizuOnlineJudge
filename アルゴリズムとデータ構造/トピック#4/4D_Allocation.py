n, k = list(map(int, input().split(' ')))
w = [int(input()) for i in range(n)]

left = 0
right = 100000 * 10000

def check(loaded_w):
  truck_num = 1
  tmp_w = 0
  i = 0
  while i < n:
    if tmp_w + w[i] > loaded_w:
      truck_num += 1
      tmp_w = 0
    else:
      tmp_w += w[i]
      i += 1
    if truck_num > k:
      return False
  return True

while left != right:
  mid = (left + right) // 2
  if check(mid):
    right = mid
  else:
    left = mid + 1
print(left)