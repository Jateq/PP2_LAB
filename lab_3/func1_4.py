def is_prime(num):
    result = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break
    return result
def filter_prime(*primes):
    l = list()
    for i in primes:
        if is_prime(i) == True:
            l.append(i)
    return l
lst = list(map(int, input().split()))
print(*filter_prime(*lst), end = ' ')

