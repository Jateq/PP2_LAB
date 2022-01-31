distance, bullets = input().split()
distance = int(distance)
bullets = int(bullets)
prime = True
if distance > 1:
    for i in range(2, distance):
        if (distance % i) == 0:
            prime = False
            break
if distance < 500 and prime == True and bullets % 2 == 0:
    print('Good job!')
else:
    print('Try next time!')

