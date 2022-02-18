c1 = (548, 948, 17, 23, 8, 7)

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

result = filter(is_prime, c1)