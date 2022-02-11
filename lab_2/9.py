n = int(input())

col = list()
chel = 0

for i in range(n):
    arr = list(map(str, input().split()))
    if arr[0] == "1":
        col.append(arr[1])
    else:
        chel += 1

print(*[col[i] for i in range(chel)])