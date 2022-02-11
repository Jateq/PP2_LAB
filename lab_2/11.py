alphabet = 'poiuytrewqlkjhgfdsamnbvcxzPOIUYTREWQASDFGHJKLMNBVCXZ' # its for check
arr = list(map(str, input().split()))
col = list()
for i in arr:
    # word = None
    word = ''
    for j in i:
        if j in alphabet:
            word += j
    if col.count(word) == 0:
       col.append(word)
print(len(col))
print('\n'.join([i for i in sorted(col)]))