n = int(input())
joke = dict()
max = -999
for i in range(n):
    name, money = input().split()
    money = int(money) 
    if name in joke:
        joke[name] += money
    else:
        joke[name] = money

for k, v in joke.items():
    if v > max:
        max = v
for k, v in sorted(joke.items()):
    if max - v == 0:
        print(k + " is lucky!")
    else:
        print(k + " has to receive " + str(max - joke[k]) + " tenge ")