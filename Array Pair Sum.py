A = [8,11,7,4,5]
k=15
store = set()
output = set()

for i in A:
    target = k-i
    if target not in store:
        store.add(i)
    else:
        output.add((min(i,target),max(i,target)))
print(len(output))
print(store)
print(output)

# A = [1,3,2,2,1,3]
# k = 4
# B = []
# C = []
# for i in A:
#     target = k-i
#     if target not in B:
#         B.append(i)
#         print(B)
#         print("Hello.......................................................")
#     else:
#         if i==target:
#             C.append((min(i, target), max(i, target)))
#         else:
#             C.append((min(i,target),max(i,target)))
#             C.append((max(i, target), min(i, target)))
#         print(C)
#         print("Bye.......................................................")




