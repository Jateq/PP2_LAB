amount = int(input())
hisoka = list()
for i in range(amount):
    n = int(input())
    hisoka.append(n)
for i in hisoka:
    if i <= 10:
        print('Go to work!')
    elif i > 10 and i <= 25:
        print("You are weak")
    elif i > 25 and i <= 45:
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')
    # n++