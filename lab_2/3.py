amount = int(input())

for i in range(amount):
    for j in range(amount):
        if j == 0:
            print(i,end = " ")
        elif i == 0:
            print(j,end = " ")
        elif i == j:
            print(i * j,end = " ")
        else:
            print("0",end = " ")
    print(' ')