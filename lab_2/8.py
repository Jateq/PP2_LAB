import math

arr = list(map(int, input().split()))
kaed = list()

def point(kaed):
    return math.sqrt(((kaed[0] - arr[0])**2) + ((kaed[1] - arr[1])**2))

n = int(input())

for i in range(n):
    inp = list(map(int, input().split()))
    kaed.append(inp)
kaed.sort(key=point)

for i in range(n):
    for j in range(2):
        print(kaed[i][j], end=" ")
    print()
    
