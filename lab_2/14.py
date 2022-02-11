val=input()

orant= list()

while val != '0':
    val = val.split()
    val[2], val[0] = val[0], val[2]
    orant.append(val)
    val = input()
orant.sort()
for i in range(len(orant)):
    orant[i][2],orant[i][0]=orant[i][0],orant[i][2]
for i in orant:
    print(*i)