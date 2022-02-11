array = list()
amount = input()
amount = int(amount)
array = list(map(int, input().split(' ')))
array.sort()
array.reverse()
array = array[0:2]
sum = 1
for i in array:
    sum *= i 
print(sum)