n = int(input())
my_dict = {}

for i in range(n):
  order, key = input().split(' ')
  if order == 'insert':
    my_dict[key] = True
  elif order== 'find':
    if key in my_dict.keys():
      print('yes')
    else:
      print('no')