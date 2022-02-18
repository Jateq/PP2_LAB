c1 = (548, 948, 17, 23, 8, 7,4)

def is_prime(n):
    
    for i in range(2, n//2):
        if n%i == 0:
            return False
    return True

result = filter(is_prime, c1)
print(*result)
# lambda