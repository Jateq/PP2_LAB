
x = 94
y = 35
def solve(numheads,numlegs):
   ch = numlegs // 2 - numheads 
   ra = numheads - ch
   return ch, ra

print(*solve(y,x), end= ' ')