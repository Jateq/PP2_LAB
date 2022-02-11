arr = list()
# j = [None] * n
try:
    n, x = input().split()
except:
    n = int(input())
    x = int(input())
n = int(n)
x = int(x)
for i in range(n):
    k = x + 2*i
    arr.append(k)
goto = 0
for i in arr:
    goto ^= i
print(goto)