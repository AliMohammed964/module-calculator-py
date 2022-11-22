test = ['R', 'A', 'M', 'A', 'D', 'A', 'N', 'K', 'A', 'E', 'E', 'M']
print("Original list ", str(test))
counter = 0
for item in test:
    if 'A' in item:
        counter += 1

print("The number of A : ", counter)

res = [sub.replace('M', 'N') for sub in test]
print("List after replace ", str(res))


res = [item.removeprefix('E')for item in test]
print("List after delete E ", str(res))


