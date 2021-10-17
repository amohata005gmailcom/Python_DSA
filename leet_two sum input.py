numbers = [0,0,3,4]
target=0
B=[]
C=[]
for i in numbers:
    tg = target - i
    if tg not in B:
        B.append(i)
    else:
        x = numbers.index(tg)+1
        C.append(x)
        C.append(numbers.index(i,x)+1)
print(C)


# O(1)
# low, high = 0, len(numbers) - 1
#         while low < high:
#             sum = numbers[low] + numbers[high]
#             if sum > target:
#                 high -= 1
#             elif sum == target:
#                 return [low + 1, high + 1]
#             else:
#                 low += 1