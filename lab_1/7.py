#bin to decimal
binary = input()
illumi = list()
for i in range(len(binary)):
    illumi.append(binary[i])
illumi.reverse()

def recursion(i):
    result = 0
    if i == len(binary):
        return result
    else:
        k = illumi[i]
        k = int(k)
        result = k * 2**i
        return result + recursion(i+1)
print(recursion(0))

