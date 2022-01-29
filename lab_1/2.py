food = input()
ASCII_values = list()
for character in food:
   ASCII_values.append(ord(character))
sum = 0
for i in range(len(ASCII_values)):
    sum += ASCII_values[i]
if sum >= 300:
    print( "It is tasty!")
else:
    print("Oh, no!")