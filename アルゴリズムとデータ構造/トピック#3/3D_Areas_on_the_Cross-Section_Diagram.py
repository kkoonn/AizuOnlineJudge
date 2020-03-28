mountains = list(input())
stack1, stack2 = [], []

for i, grad in enumerate(mountains):
    if grad == '\\':
        stack1.append(i)
    elif grad == '/':
        if stack1:
          left = stack1.pop(-1)
          right = i
          space = right - left
          while stack2 and stack2[-1][0] > left:
            space += stack2.pop(-1)[1]
          stack2.append([left, space])
    else:
        pass
#print(stack2)
space_list = [space for index, space in stack2]
print(sum(space_list))
print(len(space_list), *space_list)