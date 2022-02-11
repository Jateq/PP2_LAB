
  
kleo = int(input())
ikwa = upp = low = j = cur = 0   
arr = list()
col = list()
for i in range(kleo):
    s = input()
    for i in range(len(s)):
        if ord(s[i]) > 47 and ord(s[i]) < 58:
            ikwa += 1
        if ord(s[i]) > 64 and ord(s[i]) < 91:
            upp += 1
        if ord(s[i]) > 96 and ord(s[i]) < 123:
            low += 1
    if ikwa > 0 and low > 0 and upp > 0:
        arr.insert(j,s)
        j += 1
        cur += 1
    ikwa = upp = low = 0
arr = sorted(list(set(arr)))
print(len(arr))
for i in arr:
    print(i)