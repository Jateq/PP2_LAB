from os import kill
from queue import Empty


str = input()
word = input()
killua = list(str)
gon = list()
for i in range(len(killua)):
    if word in killua[i]:
        gon.append(i)
gon.sort()
if len(gon) == 1:
    print(killua.index(word))
else:
    print(killua.index(word), gon[len(gon)-1])