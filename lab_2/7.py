number = int(input())
demons = dict()
demon_slayer_corps = dict()
for i in range(number):
    name, k = input().split()
    if k in demons:
        demons[k] += 1
    elif not k in demons:
        demons[k] = 1
m = int(input())
for i in range(m):
    name, k, times = input().split()
    if k in demon_slayer_corps:
        demon_slayer_corps[k] += int(times)
    elif not k in demon_slayer_corps:
        demon_slayer_corps[k] = int(times)
sum = 0
for k in demons:
    if not k in demon_slayer_corps:
        sum += demons[k]
    elif demons[k] - demon_slayer_corps[k] >= 0 and k in demon_slayer_corps:
        sum += demons[k] - demon_slayer_corps[k]
print('Demons left: ' + str(sum))