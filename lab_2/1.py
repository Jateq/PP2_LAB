strings = input()
lst = strings.split()
current = 0
ok = False
l = len(lst) - 1
for i in range(len(lst)):
    if i > current:
        ok = False
        break
    if lst[i] + i > current:
        current = lst[i]+i
    if current >= l:
        print(1)
        ok = True
        break
if ok == False:
    print(0)