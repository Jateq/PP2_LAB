amount = int(input())
if amount % 2 == 0:
    for i in range(amount):
        for j in range(amount):
            if i >= j:
                print('#',end = "")
            else:
                print('.', end = "")
        print(' ')
else:
    for i in range(amount):
        for j in range(amount):
            if i + j >= amount-1:
                print('#',end = "")
            else:
                print('.', end = "")
        print(' ')
